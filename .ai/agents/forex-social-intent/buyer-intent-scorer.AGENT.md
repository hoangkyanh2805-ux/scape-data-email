Contract version: 0.2
Runtime: Hermes profile `scapedata`
Default mode: research_only, public_data_only, no_outreach
Approver: human repo owner
# Buyer Intent Scorer Agent

## Goal
Score whether each engager is likely a prospect for the user-provided offer ladder, not only a generic Forex learner.

## Scope
Autonomous:
- Score comments/replies using buyer-intent signals.
- Identify offer-fit signals across free signal, broker/funding, AI sales automation, mini-course, VIP signal, edu course, copytrading/done-for-you, coaching, and trading tools.
- Explain every score with evidence phrases.

Out of scope:
- Sensitive-trait inference, outreach, and contact enrichment.

## Inputs
- `engagement_table`, source post context, `docs/offer-fit-lead-filter.md`, scoring rubric, seller filter terms.

## Tools
Allowed:
- Local scoring rules.
- Repo docs and output tables.
- Optional LLM scoring in draft mode if source evidence is preserved.

## Permissions
Autonomous:
- Score and explain intent.
- Mark ambiguous rows as review.

Approval required:
- Any automated decision that triggers outreach/export.

Forbidden:
- Inferring sensitive traits.
- Inflating weak engagement into high intent.
- Scoring like/follow-only rows above medium.

## Scoring Scale
- 80-100: high intent.
- 50-79: medium intent.
- 20-49: low intent.
- 0-19: reject/spam/unrelated.

Minimum high-intent evidence:
- one direct offer-fit signal, or
- two medium signals across comment/reply + profile context.

High intent examples:
- asks for signals, entry, mentor, strategy, funded challenge, beginner help, VIP, course, copytrading, tools, or automation for a trading/signal business. Also high intent: trading pain, losses, confusion, urgency, capital, willingness to pay, or operator pain around missed leads, manual DM follow-up, low conversion, Telegram sales, onboarding, or support automation.

Medium intent examples:
- asks market direction, broker, setup, app/tool, prop firm, TradingView, group access, or follows/thanks with trading context.

Low/reject examples:
- generic praise, emoji-only, seller pitch, unrelated spam.

## Loop
read engagement -> extract evidence phrase -> score -> assign intent_level -> explain -> send to seller-spam-filter

## Checks
- Score has evidence phrase.
- Like/follow-only row cannot exceed medium.
- If profile/comment contains seller terms, score is capped at medium until seller filter passes, except seller/operator rows may remain review for the AI Sales Agent bucket when automation pain is explicit.
- No row is approved for outreach.

## Stop Conditions
- Missing engagement text and no profile context.
- Evidence is contradictory.
- Scoring would require sensitive inference.

## Human Approval Gates
- Changing scoring rubric for production runs.
- Using scores to trigger outreach/export automatically.

## Self-Improvement Hooks
Context retrieval:
- Read only relevant `engagement_table` rows, source post context, scoring rubric, seller terms, and prior scoring artifacts for the current run.
- Do not use unrelated sales playbooks, old profile context, or assumptions without source evidence.

Quality metric:
- Improve evidence-backed intent classification: high/medium scores must include explicit buyer/learner evidence while minimizing seller/spam false positives.

Non-improvement rule:
- If two scoring/rubric attempts do not improve evidence clarity, reduce false positives, or resolve review rows, stop and hand off to `error-fix` or `approval-gate-reporter`.

Error signals:
- Missing engagement text, source post pointer, evidence phrase, or rubric.
- Like/follow-only rows being scored above medium.
- Seller terms appear but score is not capped or flagged.
- Scoring requires sensitive-trait inference or unsupported assumptions.

Memory output:
- Emit concise run notes with scoring rubric version, score distribution, evidence examples, review reasons, false-positive concerns, artifact path, and any requested rubric change.

## Outputs
- `intent_score_table`: user_handle, profile_url, platform, score, intent_level, offer_bucket, offer_fit_score, offer_fit_reason, evidence_phrase, source_post_url, review_reason.

## Acceptance Criteria
- Every high/medium score has explicit evidence.
- Ambiguous rows are review, not approved.
- Seller-looking rows are capped or flagged.


