#!/usr/bin/env python3
"""
verify_socials.py — resolve-check candidate social/app links before writing them
into an exchange review's frontmatter.

Part of the "discover -> verify -> write" social-enrichment system.
Discovery is done by Claude via web search; this script does the VERIFY step:
given candidate URLs, it reports whether each one actually resolves to a real
page (not a 404), so only confirmed links get written.

Usage:
  echo '{"twitter":"https://x.com/Bitstamp","android":"https://play.google.com/store/apps/details?id=net.bitstamp.app"}' \
    | python3 scripts/verify_socials.py
  # or
  python3 scripts/verify_socials.py twitter=https://x.com/Bitstamp android=...

Output: JSON map of platform -> {url, status, ok} where status is
  OK         (resolves, 2xx)
  MISSING    (404/410 — drop it)
  AMBIGUOUS  (bot-blocked / login wall / non-2xx that isn't a clear 404)
Exit code is always 0; the caller (Claude) decides what to keep.
"""
import sys, json, urllib.request, urllib.error, urllib.parse, re

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36")


def fetch_status(url, method="GET"):
    req = urllib.request.Request(url, method=method, headers={
        "User-Agent": UA,
        "Accept": "text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
    })
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            return r.getcode(), r.geturl(), r.read(4000).decode("utf-8", "ignore")
    except urllib.error.HTTPError as e:
        return e.code, url, ""
    except Exception as e:
        return None, url, str(e)


def verify_apple(url):
    """Apple App Store: use the iTunes lookup API (reliable JSON, no bot wall)."""
    m = re.search(r"/id(\d+)", url)
    if not m:
        return "AMBIGUOUS"
    code, _, body = fetch_status(
        f"https://itunes.apple.com/lookup?id={m.group(1)}")
    if code == 200:
        try:
            return "OK" if json.loads(body).get("resultCount", 0) > 0 else "MISSING"
        except Exception:
            return "AMBIGUOUS"
    return "AMBIGUOUS"


def verify(platform, url):
    host = urllib.parse.urlparse(url).netloc.lower()
    if "apps.apple.com" in host:
        return verify_apple(url)
    code, final, body = fetch_status(url)
    if code is None:
        return "AMBIGUOUS"
    if code in (404, 410):
        return "MISSING"
    if 200 <= code < 300:
        # Google Play returns 200 with a "not found" body for bad ids
        if "play.google.com" in host and re.search(
                r"we're sorry, the requested URL was not found", body, re.I):
            return "MISSING"
        # Instagram/Twitter sometimes 200 a generic page; treat as OK unless empty
        return "OK"
    if code in (401, 403, 429, 999):  # login wall / bot block
        return "AMBIGUOUS"
    return "AMBIGUOUS"


def main():
    if not sys.stdin.isatty() and len(sys.argv) == 1:
        cand = json.load(sys.stdin)
    else:
        cand = {}
        for a in sys.argv[1:]:
            if "=" in a:
                k, v = a.split("=", 1)
                cand[k] = v
    out = {}
    for p, u in cand.items():
        if not u:
            continue
        st = verify(p, u)
        out[p] = {"url": u, "status": st, "ok": st == "OK"}
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
