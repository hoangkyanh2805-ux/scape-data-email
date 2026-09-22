# Playbook - Question-First Social Demand Mining

Source: `how to sell info products (FULL GUIDE)` pasted script
Project fit: `scape-data` public social email/contact data pipeline

## Core Principle

Do not start from a product, offer, or guessed audience. Start from repeated public questions and complaints. The best lead source is a place where people are already asking for help in their own words.

For `scape-data`, the reusable version is:

```text
public question/complaint -> engagement intensity -> repeated phrases -> buyer intent signals -> public profile/email enrichment
```

## Mechanism

1. Pick several communities, pages, posts, creators, hashtags, or query phrases in a niche.
2. Collect public posts and comments where people talk about their own problem.
3. Rank sources by urgency, not raw size.
4. Preserve exact phrasing because it becomes query terms, scoring evidence, and review language.
5. Filter out sellers, broadcasters, admins, and dead groups/pages.
6. Enrich only the people who showed intent through their own public text.

## Metrics To Reuse

### Engagement Density

For communities with known size:

```text
comments_per_1k_members = total_comments / subscribers_or_members * 1000
```

For post/video sources where member count is unavailable:

```text
usable_comment_rate = usable_intent_comments / total_comments_collected
high_intent_rate = high_intent_comments / total_comments_collected
seller_spam_rate = rejected_seller_spam / total_comments_collected
public_email_yield = sourced_public_emails / retained_profiles
```

## Source Quality Rules

Good source:

- People ask personal, concrete questions.
- Comments/replies contain pain, confusion, requests, or decision language.
- The same phrasing repeats across multiple posts.
- Engagement is from real users, not only admins/sellers.
- Public profile/contact enrichment is possible later.

Bad source:

- Broadcast posts with no comments.
- Seller/IB/broker pages where commenters are mostly sellers too.
- Hobby/audience-only groups with low urgency.
- Keyword false positives where the phrase appears in unrelated contexts.
- Private/login-only groups.

## Exact-Language Extraction

For every batch, extract:

```text
repeated_question
count
example_phrases
source_urls
platform
context
intent_type
```

Use repeated phrases for:

- Apify/search queries;
- buyer-intent scoring rules;
- review labels;
- report summaries;
- future creative/offers only if a separate project asks for that.

## Application To Forex Email Data

Forex-specific examples of repeated questions/phrases to mine:

```text
how do I pass FTMO
why do I keep failing prop challenges
XAUUSD entry help
ICT beginner help
SMC strategy question
funded trader advice
best broker for beginners
why did gold hit my stop loss
need help with risk management
```

Use comments/replies first. A like/follow alone is weak evidence and should not produce a high-intent lead.

## Stop Boundaries

For this repo, stop before:

- building or selling an info product;
- writing ad creative for launch;
- deploying Whop checkout;
- launching campaigns;
- sending outreach;
- syncing emails to external tools;
- using private groups or login/session cookies.

## Hermes Loop

```text
source-finder: find question-rich public sources
post-collector: collect posts/videos around repeated questions
engagement-collector: collect public comments/replies
buyer-intent-scorer: score based on exact phrases and urgency
seller-spam-filter: remove sellers/brokers/IB spam
profile-enricher: enrich retained profiles with public contact fields only
lead-normalizer: dedupe and preserve source evidence
approval-gate-reporter: report yield, risk, and next safe test
```

## Acceptance Criteria

- Every candidate has a source question/comment or public evidence pointer.
- Every high-intent score has an exact phrase.
- Every email has `email_source_url` and `email_source_field`.
- Seller/broadcast/dead-source rows are preserved as rejected/review, not silently deleted.
- No outreach/export occurs.

## Sub-Agent Review Notes

A second review agent confirmed the source should be used only as research intelligence for `scape-data`.

Reusable insights:

- Find questions before emails.
- Commenters/repliers matter more than sellers or creators.
- Comment count and reply depth are urgency proxies.
- Normalize engagement by source size when possible.
- Keyword/phrase search can beat fixed group/account lists because large groups can be dead.
- Community/post/query names can be intent signals.
- Read top items to extract repeated phrases before scaling.
- Distinguish audience size from market pain.
- Current-solution dissatisfaction is a strong intent signal.
- Periodic reruns can improve source/query/scoring quality without outreach.

Rejected for this repo:

- info product creation;
- Whop checkout/page setup;
- ad creative/campaign launch;
- DMs/replies/posts;
- private/login-only data;
- inferred/generated emails;
- external export without approval.
