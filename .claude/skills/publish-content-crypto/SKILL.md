---
name: publish-content-crypto
description: Publish content to thecrypto.wiki via the local n8n workflows - suggest topics, generate the article, quality-gate it, stage locally for review, then push (deploy-gated) and share to social media. Use when the user wants to create/publish/share a crypto post, exchange review, or crypto OG bio. For Tinnitus Help use publish-content-tinnitus instead.
---

# Publish Content — Crypto Wiki

Full agent loop: **suggest topics → user picks → generate via n8n → quality gate → stage locally → fetch main-image candidates (user picks) → user reviews → push (deploy gate) → share → verify.**

This skill covers **thecrypto.wiki only**. For tinnitushelp.me, use `publish-content-tinnitus` in `tinnitus-help-automation` — it is a separate copy, not a shared script, so a fix here does not apply there automatically.

**Repo paths (absolute; this skill works from any directory):** automation repo `/Users/oktayshakirov/Coding/crypto-wiki-automation`; site (production) repo `/Users/oktayshakirov/Coding/crypto-wiki`. The `.n8n-api-key`, `.n8n-backups/`, and workflow-editing all live in `crypto-wiki-automation`.

**Production URLs (do NOT guess these - a wrong host returns curl `000` forever and looks exactly like a slow deploy):**

| Domain | Article URL | Main image URL |
|---|---|---|
| `https://www.thecrypto.wiki` | `/posts/<slug>`, `/exchanges/<slug>`, `/crypto-ogs/<slug>` | `/images/posts/<slug>.jpg` |

301s to `www`, so always `curl -L`. A `000` status is DNS/connection failure, not a pending deploy - re-check the host before continuing to poll.

**Where this skill lives / cross-device:** the real files are versioned in the `crypto-wiki-automation` repo at `.claude/skills/publish-content-crypto/`; `~/.claude/skills/publish-content-crypto` is a **symlink** into it, which is how Claude Code discovers the skill. So edits to `SKILL.md` or `scripts/` are committed like any repo change (backup workflow JSON to `.n8n-backups/` still applies for workflow edits, but the skill files themselves just commit). **To set up a new device:** clone `crypto-wiki-automation`, then `ln -s <repo>/.claude/skills/publish-content-crypto ~/.claude/skills/publish-content-crypto`, and recreate the two gitignored secrets locally (`.n8n-api-key`, `.pexels-api-key`).

## Prerequisites
- **n8n must be running** at `http://localhost:5678` (user starts it manually with `n8n`; it is NOT always on). If unreachable, ask the user to start it.
- Prefer the `mcp__n8n-local__*` MCP tools. If they're not loaded in this session, call the MCP endpoint directly with curl: POST `http://127.0.0.1:5678/mcp-server/http` (JSON-RPC `tools/call`), auth `Authorization: Bearer <token>` - read the token from the `n8n-local` server entry in `~/.claude.json`. Poll executions via REST: `http://127.0.0.1:5678/api/v1/executions/<id>?includeData=true` with header `X-N8N-API-KEY` from the gitignored `/Users/oktayshakirov/Coding/crypto-wiki-automation/.n8n-api-key`.
- **Triggering a Form Trigger without the MCP tools** (reading the MCP bearer token out of `~/.claude.json` may be blocked by the permission classifier): fetch the workflow over REST, read the form trigger's `webhookId`, and POST to `http://127.0.0.1:5678/form/<webhookId>`. Two non-obvious requirements, both of which fail *quietly*:
  - It must be **`multipart/form-data`** (`curl -F`, not `--data-urlencode`). Form-encoded returns HTTP 500 `Workflow could not be started!`, and the real reason (`Expected multipart/form-data`) only shows up in the execution record.
  - Fields are named **`field-0`, `field-1`, ... by index**, NOT by field label. `-F "topic=..."` returns **HTTP 200** and the trigger emits `topic: null`; the AI then invents an unrelated topic and the run looks completely normal. A `New Post` run triggered with `topic=` produced a full, gate-passing article about crypto wallets. **Always confirm the Form Trigger node's output actually carries your topic/slug before trusting a run.**
- **Polling gotcha:** `GET /api/v1/executions` **excludes running executions by default**, so right after a trigger the newest entry is the previous run - easy to misread as "my run failed." Use `?status=running` to find the new id, then poll `/executions/<id>` directly.
- `git pull` both relevant repos first: `crypto-wiki-automation` and `crypto-wiki`. Use `git pull --autostash` - the automation repo often carries uncommitted skill edits, which make a plain rebase pull abort.
- **Main-image fetch (Step 4)** needs a free Pexels key at `crypto-wiki-automation/.pexels-api-key` (gitignored, shared with the tinnitus skill's copy of this key). If missing, ask the user to create it from `https://www.pexels.com/api/`. Only `sips` + `cwebp` are available locally (no ImageMagick); `sips` does the resize/JPEG re-encode.
- Workflow-edit gotcha: the n8n public-API PUT rejects `settings.binaryMode`; filter `settings` to allowed keys (executionOrder, callerPolicy, availableInMCP, ...) or the PUT 400s.

## Workflow registry (Form Triggers; run with `inputs: {type:"form", formData:{...}}`)
| Action | Workflow ID | formData |
|---|---|---|
| New Post | `aPOOMzK1MuUcr6sM` | `{ topic }` |
| New Exchange | `pEfGTfVz5FdtLTGM` | `{ name, website }` |
| New Crypto OG | `MYaoP3c6N5qLFX3U` | `{ name }` |
| Share Post | `LUkP4LjfcWefJZpJ` | `{ slug }` |
| Share Exchange | `KYJga45bwixvg8DY` | `{ slug }` |
| Share Crypto OG | `5dyD2hHUqfHCV8Rw` | `{ slug }` |
| Publish Reel | `uIV6956N14pMGMZ5` | `{ videoUrl, coverUrl, caption, durationSeconds }` |
| Publish Facebook Video | `zS3xX6tbXpXnF32N` | `{ videoUrl, title, description, thumbUrl }` |

**Publish Reel** is driven by the `publish-video` skill, not by this one. It posts one
vertical video as an Instagram Reel and a Facebook Reel; `videoUrl` and `coverUrl` must
be publicly reachable for the length of the run (the skill opens a cloudflared quick
tunnel over the render folder). Facebook Reels accepts 3 to 90 seconds only, which is
why `durationSeconds` is required and checked before anything uploads.

**Publish Facebook Video** posts a long-form video natively to the Page feed - not a
Reel, no duration cap, `POST /me/videos` with `file_url` rather than the three-phase
Reels upload. Built 2026-08-20 to test whether native video earns more organic reach
than posting a YouTube link; all four existing crypto long-form videos went out this
way as the first test - see CHANGELOG for the results once there is data. **It replaced
the Share Video workflow**, which posted a YouTube URL to Facebook and Telegram and let
them unfurl it into a card. It was deleted on 2026-08-20 - a link post sends the
viewer to YouTube and earns the reach an outbound link earns, which is the thing native
upload exists to avoid. The last JSON is in `.n8n-backups/*.before-delete.json` -
**local only**, since `.n8n-backups/` is gitignored, so that safety net does not survive
a fresh clone. Pulls `title`/`description` straight from `youtube-audit video <id>`
rather than writing Facebook-native copy, since the source videos are already public on
YouTube.

**Pass the full YouTube description; the workflow trims it.** `Normalise Input` keeps
the first paragraph and the line carrying the article link, and drops the rest - the
second summary, the chapter list, and the repeat of the same URL at the bottom. A whole
YouTube description under a Facebook video buries the one line a reader acts on and
prints the URL twice. The trim lives in the workflow rather than at the caller so it
cannot be forgotten. It carries the link's own line **verbatim** rather than relabelling
it: the workflow expects a line like `Full article: <url>`.

**If the source folder has no thumbnails, pull each video's `maxresdefault.jpg` from
YouTube** rather than rendering new ones - that is the poster already live on the
channel, so the Facebook cover matches. **Match files to YouTube videos by duration,
not by title**: filenames drift from published titles.

**The `FB Reel Upload` node posts to `rupload.facebook.com`, not `graph.facebook.com`.**
Meta documents its auth as an `Authorization: OAuth <token>` header; the node instead
uses the existing Facebook Graph credential as a *predefined credential type*, which
n8n injects as `?access_token=` on the query string. **Verified working on 2026-08-20** -
rupload accepts the query string as well as the header, so no Header Auth credential is
needed. If it ever starts 401ing, that is the first thing to suspect and a Header Auth
credential (`Authorization` = `OAuth <page token>`) on that one node is the fix.

## Step 1 - Suggest 10 topics
Read `content-database.json` in `crypto-wiki-automation` (`posts`/`exchanges`/`crypto_ogs`). Gap-analyze vs existing titles; use WebSearch for trends (CMC exchange rankings page is JS-rendered - WebSearch only). Present 10 options with a one-line "why" each. **The chosen topic becomes title AND slug verbatim - keep it short.**

## Step 2 - Generate
Execute the matching "New" workflow. GPT-5 takes 1-3 min (retryOnFail 3x is set); if the run still fails with ECONNRESET/ETIMEDOUT, just re-run. On success it commits the MDX + updates `content-database.json` in the automation repo.

## Step 3 - Quality gate (pull the automation repo, check the MDX)
**Run the automated gate first:** `python3 scripts/quality_gate.py <path-to.mdx>` (script dir is this skill's folder). It checks all of the below deterministically and exits non-zero on any hard FAIL - fix those, re-run, then eyeball anything a script can't judge (image relevance, factual/date accuracy, link *aptness*).

It resolves the DB + image archive itself and infers the type from the path (`/exchanges/` -> exchange, `/crypto-ogs/` -> og, else post). Override with `--db` / `--archive` / `--type`, but the bare one-argument call is normally right. It echoes the resolved `type` as its first line - **check that line**.

Known non-issues it deliberately tolerates: markdown table separator rows (`| --- |`) are stripped before the dash check, `#anchor`/`?query` links validate against the base page, and link targets are checked against the DB **union the MDX actually on disk** (the DB can drift and miss live posts).

Checks: 1,200-2,500 words; 8-15 internal links, **bold** `**[Text](/path)**`, each page linked at most once, all slugs valid vs DB; exactly 2 body images **from the real archive** (never invented names) and **not repeated in posts published close together** - reusing an archive image across the site is fine and expected; what matters is that someone reading a few recent posts back to back never sees the same picture twice. The gate warns when a body image also appears in any of the 5 most recent other posts by frontmatter date (`--recent-window`). On a warning, swap in a different archive file, or fetch a new one with `pick_main_image.py`; no em/en dashes or `--` (plain `-` only); **no curly quotes** (`'`/`'`/`"`/`"` -> straight; applies to body AND the frontmatter description); no trailing metadata JSON (fenced or bare); ads never adjacent to images; no References section; author `Oktay Shakirov`.
Most violations are auto-fixed by the Build node now - if one slips through, fix the article AND add a deterministic fix to the workflow node + guidelines (backup to `.n8n-backups/` first; mutate the workflow dict in place; PUT only `name,nodes,connections,settings`).
**Persisting workflow fixes:** live n8n edits only survive in the gitignored `.n8n-backups/`. When a fix is **important/major** (fixes a broken workflow, changes a contract, or prevents a defect on every future run), also sync the live workflow into the repo's committed JSON snapshot (`crypto-wiki-automation/{new_post,share_post,...}.json`) and commit, so it survives an n8n reset - minor tweaks can stay live-only. Known deterministic fix already committed: Share `Set Slug` reads `={{ $json.slug }}` (was hardcoded, shared the wrong post). Live-only (not yet in committed JSON): New Post Build node curly-quote normalization.

Per-type conventions:
- **Post**: starts `## Heading`; `<ArticleAd />`; images `![alt](/images/posts/x.jpg)`; main image ≠ body images; frontmatter `categories` (fixed list) + optional `crypto-ogs`/`exchanges` (Title Case) + `draft: false`; description 150-160 chars. Proactively link relevant existing crypto-OGs. Avoid brand-heavy/ad-like archive images. **Every name in `crypto-ogs`/`exchanges` must actually be linked in the body** - the AI tends to list OGs it never mentions (the gate now fails on this); either add a real mention+link or drop the name. If you trim a body link, drop the matching frontmatter entry too.
- **Exchange**: `## Heading` (recent pages are plain, older ones bold - either passes); `<ArticleAd />`; body images `![alt](/images/posts/x.jpg)` from the archive; main image is a **brand logo** at `/images/exchanges/<slug>.png` (~16:9, 600-1200px wide, <100 KB) that the user supplies by hand - never Pexels. Frontmatter needs `title, image, description, date, updated, order, authors, quickFacts, faqs, social` - **`quickFacts` and `faqs` are mandatory** (both render in `layouts/ExchangeSingle.js`, and `faqs` feeds the `faqSchema()` JSON-LD, so omitting it silently costs the FAQ rich result; the AI leaves both out). description **90-125 chars** - the exchange card is a fixed tile and past ~125 chars it wraps to a 5th row and looks off next to the rest of the grid. `social` keys are limited to what `layouts/components/Social.js` destructures (website, twitter, discord, github, telegram, apple, android, facebook, instagram, linkedin, youtube, reddit, medium, wikipedia, ...) - anything else, e.g. `docs`, is silently dropped. Verify each social URL via WebSearch and drop unverified ones. **Always add `apple` and `android` links when the exchange ships mobile apps** - nearly all of them do, and the AI omits them or invents plausible-looking fakes (it guessed `apps.apple.com/app/asterdex` and `id=com.asterdex`, both nonexistent). Find the real listings via WebSearch or the exchange's own site/X account, then **confirm the developer name on the listing matches the exchange** (Aster's Play listing is developer "Aster DEX" / contact@asterdex.com) - store search is full of copycat wallet apps. `curl -sL -o /dev/null -w '%{http_code}'` both URLs before committing. Apple storefronts are per-country and a listing missing from one 404s there while working elsewhere, so if `/us/` 404s try `gb`, `de`, `ch`, `ee` and use one that returns 200 (Aster is not in the US/UK/DE stores; the page uses `ch`). Play Store URLs are global - no `hl=` needed. Fact-check the protocol/company specifics: GPT-5 tends to emit a generic exchange template with the name swapped in, so confirm founders, launch year, native token, architecture, and any major incident actually made it into the body.
- **Crypto OG**: `## **Bold Heading**`; quotes `> "..." - Name`; social block in frontmatter (verify links via WebSearch; drop unverified); no tags; ISO date + order; description 90-125 chars (same card grid as exchanges). Fact-check recent events (GPT-5 may miss them, e.g. verdicts/sentencings).

## Step 4 - Stage locally + pick the main image
Copy the MDX to `crypto-wiki/content/{posts|exchanges|crypto-ogs}/` - do NOT commit.

**Main image (posts only - auto-fetched from Pexels).** Skip for crypto-OGs and exchanges - those need a specific person's photo or a brand logo, which stock search can't supply; ask the user to drop those in manually at the frontmatter path (OGs are 500px PNGs, ~500px wide).

Flow for a post:
1. Derive a concrete visual search query from the topic (e.g. `What Are Layer 2 Blockchains` -> `blockchain network technology abstract`; avoid brand-heavy/ad-like results). Aim for an editorial, aesthetically strong photo, not a clinical or literal one. Add a demographic word when the topic is adult-facing (`adult`, `mature man`, `woman`) - a bare query like `person covering ear` returns almost entirely children and teenagers.
2. Run `scripts/pick_main_image.py --query "<query>" --slug <slug> --out <scratchpad>/imgpick --archive crypto-wiki/public/images/posts [--width 800]` (script dir is this skill's folder; default width 800 for posts). It downloads candidates, resizes to the standard width, re-encodes JPEG < 200 KB, and prints a JSON manifest (file path, KB, photographer, Pexels URL).
   **Always pass `--archive`.** Pexels re-serves its popular stock constantly, so candidates are frequently a photo already published under another slug - the script aHashes each candidate against the archive, drops anything within `--dup-threshold` (default 6), backfills a replacement, and reports what it rejected on stderr.
3. `open` the `candidate_*.jpg` AND send them with `SendUserFile` (`display: "render"`) so they appear inline in chat, then ask which to use. Offer a re-roll (`--page 2`, or a new `--query`); expect to need 2-3 rounds before one lands, and vary the *direction* between rounds rather than just re-running the same query.
4. On pick, copy the chosen candidate to `crypto-wiki/public/images/posts/<slug>.jpg` and delete the preview dirs. The main image is frontmatter-only and has no alt text, so there is nothing to rewrite there - instead `Read` both **body** images and check their alts, which are written blind against an imagined image (a real case: `futuristic-ui.jpg`, a person at a laptop with data overlays, was captioned "an AI agent approving and signing a crypto transaction").

   If the user supplies a specific Pexels photo URL instead of picking a candidate, pull it by id via `GET https://api.pexels.com/v1/photos/<id>` (auth header is the bare key), download `src.original` with `?w=1600`, then `sips -Z 800` + JPEG re-encode. Still dup-check it against the archive - `pick_main_image.ahash` / `archive_hashes` are importable for exactly this. Pexels needs no attribution, but the manifest keeps the photographer/URL if the user ever wants to credit.

Site standards: posts ~800px wide JPG (existing archive is 800-900px, ~70 KB); crypto-OGs 500px. The script already keeps every candidate < 200 KB.

Then let the user review (offer dev server). Fold their feedback into guidelines/workflow so the next run is right by default.

## Step 5 - Push (only on explicit approval)
Commit post + ALL new images (check `git status` for untracked images - a missing image ships a broken page) to `crypto-wiki`, push. Then **DEPLOY GATE**: poll the production article URL AND main-image URL until both return 200, using the exact hosts + path shapes from the **Production URLs** table at the top of this skill (`curl -sL`). If the first poll returns `000`, stop and fix the URL - that is a bad host, not a slow deploy. Never share before this passes - the banner generator fetches the main image from production (black-spot banner otherwise).

### Step 5b - Push notification (automatic)
**Nothing to run.** The push to main triggers `.github/workflows/notify-new-content.yml`, which waits for the deployment to go live and then syncs to Firestore, which sends the notification. Check the repo's Actions tab to confirm the run went green - it takes a few minutes because it waits on the deploy.

If the run failed or timed out, re-run it from the Actions tab, or send it by hand from the site repo with `npm run sync-content`. Never move the sync into `npm run build` - it used to live there, which is exactly why taps in the first ~15s hit a 404.

## Step 6 - Share (only on explicit approval - posts publicly)
Before running: confirm the share image doesn't already exist in the automation repo (`images/posts/<slug>.png` or `images/crypto-ogs/<slug>.png` via GitHub API; if present from a previous run, `git rm` + push first - the Upload node is create-only and fails with "sha wasn't supplied").
Run the matching Share workflow. It posts to Telegram (binary upload), Instagram + Facebook (Twitter nodes are intentionally disconnected - no X API). Verify: every node success; Telegram result has a `photo` array (**nested at `result.photo`, not top-level** - checking the top level looks like a failure on a perfectly good run); Facebook/Instagram outputs each carry an `id`; download the run's APITemplate `download_url_png` and view it to confirm the banner rendered (title + photo, no black spot).
**Single-channel re-share**: temporarily remove the other channel targets from `Format Social Post`'s connections, run, then restore.

## Safety
- Never push or share without the user's explicit go for that step.
- Secrets: `.n8n-api-key` (REST), `.pexels-api-key` (Step 4 images), and the MCP bearer token (in `~/.claude.json`) - never commit or echo them.
- Workflow edits: backup JSON to `.n8n-backups/` first; verify the PUT response.
