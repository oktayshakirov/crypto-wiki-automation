# Changelog - publish-content-crypto

## 2026-10-03 - Article generation moved from GPT-5 to Claude

**What changed:** Step 2 no longer triggers the n8n "New Post" / "New Exchange" /
"New Crypto OG" workflows. Claude writes the MDX directly into the site repo and
registers it in `content-database.json`. The workflows are retained as a fallback.
Share and video workflows are untouched.

**Trigger:** the OpenAI account ran out of credit on 2026-10-03 (executions 702 and
703, HTTP 429 `insufficient_quota`), which blocked both sites. Investigation showed
the API has no free tier; a $5 prepaid deposit from ~2025-09 had been the only
funding. That prompted the question of whether the GPT-5 step was earning its place.

**Evidence gathered before deciding.** Raw GPT-5 output was recovered from execution
678 (2026-09-30, the tokenized-stocks post) while it was still inside n8n's 14-day
retention, and run through the unmodified gate:

| | Claude (MiCA, 2026-10-03) | GPT-5 raw (678) |
|---|---|---|
| Gate fails | 0 | 0 |
| Gate warnings | 0 | 2 |

Mechanically the two are near-equivalent, and the earlier assumption that GPT-5
output needed heavy mechanical repair was **wrong** - the Build node's auto-fixes
and the guidelines were doing their job. The real gap showed up only in the diff
between raw 678 and the published version (14 changed lines):

- **A figure off by 26x.** "Tokenized U.S. Treasury funds grew past $1 billion by
  2024" versus the actual $26.4 billion by March 2026. Stated confidently; the gate
  passed it.
- **An entire 2026 paragraph had to be added** that the model could not know: the
  SEC's five-year exemption (2026-09-17), Robinhood's 2026-07-01 launch across 120+
  countries on Robinhood Chain, Kraken's acquisition of Backed Finance (2025-12).
- **Answer-first was violated** ("Imagine buying a fraction of Apple or Tesla on a
  weekend...") - a rule the gate does not check, so it ships silently.

**Conclusion:** `gpt-5-2025-08-07` writes clean prose containing stale facts, and the
quality gate cannot see facts. On YMYL finance and living-person pages that is the
failure that matters.

**Known cost of the change:** the two-model check is gone. GPT-5 wrote and Claude
audited, so their blind spots did not line up; now Claude does both. The sourcing
discipline added to Step 2 (date every figure, search past the cutoff, verify every
external URL by fetching it, omit rather than estimate) is what replaces that
independence. `quality_gate.py` is unchanged and now carries more weight.

**Gotcha found during the first migrated post:** `content-database.json` was not
updated, because that was the `Update Database` node's job. Step 2 now spells out the
replication (dot-separated key, `next_orders` increment, no trailing newline).

**Also on this date:** six dead exchange-generator workflows were identified; two were
deleted (`H6X0O2HshAaMb3v4`, `Wq4XY7OUIKf8Xhu0`), with JSON backed up to the gitignored
`.n8n-backups/`. The other four were backed up but the delete was refused by the
permission classifier and left for the user.

**Open / unverified:** whether this holds up across types - only a post has been
migrated so far. Tinnitus, exchange and OG migrations are pending. The
`Format Social Post` node strips apostrophes from the banner text ("EU's" rendered as
"EUs" on the MiCA banner); cosmetic, banner-only, not yet fixed.

## Pending - native Facebook video test (2026-08-20)

`Publish Facebook Video` replaced the old Share Video workflow to test whether native
uploads out-earn YouTube link posts. All four crypto long-form videos went out this
way as the first test. **Results not yet recorded** - fill in once there is data.
