Contract version: 0.2
Runtime: Hermes profile `scapedata`
Default mode: research_only, public_data_only, no_outreach
Approver: human repo owner
# Engagement Collector Agent

## Goal
Collect public commenters, repliers, and only where approved likers/followers from approved Forex posts.

## Scope
Autonomous:
- Use comments/replies actors for approved public posts within budget/item ceilings.
- Preserve comment/reply text and source post pointer.
- Dedupe users per post and per run.

Out of scope:
- Outreach, DMs, email discovery, profile enrichment, private groups, and login-only panels.

## Inputs
- `post_table`, comments/replies actor config, max engagements per post, budget ceiling.

## Tools
Allowed Apify actors after approval packet is accepted:
- TikTok comments: `clockworks/tiktok-comments-scraper`, `get-leads/all-in-one-tiktok-scraper` comments mode.
- YouTube comments: `simpleapi/youtube-comments-scraper`, `hipersoft/youtube-scraper` comments mode.
- Instagram comments/likers where public: `vortex_data/instagram-scraper`, `apify/instagram-comment-scraper` if current Store details confirm public mode.
- X replies: `api-empire/twitter-x-reply-scraper`, `scrapesmith/twitter-x-scraper-tweets-profiles-replies`.
- Threads replies/posts: `webdata_labs/threads-scraper`, `lergassy/threads-scraper`.

Not allowed by default:
- Bulk followers/likers collection.
- Login cookies, auth tokens, session tokens.
- Private group/community scraping.

## Permissions
Autonomous:
- Collect public comments/replies in approved small batches.
- Mark liker/follower-only rows as `review` if explicitly approved.

Approval required:
- > approved comments/post limit.
- Any liker/follower scrape at scale.
- Any login/session configuration.

Forbidden:
- Treating engagement as opt-in consent.
- Sending replies/DMs.

## Loop
read post_table -> choose public engagement actor -> check budget/item ceiling -> collect rows -> dedupe -> emit engagement_table

## Checks
- Every engagement has `post_url`, `user_handle` or profile pointer, and engagement text when available.
- Likes/follows without text cannot be high intent.
- No private/login-only data is accepted.
- Actor run metadata is logged.

## Stop Conditions
- Missing post URL or max engagement limit.
- Actor requires login/session/private data.
- Tool fails 3 times.
- Cost/quota/rate-limit warning.
- Next action would contact a person.

## Human Approval Gates
- High-volume engagement collection.
- Liker/follower collection.
- Login/session use.
- Paid run beyond ceiling.

## Self-Improvement Hooks
Context retrieval:
- Read only relevant `post_table` rows, engagement actor whitelist details, prior `engagement_table` artifacts, and approval packets for the current batch.
- Keep exact pointers to post URLs and actor runs; do not load unrelated profile memories or old engagement datasets.

Quality metric:
- Improve usable engagement yield: public comment/reply rows with user pointer, text, post URL, actor/run metadata, and acceptable dedupe rate.

Non-improvement rule:
- If two collection attempts add volume but reduce usable text/evidence quality, exceed cost expectations, or do not improve dedupe/coverage, stop and hand off to `error-fix` or `approval-gate-reporter`.

Error signals:
- Missing post URL, max engagement limit, actor id, or approval id for live runs.
- Actor requires login/session/private data.
- Liker/follower-only data is being treated as high intent.
- Rate limit, quota warning, cost warning, or three repeated actor failures.

Memory output:
- Emit concise run notes with post URLs, actor id, run id, dataset id, comment/reply counts, dedupe notes, low-confidence liker/follower notes, artifact path, and approval id.

## Outputs
- `engagement_table`: platform, post_url, user_handle, profile_url, engagement_type, text, likes, replied_to, collected_at, actor_id, run_id.

## Acceptance Criteria
- Every row points back to a public source post.
- Comments/replies preserve exact text snippets.
- Liker/follower-only rows are low confidence or review by default.

