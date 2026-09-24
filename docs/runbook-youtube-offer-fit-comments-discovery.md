# Runbook - YouTube Offer-Fit Comments Discovery

## Goal

Find public YouTube comments that show customer intent for the offer ladder before any public email/contact enrichment.

This runbook replaces the failed direct keyword-to-email flow for discovery work.

## Required Files

- `docs/offer-fit-lead-filter.md`
- `.codex/skills/youtube-offer-fit-comments-discovery/SKILL.md`
- `.ai/agents/offer-fit-youtube-comments/youtube-comments-discovery.AGENT.md`

## Agent Sequence

```text
approval-gate-reporter
-> source-finder
-> post-collector
-> engagement-collector
-> buyer-intent-scorer
-> seller-spam-filter
-> lead-normalizer
-> approval-gate-reporter
```

`profile-enricher` is intentionally excluded until `filtered_leads.csv` exists.

## Approval Packet Shape

```yaml
approval_id:
platform: youtube
actor_id:
actor_url:
input_summary:
source_queries:
max_queries:
max_videos_per_query:
max_comments_per_video:
email_enrichment: false
estimated_cost_usd:
budget_ceiling_usd:
uses_login_or_session: false
uses_private_sources: false
storage_target: local_csv_markdown
rollback_or_stop_plan:
approval_status: requested
```

## First Tiny Test Candidate

Do not run until approved.

```yaml
source_queries:
  - xauusd beginner need help
  - forex funded challenge help
  - need forex signal which broker
max_queries: 3
max_videos_per_query: 5
max_comments_per_video: 25
email_enrichment: false
```

Candidate actor to inspect before run:

```text
hipersoft/youtube-scraper
Apify actor id: eQFDaaFKkTIe3fplv
```

## Output Tables

### source_map.csv

```text
platform,source_query,offer_bucket,source_url,source_type,buyer_quality,activity_status,notes
```

### post_table.csv

```text
platform,source_query,offer_bucket,video_url,video_title,channel_name,channel_url,metrics,posted_at,actor_id,run_id
```

### engagement_table.csv

```text
platform,video_url,user_handle,channel_or_profile_url,comment_text,likes,replies,collected_at,actor_id,run_id
```

### intent_score_table.csv

```text
user_handle,channel_or_profile_url,platform,score,intent_level,offer_bucket,offer_fit_score,offer_fit_reason,evidence_phrase,source_video_url,review_reason
```

### filtered_leads.csv

```text
user_handle,platform,channel_or_profile_url,source_video_url,engagement_text,offer_bucket,seller_filter_status,filter_reason,retained_for_enrichment,evidence
```

## Review Labels

```text
qualified_customer_candidate
operator_ai_sales_agent_fit
seller_affiliate_creator_reject
spam_scam_reject
not_enough_evidence_review
```

## Stop Gates

Stop before:

- paid actor run without approval;
- collecting email before comment scoring;
- using login/cookies/private sources;
- exporting contacts externally;
- outreach or Telegram automation.

## Batch Report Must Include

```text
actor_id
run_id
dataset_id
actual_cost_usd
source_queries
video_count
comment_count
qualified_customer_candidate_count
operator_ai_sales_agent_fit_count
seller_affiliate_creator_reject_count
not_enough_evidence_review_count
next_recommended_enrichment_scope
approval_needed
```
