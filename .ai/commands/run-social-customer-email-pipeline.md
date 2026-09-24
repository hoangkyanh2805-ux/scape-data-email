# Command: run-social-customer-email-pipeline

Use this command when the goal is to find public customer emails from social sources without collecting creators, sellers, IBs, brokers, affiliates, or signal/course vendors by mistake.

## Principle

Never start from broad `keyword -> email` scraping for retail customers.

Start from:

```text
public customer comment/post intent -> handle/profile -> public contact source -> email review row
```

## Agent Sequence

```text
approval-gate-reporter
-> source-finder
-> engagement-collector
-> buyer-intent-scorer
-> seller-spam-filter
-> profile-enricher
-> website-contact-enricher
-> lead-normalizer
-> compliance-reviewer
-> approval-gate-reporter
```

## Allowed Sources

- Public YouTube comments and commenter channels.
- Public TikTok videos/comments and commenter profiles.
- Public Instagram profiles/posts/comments only when the actor supports public data without login.
- Public Facebook indexed pages/snippets only as review evidence, not final proof by itself.
- Public websites/link hubs discovered from a qualified customer profile.

## Rejection Rules

Reject before enrichment when evidence suggests:

```text
IB
affiliate
broker partner
signal provider
VIP seller
managed account
account recovery
copy my trades
DM me for signals
course seller
mentorship seller
creator/influencer outreach target
```

Operator/business rows may be kept only in a separate `operator_business` table when the approved offer bucket is AI Sales Agent or automation.

## Accepted Email Rules

A retained email row must include:

```text
email
email_source_url
email_source_field
source_platform
source_handle
customer_intent_evidence
offer_bucket
seller_or_operator_status
approval_status
```

Reject guessed/generated emails, private contact panel output, missing source URLs, and weak identity matches.

## Tiny Test Template

Prepare this approval packet before running any paid actor:

```yaml
approval_id: apify-social-customer-email-cross-platform-001
input_source: data/forex-social-intent/runs/20260922-190136/filtered_leads.csv
max_profiles: 4
budget_ceiling_usd: 0.05
actors:
  - public profile/channel enrichment for the platform
  - exact handle SERP probe only for qualified handles
  - website contact extractor only when public website/link exists
rules:
  - public data only
  - no login/cookies/private panels
  - no guessed emails
  - no validation at scale
  - no outreach
  - local CSV/Markdown only
```


## Approved Runner

After human approval for the YouTube exact-email packet, run:

```powershell
python agent-lead-scraper\run_youtube_retail_commenter_email.py --approved --approval "approve run youtube retail commenter exact email budget 0.05" --budget 0.05
```

The runner refuses to start without the exact approval phrase. It writes only local artifacts under `data/forex-social-intent/runs/<timestamp>-retail-commenter-email-exact/` and normalizes accepted/rejected rows with source attribution.
## Stop Conditions

Stop if:

- the next step spends money without approval;
- actor requires login/cookies/private panels;
- no public email/link/site exists;
- returned rows are mostly sellers/creators/IBs/affiliates;
- `email_source_url` or `customer_intent_evidence` is missing.