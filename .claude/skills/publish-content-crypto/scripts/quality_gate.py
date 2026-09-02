#!/usr/bin/env python3
"""Deterministic quality gate for a thecrypto.wiki post MDX (skill Step 3).

Usage:
  python3 quality_gate.py <post.mdx> [--db <content-database.json>]
      [--archive <image dir>] [--type post|exchange|og]

Runs every Step-3 check and prints one line per check (PASS / WARN / FAIL).
Exits non-zero if any hard FAIL is found (WARN does not fail the gate).

Crypto-wiki only. For tinnitushelp.me use publish-content-tinnitus's own copy
of this script in tinnitus-help-automation - the two sites differ in almost
every surface detail (link prefixes, image syntax, ad component, frontmatter
quoting, whether an author field exists), which is why this is a separate
script rather than one shared script branching on site.
"""
import argparse, json, os, re, sys
from datetime import datetime

DB = "/Users/oktayshakirov/Coding/crypto-wiki-automation/content-database.json"
ARCHIVE = "/Users/oktayshakirov/Coding/crypto-wiki/public/images/posts"
DOMAIN = "https://www.thecrypto.wiki"
# Non-content link targets that are valid but never in the DB.
STATIC = {"/app", "/tools", "/search", "/about", "/posts",
          "/exchanges", "/crypto-ogs", "/categories"}

FAIL, WARN, PASS = "FAIL", "WARN", "PASS"
results = []  # (level, check, detail)


def record(level, check, detail=""):
    results.append((level, check, detail))


def check(cond, name, ok_detail="ok", bad_detail="", level=FAIL):
    record(PASS if cond else level, name, ok_detail if cond else bad_detail)


# Content directory -> URL prefix.
CONTENT_DIRS = {"posts": "/posts/", "exchanges": "/exchanges/",
                "crypto-ogs": "/crypto-ogs/", "tools": "/tools/"}


def valid_slugs(db, mdx_path):
    """Set of valid internal link targets.

    Union of the content DB and the MDX actually on disk. The DB drifts, and
    a link to a page that really exists must not fail the gate.
    """
    out = set(STATIC)

    for key, pref in (("posts", "/posts/"), ("exchanges", "/exchanges/"),
                      ("crypto_ogs", "/crypto-ogs/"), ("tools", "/tools/")):
        for v in db.get(key, {}).values():
            s = (v.get("slug") or "").lstrip("/")
            if s.startswith(("posts/", "exchanges/", "crypto-ogs/", "tools/")):
                out.add("/" + s)
            else:
                out.add(pref + s)

    # ...plus whatever is actually published in the site repo's content tree.
    content_root = os.path.dirname(os.path.dirname(os.path.abspath(mdx_path)))
    for sub, pref in CONTENT_DIRS.items():
        d = os.path.join(content_root, sub)
        if not os.path.isdir(d):
            continue
        for fn in os.listdir(d):
            if fn.endswith(".mdx") and not fn.startswith("_"):
                out.add(pref + fn[:-4])
    return out


def imgs_in(txt):
    return re.findall(r"!\[[^\]]*\]\((/images/[^)\s]+)\)", txt)


def strip_tables(txt):
    """Drop markdown table separator rows (| --- | --- |).

    Legitimate table syntax, but looks like a banned `--` to the dash check.
    """
    return "\n".join(ln for ln in txt.split("\n")
                     if not re.match(r"^\s*\|[\s:|-]+\|\s*$", ln))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mdx")
    ap.add_argument("--db", default=DB)
    ap.add_argument("--archive", default=ARCHIVE)
    ap.add_argument("--type", default=None,
                    choices=["post", "exchange", "og"],
                    help="content type; inferred from the path when omitted")
    ap.add_argument("--recent-window", type=int, default=5,
                    help="how many of the most recent other posts to check for "
                         "repeated body images (reuse is fine, just not back to back)")
    a = ap.parse_args()

    p = os.path.abspath(a.mdx).replace(os.sep, "/")
    if a.type is None:
        a.type = ("exchange" if "/exchanges/" in p
                  else "og" if "/crypto-ogs/" in p
                  else "post")
    record(PASS, "type", a.type)

    text = open(a.mdx, encoding="utf-8").read()
    parts = text.split("---", 2)
    if len(parts) < 3:
        record(FAIL, "frontmatter", "no --- frontmatter block")
        emit_and_exit()
    fm, body = parts[1], parts[2]
    db = json.load(open(a.db))

    # --- word count ---
    words = len(re.findall(r"\b[\w'-]+\b",
                           re.sub(r"<[^>]+>|!\[.*?\]\(.*?\)", "", body)))
    record(PASS if 1200 <= words <= 2500 else WARN, "word count",
           f"{words} (target 1,200-2,500)")

    # --- description length ---
    # Posts run long (SEO meta). Exchange cards wrap the description in a fixed
    # tile: past ~125 chars it spills to a 5th row and looks off next to the
    # rest of the grid, so exchanges target the existing pages' 90-125 band.
    # OG pages sit in the same card grid and measure the same way.
    desc_range = {"post": (150, 160), "exchange": (90, 125), "og": (90, 125)}[a.type]
    m = re.search(r"""description:\s*(['"])(.*)\1""", fm)
    if m:
        desc = m.group(2)
        dl = len(desc)
        lo, hi = desc_range
        record(PASS if lo <= dl <= hi else WARN, "description length",
               f"{dl} chars (target {lo}-{hi} for {a.type})")
    else:
        desc = ""
        record(FAIL, "description", "missing description in frontmatter")

    # --- quickFacts / faqs: required on exchanges AND crypto-OGs ---
    # ExchangeSingle.js and CryptoOgSingle.js both render these (as
    # ExchangeQuickFacts / PersonQuickFacts plus ExchangeFaq) and both feed
    # faqSchema(), so a missing block silently costs the FAQ rich result and
    # the whole quick-facts panel. All 33 live OG pages carry both; this used
    # to be checked on exchanges only, which left OGs unguarded.
    if a.type in ("exchange", "og"):
        for block in ("quickFacts", "faqs"):
            check(bool(re.search(rf"^{block}:", fm, re.M)), f"{block} present",
                  bad_detail="missing")

    # --- meta_title: required on exchanges AND crypto-OGs ---
    # Without it both layouts fall back to a shared boilerplate title
    # ("<X> Review | In-Depth Exchange Analysis", "<X> | Achievements,
    # Contributions & Impact"). That filler is identical on every page, eats
    # ~30 of the ~60 usable characters, and mismatches the intent that actually
    # drives traffic here: GSC shows the demand is encyclopedia-shaped
    # ("trade republic wiki", "michael saylor wiki"), which the word "Review"
    # reads as the wrong page type. Every live entity page now sets one.
    if a.type in ("exchange", "og"):
        mt = re.search(r"""^meta_title:\s*(['"])(.*)\1""", fm, re.M)
        if not mt:
            record(FAIL, "meta_title", "missing - page would fall back to "
                   "the shared boilerplate title")
        else:
            mt_val = mt.group(2)
            n = len(mt_val)
            record(PASS if n <= 60 else WARN, "meta_title length",
                   f"{n} chars (keep <=60 or Google truncates)")
            # "Wiki" is generic and fine. "Wikipedia" is a Wikimedia Foundation
            # trademark - targeting the query is legitimate, claiming to be
            # them is not.
            record(FAIL if "wikipedia" in mt_val.lower() else PASS,
                   "meta_title trademark",
                   "contains 'Wikipedia' (trademark) - use 'Wiki' instead"
                   if "wikipedia" in mt_val.lower() else "ok")

    # --- freshness ---
    # `updated` feeds dateModified and the visible "Last updated:" line; without
    # it both fall back to `date`. Not required on a new page - it has never
    # been revised - but it must be a real date and never precede `date`.
    mu = re.search(r"^updated:\s*['\"]?([0-9]{4}-[0-9]{2}-[0-9]{2})", fm, re.M)
    md_ = re.search(r"^date:\s*['\"]?([0-9]{4}-[0-9]{2}-[0-9]{2})", fm, re.M)
    if re.search(r"^updated:", fm, re.M) and not mu:
        record(FAIL, "updated format",
               "present but not an ISO YYYY-MM-DD date")
    elif mu and md_:
        record(PASS if mu.group(1) >= md_.group(1) else FAIL, "updated >= date",
               f"updated {mu.group(1)}, date {md_.group(1)}")

    # --- author ---
    check("Oktay Shakirov" in fm, "author", "Oktay Shakirov", "author not found")

    # --- links: count, dedupe, bold, slug validity ---
    links = re.findall(r"\[([^\]]+)\]\((/[^)]+)\)", body)
    internal = [(t, u) for t, u in links if not u.startswith("/images/")]
    record(PASS if 8 <= len(internal) <= 15 else WARN, "internal link count",
           f"{len(internal)} (target 8-15)")

    seen, dups = set(), set()
    for _, u in internal:
        (dups if u in seen else seen).add(u)
    check(not dups, "no duplicate links",
          bad_detail="dupes: " + ", ".join(sorted(dups)))

    bold = set(re.findall(r"\*\*\[[^\]]+\]\((/[^)]+)\)\*\*", body))
    notbold = [u for _, u in internal if u not in bold]
    check(not notbold, "links bolded",
          bad_detail="not bold: " + ", ".join(notbold))

    valid = valid_slugs(db, a.mdx)
    # Strip #anchors and ?query - a deep link into a real page is still valid.
    invalid = [u for _, u in internal
               if u.split("#")[0].split("?")[0].rstrip("/") not in valid]
    check(not invalid, "slugs valid vs DB",
          bad_detail="invalid: " + ", ".join(invalid))

    # --- frontmatter crypto-ogs / exchanges must actually be linked in body ---
    linked = {u for _, u in internal}

    def fm_list(field):
        m2 = re.search(r"^%s:\s*\[(.*?)\]" % re.escape(field), fm, re.M)
        if not m2:
            return []
        return [x.strip().strip("\"'") for x in m2.group(1).split(",") if x.strip()]

    def slug_for(section, name):
        want = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
        for v in db.get(section, {}).values():
            slug = (v.get("slug") or "").lstrip("/").split("/")[-1]
            title = (v.get("title") or "").strip().lower()
            if title == name.strip().lower() or slug == want:
                return slug
        return None

    orphans = []
    for field, section, prefix in (("crypto-ogs", "crypto_ogs", "/crypto-ogs/"),
                                   ("exchanges", "exchanges", "/exchanges/")):
        for name in fm_list(field):
            s = slug_for(section, name)
            if s is None:
                orphans.append(f"{name} (not in DB)")
            elif prefix + s not in linked:
                orphans.append(f"{name} (no body link)")
    check(not orphans, "frontmatter ogs/exchanges linked in body",
          bad_detail="; ".join(orphans))

    # --- images ---
    mi = re.search(r"""image:\s*(['"])([^'"]+)\1""", fm)
    main_img = mi.group(2) if mi else ""
    body_imgs = imgs_in(body)

    check(len(body_imgs) == 2, "exactly 2 body images",
          f"{len(body_imgs)} found", f"{len(body_imgs)} found")
    check(bool(main_img) and main_img not in body_imgs,
          "main image != body images", main_img,
          main_img or "no main image in frontmatter")
    extra = body_imgs

    missing = [q for q in body_imgs
               if not os.path.exists(os.path.join(a.archive, os.path.basename(q)))]
    check(not missing, "images exist in archive",
          bad_detail=f"missing from {a.archive}: " + ", ".join(missing))

    # --- shared images not repeated in nearby posts ---
    # Reusing an archive image is fine and expected. What is not fine is reusing
    # it in posts published close together, because someone reading a few in a
    # row sees the same picture twice. So compare only against the N most
    # recent OTHER posts, by frontmatter date, not the archive as a whole. The
    # main image is slug-specific and never shared, so it is excluded.
    def post_date(txt):
        d = re.search(r"^date:\s*['\"]?([^'\"\n]+)['\"]?\s*$", txt, re.M)
        if not d:
            return None
        raw = d.group(1).strip()
        for fmt in ("%Y-%m-%d", "%B %d, %Y", "%b %d, %Y"):
            try:
                return datetime.strptime(raw, fmt)
            except ValueError:
                continue
        return None

    mine = set(extra) - {main_img}
    content_dir = os.path.dirname(os.path.abspath(a.mdx))
    others = []
    for fn in os.listdir(content_dir):
        if not fn.endswith(".mdx") or fn == os.path.basename(a.mdx) or fn.startswith("_"):
            continue
        txt = open(os.path.join(content_dir, fn), encoding="utf-8", errors="ignore").read()
        dt = post_date(txt)
        if dt:
            others.append((dt, fn, txt))
    others.sort(reverse=True)

    clashes = []
    for dt, fn, txt in others[:a.recent_window]:
        used = set(imgs_in(txt))
        for q in sorted(mine & used):
            clashes.append(f"{os.path.basename(q)} also in {fn[:-4]} ({dt:%Y-%m-%d})")
    record(PASS if not clashes else WARN,
           f"images not reused in last {a.recent_window} posts",
           "ok" if not clashes else "; ".join(clashes))

    # --- dashes / curly quotes (body + user-facing description) ---
    hygiene = strip_tables(body) + "\n" + desc
    bad_dash = [c for c in ("—", "–") if c in hygiene] + (["--"] if "--" in hygiene else [])
    check(not bad_dash, "no em/en/-- dashes",
          bad_detail="found: " + " ".join(bad_dash))

    curly = {c: hygiene.count(c) for c in "‘’“”" if hygiene.count(c)}
    check(not curly, "no curly quotes",
          bad_detail=", ".join(f"{k}x{v}" for k, v in curly.items()))

    # --- metadata / references ---
    record(PASS if not re.search(r"```[\s\S]*\{[\s\S]*\}[\s\S]*```\s*$", body)
           and not re.search(r"^\s*\{[\s\S]*\}\s*$", body.strip()[-400:] or "x")
           else WARN, "no trailing metadata JSON", "ok")

    check(not re.search(r"^#+\s*References\b", body, re.M), "no References section")

    # --- structure ---
    if a.type == "post":
        record(PASS if re.match(r"\s*##\s", body) else WARN, "starts with ## heading",
               "ok" if re.match(r"\s*##\s", body) else "does not start with ##")

    # --- ads present + not adjacent to images ---
    check("ArticleAd" in body, "<ArticleAd /> present", bad_detail="no ArticleAd in body")

    sig = [(i, ln) for i, ln in enumerate(body.split("\n"))
           if "ArticleAd" in ln or ln.strip().startswith("![")]
    adj = []
    for (i1, l1), (i2, l2) in zip(sig, sig[1:]):
        k1 = "AD" if "ArticleAd" in l1 else "IMG"
        k2 = "AD" if "ArticleAd" in l2 else "IMG"
        if k1 != k2 and i2 - i1 <= 2:
            adj.append(f"lines {i1+1}->{i2+1}")
    check(not adj, "ads not adjacent to images", bad_detail="; ".join(adj))

    emit_and_exit()


def emit_and_exit():
    icon = {PASS: "✓", WARN: "⚠", FAIL: "✗"}
    for level, chk, detail in results:
        print(f"  {icon[level]} {level:4} {chk}" + (f" - {detail}" if detail else ""))
    fails = sum(1 for l, _, _ in results if l == FAIL)
    warns = sum(1 for l, _, _ in results if l == WARN)
    print(f"\n{'FAILED' if fails else 'PASSED'}: {fails} fail, {warns} warn, "
          f"{len(results)} checks")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
