# Agent Contracts

Use these contracts when splitting the Reddit system into reusable jobs.

## Reddit Feed Monitor Agent

Goal: collect public Reddit RSS items safely and consistently.

Inputs: subreddit list, RSS URLs, pull cadence, storage destination.

Autonomous actions: pull public RSS within rate limits, normalize posts/comments, dedupe by permalink/id, log volume and errors.

Human approval required: none for public read-only pulls within approved limits; approval required for private communities or paid tooling.

Outputs: reddit-feed-history, rate-limit-report, fetch-error-log.

Stop when: 429 occurs repeatedly, source format changes, subreddit access becomes unavailable, or cadence would exceed rate limits.

## Subreddit Profiler Agent

Goal: maintain one evidence-backed profile per subreddit.

Inputs: reddit-feed-history, existing profile, subreddit rules evidence.

Autonomous actions: update demographics, psychographics, language, failed attempts, upvoted examples, buried examples, rules, tone, and update log.

Human approval required: using private user data or treating weak inferences as facts.

Outputs: subreddit-profile-file, daily-profile-update-log.

Stop when: evidence is too thin, rules are unclear, or profile conflicts with recent moderation outcomes.

## Product Discovery Agent

Goal: find repeated urgent problems that may justify a product or guide.

Inputs: subreddit profiles, feed history, niche constraints, risk boundaries.

Autonomous actions: cluster repeated problems, count frequency, quote examples, rank by urgency and paid intent, draft product brief.

Human approval required: selecting risky niches, building a paid product, publishing landing page, setting checkout.

Outputs: niche-candidate-table, repeated-problem-analysis, product-or-guide-brief, landing-page-copy-draft.

Stop when: no repeated high-intent problem exists or the niche needs credentials/harm review.

## Product File Agent

Goal: maintain the source of truth for what the product does and does not promise.

Inputs: product description, price, page, subreddit quotes, objections.

Autonomous actions: draft and update product file, claims boundary, objection answers.

Human approval required: changing price, changing product promise, approving regulated claims.

Outputs: product-file.

Stop when: product boundaries are unclear or claims exceed evidence.

## Thread Match Agent

Goal: find fresh posts/comments where a helpful reply is appropriate.

Inputs: product file, subreddit profiles, feed history.

Autonomous actions: score matches 1 to 5, flag urgent solution-seeking threads, skip poor fits, queue draft-needed items.

Human approval required: none for draft matching.

Outputs: thread-match-queue, skipped-opportunity-log.

Stop when: subreddit rules make replies risky or match confidence is low.

## Reply And Post Draft Agent

Goal: write useful non-promotional drafts in the subreddit voice.

Inputs: match queue, product file, subreddit profile, thread context.

Autonomous actions: draft replies and posts, include risk notes, sort by urgency, prepare copy-ready queue.

Human approval required: every post/comment/DM, every link, every product mention.

Outputs: reply-draft-queue, post-draft-queue.

Stop when: draft would be spammy, promotional, unsupported, or against subreddit rules.

## Dashboard Ops Agent

Goal: make the daily work queue visible to the human operator.

Inputs: queues, sent log, profile changes, account health notes.

Autonomous actions: update dashboards, summarize morning queue, send reminders if notification channel is approved.

Human approval required: publishing dashboard publicly, posting to Reddit, sending external promotional messages.

Outputs: product-discovery-dashboard, selling-dashboard, morning-summary, posting-window-reminders.

Stop when: dashboard cannot verify state or notification would expose sensitive data.
