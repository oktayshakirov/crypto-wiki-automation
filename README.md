# Crypto Wiki Automation

The content pipeline behind [thecrypto.wiki](https://thecrypto.wiki): topic
research, article writing, an automated quality gate, publishing and social
distribution for a crypto encyclopedia of explainers, exchange reviews and
profiles of the people who shaped the industry.

The articles are written by an AI agent working through a
[Claude Code](https://claude.com/claude-code) skill, checked by a scripted
quality gate, reviewed by a human, and then deployed and shared by
[n8n](https://n8n.io) workflows.

## The pipeline

1. **Suggest.** The agent reads `content-database.json` (every published post,
   exchange and profile) and proposes topics that fill real gaps.
2. **Write.** One article per run, following the house guidelines for its type,
   with sourced claims, internal links and an answer-first opening.
3. **Quality gate.** `quality_gate.py` runs about 20 checks before anything is
   staged: word count, 8-15 valid internal links, body images from the real
   archive and not repeated in recent posts, ad and image placement, no em
   dashes or curly quotes, no stray metadata.
4. **Stage and review.** The article is staged in the site repo and reviewed
   locally. Main images for posts come from Pexels via `pick_main_image.py`.
5. **Publish.** A push to the site repo, then a deploy gate that waits until the
   page is actually live before anything is shared.
6. **Share.** n8n workflows render a social card and post it to X, Facebook,
   Instagram and Telegram.

## What is here

| Path | Contents |
|---|---|
| `.claude/skills/publish-content-crypto/` | The agent skill: the full run, the quality gate and the image picker |
| `post_guidelines.md`, `exchange_guidelines.md`, `crypto_og_guidelines.md` | House style and structure for each content type |
| `content-database.json` | The index of everything published, used for topic gaps and link validation |
| `content/`, `images/` | Generated articles and images, before they are copied into the site repo |
| `*.json` (root) | Committed snapshots of the n8n workflows |
| `scripts/verify_socials.py` | Resolve-checks social and app links before they go into an exchange review |

### n8n workflows

| Workflow | What it does |
|---|---|
| `share_post`, `share_exchange`, `share_og` | Render a social card (APITemplate.io) and post to X, Facebook, Instagram and Telegram |
| `share_video`, `share_video_telegram` | Announce a new video on Facebook and Telegram |
| `publish_reel`, `publish_facebook_video` | Publish a finished vertical video as an Instagram/Facebook Reel, or long-form video natively on Facebook |
| `new_post`, `new_exchange`, `new_crypto_og` | The original OpenAI-based generators, kept as a fallback |

Credentials are referenced by n8n id only; no keys or tokens are stored in this
repo.

## Setup

- A local n8n instance at `http://localhost:5678` with the workflows imported
  and their credentials connected
- `.n8n-api-key` and `.pexels-api-key` in the repo root (both gitignored)
- The site repo checked out next to this one as `crypto-wiki/`
- Python 3 for the skill scripts

The sister pipeline for [tinnitushelp.me](https://tinnitushelp.me) is
[tinnitus-help-automation](https://github.com/oktayshakirov/tinnitus-help-automation);
the videos for both sites come from
[video-edit-automation](https://github.com/oktayshakirov/video-edit-automation).

## Author

Oktay Shakirov
