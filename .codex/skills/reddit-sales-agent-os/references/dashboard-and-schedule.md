# Dashboard And Schedule

Use this reference to turn the Reddit system into a daily operating loop.

## Dashboards

Build or maintain two plain one-page dashboards when requested. Keep them functional, not decorative.

## Product Discovery Dashboard

Purpose: show what problems are emerging.

Sections:

- This week by repeated problem, ranked by frequency and urgency.
- Representative real quotes under each problem.
- Paid alternatives people mention.
- Subreddit profile changes.
- Niches or problems marked review due to credential, harm, or moderation risk.
- Recommended next research step.

## Selling Dashboard

Purpose: show what the human can safely post today.

Sections:

- Reply queue with full text, copy button, direct thread/comment link, subreddit, score, urgency, and risk notes.
- Post queue with full text, submit link, best posting window, removal risk, and suggested edits.
- Sent log so the operator does not hit the same thread twice.
- Skipped items and reasons.
- Account health notes: removals, warnings, subreddit rule shifts, unusual response patterns.

If something important does not fit either page, add a new section rather than dropping it.

## Schedule

Default cadence:

- Every 30 minutes: pull new public RSS items from monitored subreddits, paced within the rate limit.
- Through the day: find new product matches and queue replies.
- Nightly: update subreddit profiles from the day activity.
- Morning: draft up to five posts, refresh both dashboards, and send a summary notification.
- Weekly: run repeated-problem analysis and report what changed.

## Notifications

Morning message should include dashboard links, number of queued replies, number of queued posts, profile changes, and any risks.

Posting-window reminder should trigger only when a queued post exists for that subreddit.

Staleness reminder should trigger when a high-priority reply opportunity is likely to lose relevance soon.

## Checks

- Dashboard items must have direct links and status.
- Sent log must prevent duplicate replies.
- Removals or rule changes must show up as account health notes.
- All queued actions remain draft until the human posts them.
