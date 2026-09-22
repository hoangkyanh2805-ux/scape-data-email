Contract version: 0.2
Runtime: Hermes profile `scapedata`
Default mode: research_only, public_data_only, no_outreach
Approver: human repo owner
# Post Collector Agent

## Goal
Collect public posts/videos/tweets/reels/threads from approved Forex sources for engagement mining.

## Scope
Autonomous:
- Run approved public-data Apify actors within written budget and item ceilings.
- Collect post URLs, text, hashtags, engagement metrics, publish dates, and author metadata.
- Keep source evidence for every collected post.

Out of scope:
- Comments/replies collection, profile enrichment, outreach, and private/login-only scraping.

## Inputs
- `source_map`, platform actor plan, max posts per source, date window, Apify budget ceiling.

## Tools
Allowed Apify actors after approval packet is accepted:
- TikTok videos/search: `clockworks/tiktok-scraper`, `apidojo/tiktok-scraper`, `get-leads/all-in-one-tiktok-scraper`.
- YouTube videos/search/channel: `streamers/youtube-scraper`, `hipersoft/youtube-scraper`.
- Instagram posts/reels/profiles: `apify/instagram-scraper`, `apify/instagram-post-scraper`, `vortex_data/instagram-scraper`.
- X/Twitter posts/search/profile: `scrapers/twitter`, `scrapesmith/twitter-x-scraper-tweets-profiles-replies`, `atomus/twitter-scraper`.
- Threads posts/search/profile: `webdata_labs/threads-scraper`, `lergassy/threads-scraper`.

Not allowed unless separately approved:
- Actors requiring login cookies or session tokens.
- Private group scrapers.
- High-volume follower/liker scraping.

## Permissions
Autonomous:
- Prepare actor inputs and dry-run plans.
- Run approved public actor jobs within cost/item ceilings.

Approval required:
- Paid actor run, high-volume run, login/session config, private/community source.

Forbidden:
- Running actors with cookies/session tokens without explicit approval.
- Collecting private content.

## Loop
read source_map -> choose whitelisted actor -> build approval/run packet -> run or stop -> collect dataset metadata -> normalize post_table

## Checks
- Actor id is whitelisted or explicitly approved.
- `max_items`, `max_cost_usd`, and budget ceiling are present.
- Every post has `source_url`, `post_url`, `actor_id`, `run_id` when run live.
- Actual/estimated cost is logged.

## Stop Conditions
- Missing cost ceiling.
- Actor requires login/session/private source.
- Actor/API fails 3 times.
- Rate limit, quota warning, or cost nearing ceiling.

## Human Approval Gates
- Apify run approval packet: platform, actor_id, input, max_items, estimated_cost, budget_ceiling.
- Any over-ceiling rerun.
- Any non-public actor configuration.

## Self-Improvement Hooks
Context retrieval:
- Read only relevant `source_map` rows, actor whitelist details, the Forex runbook, prior `post_table` artifacts, and approval packets for the current platform.
- Do not import actors, credentials, or routing assumptions from older Hermes profiles or other repos.

Quality metric:
- Improve the share of public post rows that have source URL, post URL, actor/run metadata, date/context, and visible engagement potential.

Non-improvement rule:
- If two actor/input attempts do not improve post quality, coverage, cost efficiency, or schema completeness, stop and hand off to `error-fix` or `approval-gate-reporter`.

Error signals:
- Missing actor id, cost ceiling, max items, source URL, or approval id for live runs.
- Actor schema mismatch or actor requires login/session/private data.
- Rate limit, quota warning, cost warning, or three repeated actor failures.
- Collected rows lack source evidence or required metadata.

Memory output:
- Emit concise run notes with actor id, run id, dataset id, source rows used, item count, cost estimate/actual, rejected configs, artifact path, and approval id.

## Outputs
- `post_table`: platform, source_url, post_url, author, text, hashtags, metrics, posted_at, actor_id, run_id.

## Acceptance Criteria
- Post rows are public-source only.
- Every row has source evidence and actor/run metadata.
- No comments, profiles, or emails are collected by this agent.

