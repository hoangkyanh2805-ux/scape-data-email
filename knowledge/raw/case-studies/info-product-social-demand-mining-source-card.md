# Source Card - Info Product Social Demand Mining Guide

Date ingested: 2026-09-21
Source type: pasted script/article
Local attachment: `C:\Users\Admin\.codex\attachments\303d6020-440f-4c9e-839d-0798c322b955\pasted-text.txt`
Working title: `how to sell info products (FULL GUIDE)`
Confidence: medium-high for mechanism extraction; low for any unverified numeric claims.

## Source Summary

The source describes a demand-first method for finding info product niches from Reddit and Facebook. The core mechanism is: find public posts where people ask urgent questions in their own words, rank communities by engagement intensity, build the product and ad copy from repeated questions/phrases, then automate periodic reruns.

## What Matters For scape-data

This repo is not adopting the product, Whop, ad, Telegram, or outreach parts. It is reusing only the research mechanism:

```text
find questions first -> rank urgency -> preserve exact language -> score intent -> enrich public contact data only
```

## Source Facts Preserved

- Reddit is framed as useful because anonymity makes problem language rawer.
- Facebook is framed as useful because public real-name posting can signal stronger embarrassment/urgency.
- Reddit scrape method: select communities, scrape top posts from the last month, keep title/body/comment count/score/subscriber count.
- Facebook scrape method: search phrases across public groups, keep post text/group/reactions/comments/date.
- Ranking metric: comments per thousand subscribers.
- Product/ad mechanism: repeated exact phrases become product sections and hooks.
- Automation boundary in the source: stop before publishing, launching campaigns, or changing budgets.

## Do Not Import

- Do not turn this repo into an info-product launch repo.
- Do not add Whop checkout/page/ad automation.
- Do not automate Telegram commands from this source.
- Do not send outreach, replies, DMs, or comments.
- Do not scrape private Facebook groups or logged-in sources.
