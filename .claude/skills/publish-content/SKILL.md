---
name: publish-content
description: Publish content to thecrypto.wiki or Tinnitus Help via the local n8n workflows - suggest topics, generate the article, quality-gate it, stage locally for review, then push (deploy-gated) and share to social media. Use when the user wants to create/publish/share a post, exchange review, or crypto OG bio.
---

# Publish Content

Full agent loop: **suggest topics → user picks → generate via n8n → quality gate → stage locally → user reviews + adds main image → push (deploy gate) → share → verify.**

## Prerequisites
- **n8n must be running** at `http://localhost:5678` (user starts it manually with `n8n`; it is NOT always on). If unreachable, ask the user to start it.
- Prefer the `mcp__n8n-local__*` MCP tools. If they're not loaded in this session, call the MCP endpoint directly with curl: POST `http://127.0.0.1:5678/mcp-server/http` (JSON-RPC `tools/call`), auth `Authorization: Bearer <token>` - read the token from the `n8n-local` server entry in `~/.claude.json`. Poll executions via REST: `http://127.0.0.1:5678/api/v1/executions/<id>?includeData=true` with header `X-N8N-API-KEY` from the gitignored `.n8n-api-key` at this repo root.
- `git pull` all relevant repos first: this repo + `../tinnitus-help-automation` + site repos `../crypto-wiki` / `../tinnitus-blog`.

## Workflow registry (Form Triggers; run with `inputs: {type:"form", formData:{...}}`)
| Site | Action | Workflow ID | formData |
|---|---|---|---|
| Crypto Wiki | New Post | `aPOOMzK1MuUcr6sM` | `{ topic }` |
| Crypto Wiki | New Exchange | `pEfGTfVz5FdtLTGM` | `{ name, website }` |
| Crypto Wiki | New Crypto OG | `MYaoP3c6N5qLFX3U` | `{ name }` |
| Crypto Wiki | Share Post | `LUkP4LjfcWefJZpJ` | `{ slug }` |
| Crypto Wiki | Share Exchange | `KYJga45bwixvg8DY` | `{ slug }` |
| Crypto Wiki | Share Crypto OG | `5dyD2hHUqfHCV8Rw` | `{ slug }` |
| Tinnitus | New Post | `pddxBAmv2k2nSBv2` | `{ topic }` |
| Tinnitus | Share Post | `jtUStrxCt23FGNDk` | `{ slug }` |
| Tinnitus | Share Sound | `UcubZDb1sKnszcZX` | `{ slug }` |

## Step 1 - Suggest 10 topics
Read `content-database.json` in the matching automation repo (crypto: `posts`/`exchanges`/`crypto_ogs`; tinnitus: `blog`/`zen`). Gap-analyze vs existing titles; use WebSearch for trends (CMC exchange rankings page is JS-rendered - WebSearch only). Present 10 options with a one-line "why" each. **The chosen topic becomes title AND slug verbatim - keep it short.**

## Step 2 - Generate
Execute the matching "New" workflow. GPT-5 takes 1-3 min (retryOnFail 3x is set); if the run still fails with ECONNRESET/ETIMEDOUT, just re-run. On success it commits the MDX + updates `content-database.json` in the automation repo.

## Step 3 - Quality gate (pull the automation repo, check the MDX)
Common: 1,200-2,500 words; 8-15 internal links, **bold** `**[Text](/path)**`, each page linked at most once, all slugs valid vs DB; exactly 2 body images **from the real archive** (never invented names); no em/en dashes or `--` (plain `-` only); no trailing metadata JSON (fenced or bare); ads never adjacent to images; no References section; author `Oktay Shakirov`.
Most violations are auto-fixed by the Build node now - if one slips through, fix the article AND add a deterministic fix to the workflow node + guidelines (backup to `.n8n-backups/` first; mutate the workflow dict in place; PUT only `name,nodes,connections,settings`).

Per-type conventions:
- **Crypto post**: starts `## Heading`; `<ArticleAd />`; images `![alt](/images/posts/x.jpg)`; main image ≠ body images; frontmatter `categories` (fixed list) + optional `crypto-ogs`/`exchanges` (Title Case) + `draft: false`; description 150-160 chars. Proactively link relevant existing crypto-OGs. Avoid brand-heavy/ad-like archive images.
- **Crypto OG**: `## **Bold Heading**`; quotes `> "..." - Name`; social block in frontmatter (verify links via WebSearch; drop unverified); no tags; ISO date + order. Fact-check recent events (GPT-5 may miss them, e.g. verdicts/sentencings).
- **Tinnitus post**: opens `<Blockquote>` → main `<Image>` → intro; `## <Highlighter>Heading</Highlighter>`; `<AdComponent />`; first body image = main image (`/images/{slug}.jpg` flat); 2-3 lowercase tags from fixed vocab; description 120-135 chars.

## Step 4 - Stage locally
Copy the MDX to the site repo (`crypto-wiki/content/{posts|exchanges|crypto-ogs}/` or `tinnitus-blog/content/posts/`) - do NOT commit. Ask the user to add the main image (<200 KB) at the exact frontmatter path and review (offer dev server). Fold their feedback into guidelines/workflow so the next run is right by default.

## Step 5 - Push (only on explicit approval)
Commit post + ALL new images (check `git status` for untracked images - a missing image ships a broken page) to the site repo, push. Then **DEPLOY GATE**: poll the production article URL AND main-image URL (follow redirects; both sites 301 to www) until both return 200. Never share before this passes - the banner generator fetches the main image from production (black-spot banner otherwise).

## Step 6 - Share (only on explicit approval - posts publicly)
Before running: confirm the share image doesn't already exist in the automation repo (`images/posts/<slug>.png` or `images/crypto-ogs/<slug>.png` via GitHub API; if present from a previous run, `git rm` + push first - the Upload node is create-only and fails with "sha wasn't supplied").
Run the matching Share workflow. It posts to Telegram (binary upload), Instagram + Facebook (Twitter nodes are intentionally disconnected - no X API). Verify: every node success; Telegram result has a `photo` array; download the run's APITemplate `download_url_png` and view it to confirm the banner rendered (title + photo, no black spot).
**Single-channel re-share**: temporarily remove the other channel targets from `Format Social Post`'s connections, run, then restore.

## Safety
- Never push or share without the user's explicit go for that step.
- Secrets: `.n8n-api-key` (REST) and the MCP bearer token (in `~/.claude.json`) - never commit or echo them.
- Workflow edits: backup JSON to `.n8n-backups/` first; verify the PUT response.
