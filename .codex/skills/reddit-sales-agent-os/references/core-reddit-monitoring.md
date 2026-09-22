# Core Reddit Monitoring

Use this reference for the shared infrastructure behind both product discovery and selling mode.

## Goal

Build a durable Reddit listening system using public RSS feeds, not Reddit login automation.

Flow: subreddit list -> RSS pull -> normalized history -> subreddit profile -> queues and dashboards.

## RSS Rules

- Use public Reddit RSS feeds where available by adding .rss to public Reddit URLs.
- Pull posts and comments if available for the target URL.
- Preserve title, author, body/text, permalink, parent post, timestamp, subreddit, and fetched_at.
- Pace requests conservatively. Default to one request per minute from one IP unless the operator has verified another limit.
- On 429, wait and reduce frequency. Never rotate proxies to force throughput.
- Store every pulled item with a stable id or permalink so the system can avoid duplicates.

## Subreddit Selection

If the user knows subreddits, use them. If not, infer candidates from product, audience, or problem and mark unverified communities as review.

For each candidate subreddit, record: member count if available, activity level, buyer relevance, self-promotion tolerance, moderation strictness, link tolerance, and skip reason if not suitable.

## Subreddit Profile

Keep one markdown file per subreddit. Update it nightly from that day of activity. Only change the profile when new evidence adds or contradicts something. Append a dated update log entry explaining what changed and why.

Profile sections:

- Demographics: rough age, location, occupation, life/business stage, inferred only from what users say.
- Psychographics: wants, fears, identity, embarrassment, enemy identities, status anxieties.
- Language: exact phrases for problem, solution, failed attempts, and desired outcome.
- Failed attempts: what they tried and why they say it failed.
- Upvoted examples: what got attention and why.
- Buried or removed examples: what failed and why.
- Rules and moderation: links, self-promo, flair, format, forbidden topics, removal patterns.
- Tone: post length, structure, humor, directness, vulnerability, headers, opening style.
- Update log: date, evidence, change.

## Checks

- Do not mix profiles across subreddits.
- Separate quoted source language from inference.
- Mark rules as review if based on weak evidence.
- Record rate-limit and pull volume each run.

## Outputs

- subreddit-source-map
- reddit-feed-history
- subreddit-profile-files
- daily-profile-update-log
- rate-limit-report
