#!/usr/bin/env python3
"""Deterministic quality gate for a crypto-wiki post MDX (skill Step 3).

Usage:
  python3 quality_gate.py <post.mdx> [--db <content-database.json>]
      [--archive <crypto-wiki/public/images/posts>] [--type post]

Runs every Step-3 check and prints one line per check (PASS / WARN / FAIL).
Exits non-zero if any hard FAIL is found (WARN does not fail the gate).

Defaults assume the standard repo layout under /Users/oktayshakirov/Coding.
Currently implements the crypto **post** checklist (the richest one); pass
--type to relax post-only rules for other content types later.
"""
import argparse, json, os, re, sys

DEFAULT_DB = "/Users/oktayshakirov/Coding/crypto-wiki-automation/content-database.json"
DEFAULT_ARCHIVE = "/Users/oktayshakirov/Coding/crypto-wiki/public/images/posts"

FAIL, WARN, PASS = "FAIL", "WARN", "PASS"
results = []  # (level, check, detail)


def record(level, check, detail=""):
    results.append((level, check, detail))


def valid_slugs(db):
    """Set of valid internal link targets (/posts/.., /exchanges/.., etc.)."""
    out = set()
    prefixes = {"posts": "/posts/", "exchanges": "/exchanges/",
                "crypto_ogs": "/crypto-ogs/", "tools": "/tools/"}
    for key, pref in prefixes.items():
        for v in db.get(key, {}).values():
            s = (v.get("slug") or "").lstrip("/")
            if s.startswith(("posts/", "exchanges/", "crypto-ogs/", "tools/")):
                out.add("/" + s)
            else:
                out.add(pref + s)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mdx")
    ap.add_argument("--db", default=DEFAULT_DB)
    ap.add_argument("--archive", default=DEFAULT_ARCHIVE)
    ap.add_argument("--type", default="post")
    a = ap.parse_args()

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

    # --- description length (crypto post: 150-160) ---
    m = re.search(r'description:\s*"(.*)"', fm)
    if m:
        dl = len(m.group(1))
        record(PASS if 150 <= dl <= 160 else WARN, "description length",
               f"{dl} chars (target 150-160)")
    else:
        record(FAIL, "description", "missing description in frontmatter")

    # --- author ---
    record(PASS if "Oktay Shakirov" in fm else FAIL, "author",
           "Oktay Shakirov" if "Oktay Shakirov" in fm else "author not found")

    # --- links: count, dedupe, bold, slug validity ---
    links = re.findall(r"\[([^\]]+)\]\((/[^)]+)\)", body)
    internal = [(t, u) for t, u in links if not u.startswith("/images/")]
    record(PASS if 8 <= len(internal) <= 15 else WARN, "internal link count",
           f"{len(internal)} (target 8-15)")

    seen, dups = set(), set()
    for _, u in internal:
        (dups if u in seen else seen).add(u)
    record(PASS if not dups else FAIL, "no duplicate links",
           "ok" if not dups else "dupes: " + ", ".join(sorted(dups)))

    bold = set(re.findall(r"\*\*\[[^\]]+\]\((/[^)]+)\)\*\*", body))
    notbold = [u for _, u in internal if u not in bold]
    record(PASS if not notbold else FAIL, "links bolded",
           "ok" if not notbold else "not bold: " + ", ".join(notbold))

    valid = valid_slugs(db)
    invalid = [u for _, u in internal if u not in valid]
    record(PASS if not invalid else FAIL, "slugs valid vs DB",
           "ok" if not invalid else "invalid: " + ", ".join(invalid))

    # --- body images: exactly 2, in archive, != main image ---
    body_imgs = re.findall(r"!\[[^\]]*\]\((/images/[^)]+)\)", body)
    record(PASS if len(body_imgs) == 2 else FAIL, "exactly 2 body images",
           f"{len(body_imgs)} found")
    missing = [p for p in body_imgs
               if not os.path.exists(os.path.join(a.archive, os.path.basename(p)))]
    record(PASS if not missing else FAIL, "body images in archive",
           "ok" if not missing else "missing: " + ", ".join(missing))
    mi = re.search(r'image:\s*"([^"]+)"', fm)
    main_img = mi.group(1) if mi else ""
    record(PASS if main_img and main_img not in body_imgs else FAIL,
           "main image != body images",
           main_img or "no main image in frontmatter")

    # --- dashes / curly quotes (body + user-facing description) ---
    desc = m.group(1) if m else ""
    hygiene = body + "\n" + desc
    bad_dash = [c for c in ("—", "–") if c in hygiene] + (["--"] if "--" in hygiene else [])
    record(PASS if not bad_dash else FAIL, "no em/en/-- dashes",
           "ok" if not bad_dash else "found: " + " ".join(bad_dash))

    curly = {c: hygiene.count(c) for c in "‘’“”" if hygiene.count(c)}
    record(PASS if not curly else FAIL, "no curly quotes",
           "ok" if not curly else ", ".join(f"{k}x{v}" for k, v in curly.items()))

    # --- metadata / references / heading ---

    record(PASS if not re.search(r"```[\s\S]*\{[\s\S]*\}[\s\S]*```\s*$", body)
           and not re.search(r"^\s*\{[\s\S]*\}\s*$", body.strip()[-400:] or "x")
           else WARN, "no trailing metadata JSON", "ok")

    record(PASS if not re.search(r"^#+\s*References\b", body, re.M) else FAIL,
           "no References section", "ok")

    if a.type == "post":
        record(PASS if re.match(r"\s*##\s", body) else WARN, "starts with ## heading",
               "ok" if re.match(r"\s*##\s", body) else "does not start with ##")

    # --- ads not adjacent to images ---
    sig = [(i, ln) for i, ln in enumerate(body.split("\n"))
           if "ArticleAd" in ln or ln.strip().startswith("![")]
    adj = []
    for (i1, l1), (i2, l2) in zip(sig, sig[1:]):
        k1 = "AD" if "ArticleAd" in l1 else "IMG"
        k2 = "AD" if "ArticleAd" in l2 else "IMG"
        if k1 != k2 and i2 - i1 <= 2:
            adj.append(f"lines {i1+1}->{i2+1}")
    record(PASS if not adj else FAIL, "ads not adjacent to images",
           "ok" if not adj else "; ".join(adj))

    emit_and_exit()


def emit_and_exit():
    icon = {PASS: "✓", WARN: "⚠", FAIL: "✗"}
    for level, check, detail in results:
        print(f"  {icon[level]} {level:4} {check}" + (f" - {detail}" if detail else ""))
    fails = sum(1 for l, _, _ in results if l == FAIL)
    warns = sum(1 for l, _, _ in results if l == WARN)
    print(f"\n{'FAILED' if fails else 'PASSED'}: {fails} fail, {warns} warn, "
          f"{len(results)} checks")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
