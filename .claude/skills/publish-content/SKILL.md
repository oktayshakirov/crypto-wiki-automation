---
name: publish-content
description: Publish content to thecrypto.wiki or Tinnitus Help via the local n8n workflows - suggest topics, generate the article, quality-gate it, stage locally for review, then push (deploy-gated) and share to social media. Use when the user wants to create/publish/share a post, exchange review, or crypto OG bio.
---

# Publish Content

Full agent loop: **suggest topics → user picks → generate via n8n → quality gate → stage locally → fetch main-image candidates (user picks) → user reviews → push (deploy gate) → share → verify.**

**Repo paths (absolute; this skill works from any directory):** automation repos `/Users/oktayshakirov/Coding/crypto-wiki-automation` and `/Users/oktayshakirov/Coding/tinnitus-help-automation`; site (production) repos `/Users/oktayshakirov/Coding/crypto-wiki` and `/Users/oktayshakirov/Coding/tinnitus-blog`. The `.n8n-api-key`, `.n8n-backups/`, and workflow-editing all live in `crypto-wiki-automation`.

**Where this skill lives / cross-device:** the real files are versioned in the `crypto-wiki-automation` repo at `.claude/skills/publish-content/`; `~/.claude/skills/publish-content` is a **symlink** into it, which is how Claude Code discovers the skill. So edits to `SKILL.md` or `scripts/` are committed like any repo change (backup workflow JSON to `.n8n-backups/` still applies for workflow edits, but the skill files themselves just commit). **To set up a new device:** clone `crypto-wiki-automation`, then `ln -s <repo>/.claude/skills/publish-content ~/.claude/skills/publish-content`, and recreate the two gitignored secrets locally (`.n8n-api-key`, `.pexels-api-key`).

## Prerequisites
- **n8n must be running** at `http://localhost:5678` (user starts it manually with `n8n`; it is NOT always on). If unreachable, ask the user to start it.
- Prefer the `mcp__n8n-local__*` MCP tools. If they're not loaded in this session, call the MCP endpoint directly with curl: POST `http://127.0.0.1:5678/mcp-server/http` (JSON-RPC `tools/call`), auth `Authorization: Bearer <token>` - read the token from the `n8n-local` server entry in `~/.claude.json`. Poll executions via REST: `http://127.0.0.1:5678/api/v1/executions/<id>?includeData=true` with header `X-N8N-API-KEY` from the gitignored `/Users/oktayshakirov/Coding/crypto-wiki-automation/.n8n-api-key`.
- `git pull` all relevant repos first (all under `/Users/oktayshakirov/Coding/`): the two automation repos + the two site repos.
- **Main-image fetch (Step 4)** needs a free Pexels key at `crypto-wiki-automation/.pexels-api-key` (gitignored). If missing, ask the user to create it from `https://www.pexels.com/api/`. Only `sips` + `cwebp` are available locally (no ImageMagick); `sips` does the resize/JPEG re-encode.
- Workflow-edit gotcha: the n8n public-API PUT rejects `settings.binaryMode`; filter `settings` to allowed keys (executionOrder, callerPolicy, availableInMCP, ...) or the PUT 400s.

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
**Run the automated gate first:** `python3 scripts/quality_gate.py <path-to.mdx>` (script dir is this skill's folder; defaults resolve the DB + site image archive). It checks all of the below deterministically and exits non-zero on any hard FAIL - fix those, re-run, then eyeball anything a script can't judge (image relevance, factual/date accuracy, link *aptness*). The gate currently encodes the crypto **post** checklist; for OGs/exchanges/tinnitus still verify by hand against the per-type conventions.
Common: 1,200-2,500 words; 8-15 internal links, **bold** `**[Text](/path)**`, each page linked at most once, all slugs valid vs DB; exactly 2 body images **from the real archive** (never invented names); no em/en dashes or `--` (plain `-` only); **no curly quotes** (`'`/`'`/`"`/`"` -> straight; applies to body AND the frontmatter description); no trailing metadata JSON (fenced or bare); ads never adjacent to images; no References section; author `Oktay Shakirov`.
Most violations are auto-fixed by the Build node now - if one slips through, fix the article AND add a deterministic fix to the workflow node + guidelines (backup to `.n8n-backups/` first; mutate the workflow dict in place; PUT only `name,nodes,connections,settings`).
**Persisting workflow fixes:** live n8n edits only survive in the gitignored `.n8n-backups/`. When a fix is **important/major** (fixes a broken workflow, changes a contract, or prevents a defect on every future run), also sync the live workflow into the repo's committed JSON snapshot (`crypto-wiki-automation/{new_post,share_post,...}.json`, `tinnitus-help-automation/{new_post,share_post,share_sound}.json`) and commit, so it survives an n8n reset - minor tweaks can stay live-only. Known deterministic fixes already committed: crypto Share `Set Slug` reads `={{ $json.slug }}` (was hardcoded, shared the wrong post); tinnitus New Post `slugToTitle` Title-Cases spaced-lowercase topics and splits on spaces-or-hyphens (was returning lowercase titles verbatim). Live-only (not yet in committed JSON): crypto New Post Build node curly-quote normalization.

Per-type conventions:
- **Crypto post**: starts `## Heading`; `<ArticleAd />`; images `![alt](/images/posts/x.jpg)`; main image ≠ body images; frontmatter `categories` (fixed list) + optional `crypto-ogs`/`exchanges` (Title Case) + `draft: false`; description 150-160 chars. Proactively link relevant existing crypto-OGs. Avoid brand-heavy/ad-like archive images. **Every name in `crypto-ogs`/`exchanges` must actually be linked in the body** - the AI tends to list OGs it never mentions (the gate now fails on this); either add a real mention+link or drop the name. If you trim a body link, drop the matching frontmatter entry too.
- **Crypto OG**: `## **Bold Heading**`; quotes `> "..." - Name`; social block in frontmatter (verify links via WebSearch; drop unverified); no tags; ISO date + order. Fact-check recent events (GPT-5 may miss them, e.g. verdicts/sentencings).
- **Tinnitus post**: opens `<Blockquote>` → main `<Image>` → intro; `## <Highlighter>Heading</Highlighter>`; `<AdComponent />`; first body image = main image (`/images/{slug}.jpg` flat); standalone sub-group labels that head a bullet list use `##### ` (h5); 2-3 lowercase tags from fixed vocab; description 120-135 chars (hard max 140). Title is auto-derived from the slug (Title Cased, small words lowercased, acronyms preserved via a map in the Build node) - the AI does not write it; spot-check any new acronym (add it to the `acronyms` map in the Build node if it comes out wrong, e.g. `cbt`/`tmj`/`airpods`).

## Step 4 - Stage locally + pick the main image
Copy the MDX to the site repo (`crypto-wiki/content/{posts|exchanges|crypto-ogs}/` or `tinnitus-blog/content/posts/`) - do NOT commit.

**Main image (posts only - auto-fetched from Pexels).** Applies to crypto posts and tinnitus posts, whose main image is conceptual/topical stock imagery. **Skip for crypto-OGs and exchanges** - those need a specific person's photo or a brand logo, which stock search can't supply; ask the user to drop those in manually at the frontmatter path (OGs are 500px PNGs, ~500px wide).

Flow for a post:
1. Derive a concrete visual search query from the topic (e.g. `What Are Layer 2 Blockchains` -> `blockchain network technology abstract`; avoid brand-heavy/ad-like results, matching the "no brand-heavy archive images" rule).
2. Run `scripts/pick_main_image.py --query "<query>" --slug <slug> --out <scratchpad>/imgpick [--width 800]` (script dir is this skill's folder; default width 800 for posts). It downloads 3 candidates, resizes each to the standard width, re-encodes JPEG < 200 KB, and prints a JSON manifest (file path, KB, photographer, Pexels URL).
3. `open` the three `candidate_*.jpg` so the user sees them, and ask which to use (offer a re-roll: re-run with `--page 2`, or a new `--query`).
4. On pick, copy the chosen candidate to the exact frontmatter path (`crypto-wiki/public/images/posts/<slug>.jpg` or `tinnitus-blog/public/images/<slug>.jpg`) and delete the preview dir. Pexels needs no attribution, but the manifest keeps the photographer/URL if the user ever wants to credit.

Site standards: posts ~800px wide JPG (existing archive is 800-900px, ~70 KB); crypto-OGs 500px. The script already keeps every candidate < 200 KB.

Then let the user review (offer dev server). Fold their feedback into guidelines/workflow so the next run is right by default.

## Step 5 - Push (only on explicit approval)
Commit post + ALL new images (check `git status` for untracked images - a missing image ships a broken page) to the site repo, push. Then **DEPLOY GATE**: poll the production article URL AND main-image URL (follow redirects; both sites 301 to www) until both return 200. Never share before this passes - the banner generator fetches the main image from production (black-spot banner otherwise).

## Step 6 - Share (only on explicit approval - posts publicly)
Before running: confirm the share image doesn't already exist in the automation repo (`images/posts/<slug>.png` or `images/crypto-ogs/<slug>.png` via GitHub API; if present from a previous run, `git rm` + push first - the Upload node is create-only and fails with "sha wasn't supplied").
Run the matching Share workflow. It posts to Telegram (binary upload), Instagram + Facebook (Twitter nodes are intentionally disconnected - no X API). Verify: every node success; Telegram result has a `photo` array; download the run's APITemplate `download_url_png` and view it to confirm the banner rendered (title + photo, no black spot).
**Single-channel re-share**: temporarily remove the other channel targets from `Format Social Post`'s connections, run, then restore.

## Safety
- Never push or share without the user's explicit go for that step.
- Secrets: `.n8n-api-key` (REST), `.pexels-api-key` (Step 4 images), and the MCP bearer token (in `~/.claude.json`) - never commit or echo them.
- Workflow edits: backup JSON to `.n8n-backups/` first; verify the PUT response.
