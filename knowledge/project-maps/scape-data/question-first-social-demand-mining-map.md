# Project Map - Applying Question-First Demand Mining To scape-data

Source playbook: `knowledge/distilled/playbooks/question-first-social-demand-mining.md`
Project mission: collect reviewable public social email/contact data only.

## What To Adopt

Adopt these mechanisms:

- Find public questions before choosing sources.
- Rank sources by urgency and comment density, not follower/member count.
- Preserve exact phrases as evidence.
- Use repeated phrases to build search queries and scoring rules.
- Treat dead broadcast groups/pages as bad sources even when member count is high.
- Keep monthly/weekly rerun logic as a future research schedule, not automation yet.

## What To Reject

Reject these parts for this repo:

- Info product creation.
- Whop checkout/page creation.
- Ad creative generation.
- Campaign launch or budget changes.
- Telegram command bot deployment.
- Facebook private/logged-in scraping.
- Any outreach/posting/replying.

## Updated Source-Finder Behavior

`source-finder` should look for question-rich sources, not just large accounts.

Preferred source signals:

```text
many comments per post
repeated question phrasing
non-seller users asking for help
public source URL
recent activity
low seller-spam ratio
```

## Updated Buyer-Intent Scoring

A candidate is stronger when their own text contains:

```text
I need help
how do I
why do I keep
can someone explain
what should I do
beginner here
failed again
any advice
```

For Forex, combine those patterns with niche terms:

```text
XAUUSD
FTMO
prop firm
funded challenge
ICT
SMC
risk management
stop loss
entry
broker
```

## Updated Reporting

Batch reports should include:

```text
source_quality_rank
usable_comment_rate
high_intent_rate
seller_spam_rate
repeated_phrases_top_10
public_email_yield
keyword_false_positive_notes
dead_source_notes
```

## Prompt Asset

Use:

```text
knowledge/reusable-assets/prompts/hermes-question-first-social-demand-mining.prompt.md
```
