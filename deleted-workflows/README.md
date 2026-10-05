# deleted-workflows

JSON snapshots of n8n workflows that were **deleted**, kept here because they
cannot be recovered any other way.

`.n8n-backups/` is gitignored, so everything in it is local to one machine and
does not survive a fresh clone. For a workflow that still exists in n8n that is
fine, since the live copy is the source of truth and the current state of the
important ones is committed at the repo root (`new_post.json`, `share_post.json`,
...). For a **deleted** workflow there is no live copy, so these files are the
only record and they belong in version control.

Nothing here runs. These are archives. To restore one, POST it to the n8n API
(`/api/v1/workflows`) or import the JSON through the n8n UI, then reconnect its
credentials, which are referenced by id and name only and are not stored here.

## Contents

| Workflow | ID | Deleted | Why |
| --- | --- | --- | --- |
| Crypto Wiki: Share Video | `MZy8L37FaVL5zh64` | 2026-08-20 | Replaced by `Crypto Wiki: Publish Facebook Video`. It posted a YouTube URL and let Facebook and Telegram unfurl it into a card; a link post sends the viewer to YouTube and earns the reach an outbound link earns, which is the thing native upload exists to avoid. |
| Tinnitus Help: Share Video | `q3omZaUm7kpTc6WE` | 2026-08-20 | Same change on the tinnitus side. |
| Exchange Automation | `H6X0O2HshAaMb3v4` | 2026-10-03 | Dead exchange generator, inactive since 2025-09-12, superseded by `Crypto Wiki: New Exchange`. |
| Exchange Review Automation (Manual Trigger) | `Wq4XY7OUIKf8Xhu0` | 2026-10-03 | As above. |
| Exchanges Automation | `cjW29Cgq1M8CeG8Y` | 2026-10-05 | As above. Used an `HTTP: Generate Body` node rather than the OpenAI node. |
| Exchange Review Automation (Manual Trigger) | `8el6UIQwjc8gtzVK` | 2026-10-05 | As above, duplicate name, HTTP variant. |
| Crypto Exchange Post Generator v2 | `3dospMhqO86wiLMl` | 2026-10-05 | As above. |
| Crypto Exchange Post Generator Simple | `EFX8AvarQY7wJ6kL` | 2026-10-05 | As above. |

The six exchange generators had all been inactive since 2025-09-12 and were
invisible in the n8n dashboard, which hides deactivated workflows behind a
status filter. That is why they sat there for a year.

The two `share_video_*.json` files are earlier snapshots of the same two Share
Video workflows, kept alongside their final `before-delete` state.

## What is deliberately not here

The other ~100 files in `.n8n-backups/` are routine pre-edit snapshots of
workflows that still exist. They stay local and ephemeral on purpose: the live
workflow is the source of truth, and committing every intermediate state would
bury the records that actually matter.
