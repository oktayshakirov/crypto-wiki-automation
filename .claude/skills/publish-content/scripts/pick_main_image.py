#!/usr/bin/env python3
"""Fetch main-image candidates from Pexels, resize to the site standard, and
stage them for the user to pick one.

Usage:
  python3 pick_main_image.py --query "layer 2 blockchain network" \
      --slug what-are-layer-2-blockchains --out <preview_dir> \
      [--width 800] [--count 3] [--page 1] [--orientation landscape]

Writes <out>/candidate_1.jpg .. candidate_N.jpg (resized JPEGs, each < 200 KB)
and prints a JSON manifest to stdout: [{n, file, kb, photographer, source_url}].
Re-roll with a higher --page to get different results for the same query.

Key: reads the Pexels API key from crypto-wiki-automation/.pexels-api-key
(gitignored). Get a free key at https://www.pexels.com/api/.
"""
import argparse, json, os, subprocess, sys, urllib.request, urllib.parse

KEY_PATH = "/Users/oktayshakirov/Coding/crypto-wiki-automation/.pexels-api-key"


def load_key():
    if not os.path.exists(KEY_PATH):
        sys.exit(f"ERROR: no Pexels key at {KEY_PATH}. Create it (gitignored) with a "
                 "free key from https://www.pexels.com/api/.")
    k = open(KEY_PATH).read().strip()
    if not k:
        sys.exit(f"ERROR: {KEY_PATH} is empty.")
    return k


def search(key, query, per_page, page, orientation):
    qs = urllib.parse.urlencode({
        "query": query, "per_page": per_page, "page": page,
        "orientation": orientation,
    })
    req = urllib.request.Request(
        "https://api.pexels.com/v1/search?" + qs,
        headers={"Authorization": key, "User-Agent": "publish-content/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode())


def download(url, dest):
    req = urllib.request.Request(url, headers={"User-Agent": "publish-content/1.0"})
    with urllib.request.urlopen(req, timeout=120) as r, open(dest, "wb") as f:
        f.write(r.read())


def resize_jpeg(src, dst, width):
    """Downscale to `width` (px) preserving aspect, re-encode JPEG, keep < 200 KB."""
    for quality in (80, 70, 60, 50, 40):
        subprocess.run(["sips", "--resampleWidth", str(width),
                        "-s", "format", "jpeg", "-s", "formatOptions", str(quality),
                        src, "--out", dst],
                       check=True, capture_output=True)
        if os.path.getsize(dst) <= 200 * 1024:
            return quality
    return quality  # smallest we tried; still emit it


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--query", required=True)
    ap.add_argument("--slug", required=True)
    ap.add_argument("--out", required=True, help="preview dir for candidates")
    ap.add_argument("--width", type=int, default=800)
    ap.add_argument("--count", type=int, default=3)
    ap.add_argument("--page", type=int, default=1)
    ap.add_argument("--orientation", default="landscape")
    a = ap.parse_args()

    key = load_key()
    os.makedirs(a.out, exist_ok=True)
    raw = os.path.join(a.out, "_raw")
    os.makedirs(raw, exist_ok=True)

    data = search(key, a.query, max(a.count * 3, 9), a.page, a.orientation)
    photos = data.get("photos", [])
    if not photos:
        sys.exit(f"No Pexels results for {a.query!r} (page {a.page}). Try another query.")

    manifest = []
    for i, p in enumerate(photos[:a.count], start=1):
        src_url = p["src"].get("large2x") or p["src"].get("large") or p["src"]["original"]
        tmp = os.path.join(raw, f"src_{i}.jpg")
        out = os.path.join(a.out, f"candidate_{i}.jpg")
        download(src_url, tmp)
        resize_jpeg(tmp, out, a.width)
        manifest.append({
            "n": i,
            "file": out,
            "kb": round(os.path.getsize(out) / 1024, 1),
            "photographer": p.get("photographer", ""),
            "source_url": p.get("url", ""),
            "alt": p.get("alt", ""),
        })
    print(json.dumps(manifest, indent=1))


if __name__ == "__main__":
    main()
