# Briantom Next Customer Email Approval Packet

Date: 2026-09-22
Status: draft, waiting for human approval before any paid run

## Why This Packet Exists

Previous tests found real customer-intent commenters but no public emails on those exact personal profiles. A direct Facebook keyword-to-email test returned emails, but both were seller/training-side and were rejected.

So the next test should not run broad email scraping. It should first collect more public customer-intent commenters, then enrich only retained handles.

## Proposed Tiny Test

```yaml
approval_id: apify-customer-intent-comment-discovery-002
goal: Find more retail customer social handles with explicit Forex/XAUUSD/prop-firm pain before any email enrichment.
platform: YouTube first, TikTok second if budget remains
max_videos: 6
max_comments_per_video: 50
max_retained_customer_handles: 20
budget_ceiling_usd: 0.10
no_email_actor_in_this_step: true
rules:
  - public data only
  - no login/cookies/private groups/contact panels
  - no outreach
  - no external export
  - reject creator/seller/IB/affiliate rows before enrichment
success_metric:
  - at least 10 retained customer handles
  - seller false positives below 10 percent after review
outputs:
  - source_map.csv
  - engagement_table.csv
  - intent_score_table.csv
  - retained_for_enrichment.csv
  - seller_rejects.csv
  - batch_report.md
```

## Follow-Up Enrichment Gate

Only after retained handles exist:

```yaml
approval_id: apify-public-profile-email-enrichment-002
goal: Enrich public emails only for retained customer handles.
max_profiles: 20
budget_ceiling_usd: 0.05
allowed_actors:
  - public YouTube/TikTok/Instagram profile scraper for bio/about/link
  - exact handle SERP probe
  - website contact extractor only when profile exposes website/link hub
rules:
  - every email needs email_source_url and email_source_field
  - no guessed/generated emails
  - no validation at scale
  - no outreach/export
success_metric:
  - accepted customer email rows with direct public source URLs
```

## Recommended Approval Text

To run discovery only:

```text
approve run customer-intent comment discovery budget 0.10
```

To run enrichment later, after discovery output is reviewed:

```text
approve run public profile email enrichment budget 0.05
```