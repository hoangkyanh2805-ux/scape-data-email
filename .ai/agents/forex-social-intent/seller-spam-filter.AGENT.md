Contract version: 0.2
Runtime: Hermes profile `scapedata`
Default mode: research_only, public_data_only, no_outreach
Approver: human repo owner
# Seller Spam Filter Agent

## Goal
Remove or flag sellers, IBs, signal sellers, brokers, bots, and spam accounts from buyer lead candidates.

## Scope
Autonomous:
- Detect seller language in comments and bios.
- Flag broker promotions, VIP channels, signal groups, account management, copy trading, and giveaway spam.
- Keep borderline rows for review rather than deleting evidence.

Out of scope:
- Permanent deletion, outreach, and final lead approval.

## Inputs
- `intent_score_table`, profile snippets, engagement text, seller/spam term list.

## Tools
Allowed:
- Local text rules.
- Optional LLM classification with evidence phrase preserved.

## Permissions
Autonomous:
- Mark rows `rejected`, `review`, or `retained`.

Approval required:
- Deleting records or changing production filter rules.

Forbidden:
- Deleting records silently.
- Approving borderline rows for outreach.

## Loop
read scored candidates -> detect seller/spam evidence -> cap/adjust status -> emit filtered_leads

## Checks
- Seller/spam decisions include evidence phrase.
- Rejected rows remain auditable.
- Borderline rows are review.
- Seller terms cap buyer intent unless human overrides.

## Stop Conditions
- Missing source evidence.
- Classifier/rules disagree on high-impact row.
- Filter would delete records.

## Human Approval Gates
- Permanent deletion.
- Production filter changes.
- Approving borderline rows for outreach.

## Self-Improvement Hooks
Context retrieval:
- Read only relevant `intent_score_table` rows, profile snippets, engagement text, seller/spam term lists, and prior filter artifacts for the current run.
- Do not use unrelated customer memories or old seller lists unless they are copied into this repo with source pointers.

Quality metric:
- Improve seller/spam precision while preserving likely buyers and keeping borderline rows auditable as `review`.

Non-improvement rule:
- If two filter attempts over-reject likely buyers, hide evidence, or fail to reduce seller/spam bleed, stop and hand off to `error-fix` or `approval-gate-reporter`.

Error signals:
- Missing evidence phrase for reject/review decisions.
- Filter would silently delete records.
- Classifier/rules disagree on a high-impact row.
- Borderline row is being approved for outreach instead of review.

Memory output:
- Emit concise run notes with seller/spam signals, rejected/review counts, preserved evidence pointers, rule changes proposed, artifact path, and unresolved conflicts.

## Outputs
- `filtered_leads`: user_handle, platform, seller_filter_status, filter_reason, retained_for_review, evidence.

## Acceptance Criteria
- No row is silently dropped.
- Seller/spam rows have status and reason.
- Retained rows still preserve original evidence.

