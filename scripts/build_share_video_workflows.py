#!/usr/bin/env python3
"""Build the two "Share Video" n8n workflows from one definition.

There is a Share Video workflow per site and they differ by **five values** —
credentials, Instagram user id, Telegram channel, site name and the default
call to action. Nothing structural. Writing them as two hand-maintained JSON
files is how the two Share Post workflows ended up with a `sendPhoto` on one
site and a different `file` binding on the other, so this generates both from
`SITES` below and posts them over the REST API.

    python3 scripts/build_share_video_workflows.py            # dry run, prints
    python3 scripts/build_share_video_workflows.py --apply    # create/update

**What it posts, and what it deliberately does not.** The brief is the YouTube
link plus a short call to action, so there is no banner to render: Facebook and
Telegram both unfurl a YouTube URL into a player card by themselves, which is a
better object than a still image because it is clickable. That removes the
APITemplate render, the GitHub image upload and the 30-second CDN wait that the
Share Post workflows need — this one has no image pipeline at all.

**The title is fetched, not typed.** `https://www.youtube.com/oembed` returns
the live title and needs no credential and no API key, so the caption always
matches whatever the video is actually called at the moment it is shared. It
works on unlisted videos too, which is what makes a dry run possible before a
video goes public.

**There is no Instagram branch, and that is settled.** A story was built and
did publish — the permission is there and `media_type=STORIES` works — but
**link stickers cannot be set through the Graph API at all**. That is a
platform limitation, not a scope we are missing, so the best an automated
story can ever be is a picture with no way to act on it: no tap target, no
swipe, just "go and find it". The user saw one and cut it. Do not add it back
without a way to make it clickable.
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
import uuid
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
N8N = "http://localhost:5678/api/v1"

# The n8n public API rejects a PUT carrying `settings.binaryMode`, so the
# allow-list is the safe shape rather than whatever the live workflow returns.
SETTINGS = {"executionOrder": "v1", "callerPolicy": "workflowsFromSameOwner",
            "availableInMCP": True}

SITES = {
    "crypto": {
        "name": "Crypto Wiki: Share Video",
        "snapshot": REPO / "share_video.json",
        "fb_cred": {"id": "CGGakNGphccGvIDc", "name": "Facebook Graph (CryptoWiki)"},
        "tg_cred": {"id": "geWva7g9QuODXuET", "name": "Telegram (CryptoWiki)"},
        "ig_user": "17841477190733041",
        "tg_chat": "@thecryptowiki",
        "site": "thecrypto.wiki",
        "lead": "New video about",
        "bare": "New video is up on YouTube",
    },
    "tinnitus": {
        "name": "Tinnitus Help: Share Video",
        "snapshot": (REPO.parent / "tinnitus-help-automation" / "share_video.json"),
        "fb_cred": {"id": "Ydx1TfHeHlMX2ILQ", "name": "Facebook Graph (TinnitusHelp)"},
        "tg_cred": {"id": "wvvr0VqigaV0y9Pc", "name": "Telegram (TinnitusHelp)"},
        "ig_user": "17841477062009382",
        "tg_chat": "@tinnitushelpme",
        "site": "tinnitushelp.me",
        "lead": "New video about",
        "bare": "New video is up on YouTube",
    },
}

# Accepts a bare id or any YouTube URL shape, because the user will paste
# whichever is in the clipboard. Eleven characters is the id format and
# validating it here turns a silent no-op into a named failure.
# Accepts a bare id or any YouTube URL shape, because the user will paste
# whichever is in the clipboard. Eleven characters is the id format and
# validating it here turns a silent no-op into a named failure.
NORMALISE = """
const raw = String($json.videoId ?? $json['field-0'] ?? '').trim();
const m = raw.match(/(?:v=|youtu\\.be\\/|shorts\\/|embed\\/|live\\/)([A-Za-z0-9_-]{11})/);
const id = m ? m[1] : raw;
if (!/^[A-Za-z0-9_-]{11}$/.test(id)) {
  throw new Error(`Not a YouTube video id or URL: ${raw || '(empty)'}`);
}
return [{ json: {
  videoId: id,
  url: `https://www.youtube.com/watch?v=${id}`,
  topic: String($json.topic ?? $json['field-1'] ?? '').trim(),
} }];
"""

FORMAT = """
const info = $json;                       // the oEmbed response
const v = $('Normalise Input').item.json;
const title = (info.title || '').trim();

// **Do not put the title in the caption.** Facebook and Telegram both unfurl
// the URL into a card that already carries the title, the description and the
// thumbnail, so repeating it prints the same sentence twice in one post. The
// caption's only job is the human line the card cannot supply.
//
// The subject is typed into the `topic` field. Failing that it is guessed from
// a `Subject: hook` or `hook | Subject` title, which is this channel's habit
// and not a rule — "Does Tinnitus Go Away? Temporary vs Chronic" has no
// subject to find, so the generic line is the third branch rather than an
// error. Guessing is a convenience; typing two words is the reliable path.
let topic = v.topic;
if (!topic) {
  const colon = title.match(/^([^:]{3,40}):\\s/);
  const pipe = title.match(/\\|\\s*(.{3,40})$/);
  topic = (colon && colon[1].trim()) || (pipe && pipe[1].trim()) || '';
}

const message = topic
  ? `%(lead)s ${topic} 👇`
  : `%(bare)s 👇`;

return [{ json: {
  videoId: v.videoId,
  url: v.url,
  title,
  topic,
  message,
  facebook: message,
  telegram: `${message}\\n${v.url}`,
} }];
"""


def nid(site: str, name: str) -> str:
    """A stable UUID per (site, node).

    **Node ids must be real UUIDs and must not repeat across workflows.** The
    first cut used a slug of the node name, so both sites' Form Triggers shared
    the id `form-trigger` — n8n accepted the workflow, served the form page and
    answered a submission with `{"status":200}`, and then ran nothing at all.
    Deriving them from a namespace keeps them unique across sites while staying
    stable across re-runs, so an update does not orphan the webhook.
    """
    return str(uuid.uuid5(uuid.NAMESPACE_URL,
                          f"n8n/share-video/{site}/{name}"))


def node(name, type_, tv, params, pos, creds=None, extra=None, site=""):
    n = {"parameters": params, "id": nid(site, name),
         "name": name, "type": type_, "typeVersion": tv, "position": pos}
    if creds:
        n["credentials"] = creds
    if extra:
        n.update(extra)
    return n


def build(cfg: dict, site: str, channels=("facebook", "telegram")) -> dict:
    n = lambda *a, **k: node(*a, site=site, **k)
    nodes = [
        n("Form Trigger", "n8n-nodes-base.formTrigger", 2.2, {
            "formTitle": cfg["name"],
            "formDescription": "YouTube video id or URL, plus an optional topic (the subject of the video, two or three words).",
            "formFields": {"values": [
                {"fieldLabel": "videoId", "requiredField": True},
                {"fieldLabel": "topic", "requiredField": False},
            ]},
            "options": {},
        }, [-260, 0], extra={"webhookId": nid(site, "form-webhook")}),

        n("Normalise Input", "n8n-nodes-base.code", 1,
             {"jsCode": NORMALISE.strip() + "\n"}, [-40, 0]),

        # No credential, no API key, no quota. Also works on unlisted videos,
        # which is what lets this be rehearsed before a video goes public.
        n("Fetch Video Info", "n8n-nodes-base.httpRequest", 4.2, {
            "url": "=https://www.youtube.com/oembed?url={{ encodeURIComponent($json.url) }}&format=json",
            "options": {},
        }, [180, 0]),

        n("Format Video Post", "n8n-nodes-base.code", 1,
             {"jsCode": (FORMAT % {"lead": cfg["lead"], "bare": cfg["bare"]}).strip() + "\n"}, [400, 0]),

        n("Facebook Post", "n8n-nodes-base.facebookGraphApi", 1, {
            "httpRequestMethod": "POST", "graphApiVersion": "v23.0",
            "node": "me", "edge": "feed",
            "options": {"queryParameters": {"parameter": [
                {"name": "message", "value": "={{ $json.facebook }}"},
                {"name": "link", "value": "={{ $json.url }}"},
            ]}},
        }, [640, -180], {"facebookGraphApi": cfg["fb_cred"]}),

        # sendMessage, not sendPhoto: Telegram renders the YouTube URL as a
        # playable card, and a still photo would replace that with something
        # nobody can click.
        # **Both of these must be set explicitly; the node's defaults are wrong
        # for a channel post.** `appendAttribution` defaults to true and tacks
        # "This message was sent automatically with n8n" onto the end, and the
        # node sends `disable_web_page_preview` true, which is why the first
        # run showed a bare URL and no player card — Telegram reported it back
        # as `link_preview_options: {is_disabled: true}`. The preview *is* the
        # post here, so turning it off defeats the whole design.
        n("Telegram Post", "n8n-nodes-base.telegram", 1.2, {
            "chatId": cfg["tg_chat"],
            "text": "={{ $json.telegram }}",
            "additionalFields": {
                "appendAttribution": False,
                "disable_web_page_preview": False,
            },
        }, [640, 0], {"telegramApi": cfg["tg_cred"]}),

    ]

    fan_out = [{"node": t, "type": "main", "index": 0}
               for t in ("Facebook Post", "Telegram Post")
               if t.split()[0].lower() in channels]
    if not fan_out:
        raise SystemExit(f"no channels selected from {channels}")

    conn = {
        "Form Trigger": {"main": [[{"node": "Normalise Input", "type": "main", "index": 0}]]},
        "Normalise Input": {"main": [[{"node": "Fetch Video Info", "type": "main", "index": 0}]]},
        "Fetch Video Info": {"main": [[{"node": "Format Video Post", "type": "main", "index": 0}]]},
        "Format Video Post": {"main": [fan_out]},
    }
    return {"name": cfg["name"], "nodes": nodes, "connections": conn,
            "settings": SETTINGS}


def api(method: str, path: str, key: str, body: dict | None = None) -> dict:
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(f"{N8N}{path}", data=data, method=method,
                                 headers={"X-N8N-API-KEY": key,
                                          "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read() or "{}")
    except urllib.error.HTTPError as e:
        raise SystemExit(f"{method} {path} -> {e.code}: {e.read().decode()[:500]}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--site", choices=list(SITES) + ["both"], default="both")
    # Re-posting one channel without spamming the other is a real need — a
    # message gets deleted and re-sent far more often than a whole share is
    # redone. The `publish-content` skill documents doing this by editing the
    # live connections by hand and restoring them afterwards, which is a step
    # that gets forgotten. This makes it a flag, and `--no-snapshot` keeps a
    # deliberately partial build out of the committed JSON.
    ap.add_argument("--channels", default="facebook,telegram",
                    help="comma-separated: facebook,telegram")
    ap.add_argument("--no-snapshot", action="store_true")
    args = ap.parse_args()

    channels = tuple(c.strip().lower() for c in args.channels.split(",") if c.strip())
    key = (REPO / ".n8n-api-key").read_text().strip()
    existing = {w["name"]: w["id"]
                for w in api("GET", "/workflows?limit=250", key)["data"]}

    for site in (list(SITES) if args.site == "both" else [args.site]):
        cfg = SITES[site]
        wf = build(cfg, site, channels)
        wid = existing.get(cfg["name"])
        print(f"{cfg['name']}: {len(wf['nodes'])} nodes, "
              f"channels={','.join(channels)}, "
              f"{'update ' + wid if wid else 'create'}")
        if not args.apply:
            continue
        if wid:
            got = api("PUT", f"/workflows/{wid}", key, wf)
        else:
            got = api("POST", "/workflows", key, wf)
            wid = got["id"]
        api("POST", f"/workflows/{wid}/activate", key)
        # The committed snapshot is what survives an n8n reset.
        if args.no_snapshot:
            print("  -> snapshot skipped (partial build)")
            continue
        cfg["snapshot"].write_text(json.dumps(
            {"name": wf["name"], "nodes": wf["nodes"],
             "connections": wf["connections"], "settings": wf["settings"]},
            indent=2) + "\n")
        print(f"  -> {wid}, activated, snapshot {cfg['snapshot']}")


if __name__ == "__main__":
    sys.exit(main())
