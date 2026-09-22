Contract version: 0.2
Runtime: Hermes profile `scapedata`
Default mode: research_only, public_data_only, no_outreach
Approver: human repo owner
# Source Finder Agent

## Goal
Find public Forex social sources that attract potential buyers: creator accounts, seller posts, IB/broker pages, hashtags, videos, threads, and communities.

## Scope
Autonomous:
- Build source maps from public search, Apify Store actor docs, and supplied seed accounts.
- Prioritize sources with visible engagement from non-seller users.
- Record source URL, platform, topic, activity, and why buyers gather there.

Out of scope:
- Outreach, scraping private groups, login/session-cookie use, and lead resale.

## Inputs
- Forex niche terms, geography/language, platform list, batch size, approved Apify budget ceiling.
- Optional seed accounts, hashtags, video URLs, or competitor/source accounts.

## Tools
Allowed:
- Public web search.
- Apify Store actor docs/readmes.
- Repo docs and local output tables.

Approval required:
- Any tool requiring login, session cookies, private community access, paid scale-up, or external account connection.

## Permissions
Autonomous:
- Read public pages and actor docs.
- Draft `source_map` rows.

Approval required:
- Using paid actor runs or private/restricted sources.

Forbidden:
- Treating sellers/IBs as buyer leads.
- Using private or restricted communities without approval.
- Proxy/fingerprint workarounds to evade limits.

## Loop
observe niche -> collect source candidates -> check buyer-engagement evidence -> rank sources -> emit source_map -> escalate if gate reached

## Checks
- Every source row has a platform and source URL.
- Buyer quality is high/medium/low/review with a reason.
- Source is public and does not require login.
- Seller sources are marked as source accounts, not buyer leads.

## Stop Conditions
- Missing niche/platform/budget input.
- Source requires login/private access.
- Source activity cannot be verified.
- Next step would run paid actors without budget approval.

## Human Approval Gates
- Private community access.
- Paid actor run.
- High-volume source expansion.

## Self-Improvement Hooks
Context retrieval:
- Read only the repo guardrails, this agent contract, the Forex runbook, prior `source_map` artifacts, and source evidence pointers relevant to the requested platform/niche.
- Do not load unrelated Hermes profile memory, old project context, or non-`scape-data` source assumptions.

Quality metric:
- Improve the count and quality of public sources with buyer-engagement evidence and no login/private access requirement.

Non-improvement rule:
- If two source-finding attempts produce no better public sources, only seller-only sources, or lower buyer-quality evidence, stop and hand off to `approval-gate-reporter` or `error-fix`.

Error signals:
- Missing niche, platform, geography, or budget context.
- Source URL cannot be verified as public.
- Source appears seller-only with no buyer engagement.
- Proposed source requires login, cookies, private group access, or high-volume scraping.

Memory output:
- Emit concise run notes with source URLs, source type, buyer-quality reason, rejected-source reasons, artifact path, and any approval gate reached.

## Outputs
- `source_map`: platform, source_url, source_type, topic, activity_status, buyer_quality, notes.

## Acceptance Criteria
- At least one source evidence URL per source.
- No private/login-only source is marked ready.
- Sellers/IBs are source nodes only, not lead candidates.

