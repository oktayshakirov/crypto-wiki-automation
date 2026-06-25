---
name: publish-content
description: Publish content to the user's sites (thecrypto.wiki, Tinnitus Help) by driving the local n8n workflows over MCP — create a review/post/OG, optionally enrich social links, get human approval, then post to social media. Use when the user wants to add/create/publish or share an exchange, post, crypto OG, or sound.
---

# Publish Content

Orchestrates the user's local n8n workflows (via the `mcp__n8n-local__*` MCP tools) to
publish content end-to-end, with a **human-approval gate before anything is posted publicly**.

## Prerequisites
- **n8n must be running** at `http://localhost:5678`. If `mcp__n8n-local__search_workflows`
  fails to connect, stop and ask the user to start n8n.
- All listed workflows use **Form Triggers**, so inputs are passed as `formData`.
- Edit access (rarely needed) uses the REST API key in `.n8n-api-key` (gitignored).

## Workflow registry (all Form-Trigger driven)
Run with `mcp__n8n-local__execute_workflow` →
`inputs: { type: "form", formData: { <field>: <value> } }`

| Site | Action | Workflow ID | formData |
|---|---|---|---|
| Crypto Wiki | New Exchange | `pEfGTfVz5FdtLTGM` | `{ name, website }` |
| Crypto Wiki | Share Exchange | `KYJga45bwixvg8DY` | `{ slug }` |
| Crypto Wiki | New Post | `aPOOMzK1MuUcr6sM` | `{ topic }` |
| Crypto Wiki | Share Post | `LUkP4LjfcWefJZpJ` | `{ slug }` |
| Crypto Wiki | New Crypto OG | `MYaoP3c6N5qLFX3U` | `{ name }` |
| Crypto Wiki | Share Crypto OG | `5dyD2hHUqfHCV8Rw` | `{ slug }` |
| Tinnitus Help | New Post | `pddxBAmv2k2nSBv2` | `{ topic }` |
| Tinnitus Help | Share Post | `jtUStrxCt23FGNDk` | `{ slug }` |
| Tinnitus Help | Share Sound | `UcubZDb1sKnszcZX` | `{ slug }` |

Always call `mcp__n8n-local__get_workflow_details` first to confirm the current form fields
before executing (the registry can drift).

## Flow

### 1. Decide what to publish
- Use what the user asked for. For "next item" choices, read `content-database.json`
  (`exchanges`/`posts`/`crypto_ogs`/`tools`, plus `next_orders.<type>` for the order counter)
  to see what exists and avoid duplicates. For exchanges, find gaps vs
  coinmarketcap.com/rankings/exchanges/ via **WebSearch** (page is JS-rendered).
- Confirm the choice + inputs with the user.

### 2. Create (the "New …" workflows — commit to GitHub)
- Execute with the right `formData`. The **GPT-5 node** intermittently fails with
  ECONNRESET/ETIMEDOUT (it has retryOnFail 3x); if `success:false`, re-run once or twice,
  and inspect `/api/v1/executions/<id>?includeData=true` to see the failing node.
- On success it commits the MDX + updates `content-database.json` in
  `oktayshakirov/crypto-wiki-automation`. Capture commit URLs.

### 3. Enrich social links — EXCHANGES (and OGs) only
"New" workflows reliably fill only `social: website`. For exchanges (and crypto OGs, which
have social profiles), enrich: **discover** via WebSearch (official accounts + real Play /
App Store listings — never scrape the site, they bot-block) → **verify** with
`python3 scripts/verify_socials.py 'twitter=...' ...` (run where network is open; the Claude
sandbox can't reach Google/Apple) → **write** only confirmed links into the MDX `social:`
block (key order as in `content/exchanges/binance.mdx`) → commit via git/gh (`git pull` first).
Skip for plain posts/sounds.

### 4. ⚠️ Approval gate (REQUIRED before any "Share …")
Social posting is public and irreversible. Stop, show the user the item + target channels,
and get explicit confirmation.

### 5. Share (the "Share …" workflows)
⚠️ **Repo gap:** Share workflows READ the MDX from the live **site** repo
(`oktayshakirov/crypto-wiki` for Crypto Wiki; the Tinnitus site repo for Tinnitus Help),
while "New" workflows WRITE to `crypto-wiki-automation`. The MDX must be synced to the site
repo first, or the Share run 404s on its `Get … MDX` node. Confirm before sharing.
- Execute the matching Share workflow with `{ slug }`. Posts to Telegram, Instagram,
  Facebook, Twitter/X. Report status + verify.

### 6. Report
Summarize commits, any social block added, share execution id, and channels posted.

## Safety
- Never run a "Share …" workflow without the step-4 approval.
- Secrets (`.n8n-api-key`, MCP token) are never committed or echoed.
- Editing a live workflow via REST: back up to `.n8n-backups/` first, mutate the workflow
  dict **in place** (don't reassign a local `nodes` list — it silently drops changes), and
  PUT only `name,nodes,connections,settings`.
