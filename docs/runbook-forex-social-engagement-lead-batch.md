# Runbook - Forex Social Engagement Lead Batch

## Goal
Find people who engage with Forex/trading content and show intent that fits the user-provided offer ladder, then prepare a reviewable lead candidate table with public evidence.

The offer context is captured in `docs/offer-fit-lead-filter.md`. It expands the target beyond beginner learners to include prospects for free signals, broker/funding flows, AI sales automation, mini-course, VIP signals, edu course, copytrading/done-for-you, coaching, and trading tools.

Default mode:

```yaml
research_only: true
public_data_only: true
outreach_enabled: false
external_export_enabled: false
max_cost_requires_approval: true
emails_redacted_in_reports: true
```

## Agent Sequence

```text
source-finder
-> post-collector
-> engagement-collector
-> buyer-intent-scorer
-> seller-spam-filter
-> profile-enricher
-> lead-normalizer
-> approval-gate-reporter
```

Canonical contracts live in `.ai/agents/forex-social-intent/`.

## Required Inputs

- Platforms to test: start with TikTok and YouTube.
- Offer-fit terms: XAUUSD, gold trading, Forex beginner, signal, VIP signal, free signal, broker, FTMO, funded trader, prop firm, ICT, SMC, price action, copytrading, mentorship, course, trading tools, Telegram sales automation, signal group automation.
- Geography/language if any.
- Apify budget ceiling.
- Batch size: posts/videos and comments per post.
- Storage target: default local CSV/Markdown.

## Apify Run Approval Packet

Before any paid or live Apify run, create this packet:

```yaml
approval_id:
platform:
actor_id:
actor_url:
input_summary:
max_sources:
max_posts:
max_comments_per_post:
max_profiles_to_enrich:
estimated_cost_usd:
budget_ceiling_usd:
uses_login_or_session: false
uses_private_sources: false
storage_target:
rollback_or_stop_plan:
approval_status: requested
```

No actor may run beyond the approved ceiling. Any run needing cookies, auth tokens, private communities, or proxy/fingerprint evasion must stop.


## Active Actor Whitelist

Use only the actors confirmed working in the user's Apify Console unless the user explicitly approves another actor:

```text
BDec00yAmCm1QbMEI
SbK00X0JYCPblD2wp
```

See `docs/apify-active-actors.md`.

Older actor names in research docs are reference candidates only. They are blocked for live/dry-run setup until confirmed working and added to the active whitelist.
## Apify Actor Plan

MVP:

- TikTok comments actor for public video comments.
- TikTok profile actor for retained commenters.
- YouTube comments actor with optional commenter enrichment.
- YouTube channel/profile/email actor for retained commenters where relevant.

Candidate actor ids in older docs are reference-only. For live/dry-run setup, use only the active actor whitelist in `docs/apify-active-actors.md` unless the user approves adding another actor. Fetch current input/output schema before any live run because actor schemas and pricing can change.

Secondary:

- Instagram post/comment/profile actor.
- X reply scraper and X profile/email scraper.
- Threads scraper.
- Facebook/Reddit public-only comment sources.

## Batch Artifacts

Default local artifact path:

```text
data/forex-social-intent/runs/<YYYYMMDD-HHMM>/
```

Required artifacts:

```text
source_map.csv
post_table.csv
engagement_table.csv
intent_score_table.csv
filtered_leads.csv
enriched_profiles.csv
lead_candidates.csv
duplicate_report.csv
actor_runs.yaml
batch_report.md
approval_packet.md
```

`actor_runs.yaml` fields:

```yaml
- platform:
  actor_id:
  run_id:
  dataset_id:
  input_summary:
  max_items:
  estimated_cost_usd:
  actual_cost_usd:
  started_at:
  finished_at:
  item_count:
  quota_warning:
  status:
```

## Output Tables

### source_map
platform, source_url, source_type, topic, activity_status, buyer_quality, notes

### post_table
platform, source_url, post_url, author, text, hashtags, metrics, posted_at, actor_id, run_id

### engagement_table
platform, post_url, user_handle, profile_url, engagement_type, text, likes, replied_to, collected_at, actor_id, run_id

### intent_score_table
user_handle, profile_url, platform, score, intent_level, offer_bucket, offer_fit_score, offer_fit_reason, evidence_phrase, source_post_url, review_reason

### enriched_profiles
platform, handle, profile_url, bio, website_url, public_email, email_source_url, email_source_field, confidence, notes

### lead_candidates
platform, handle, profile_url, source_post_url, engagement_text, intent_score, offer_bucket, offer_fit_score, offer_fit_reason, seller_filter_status, bio, website_url, public_email, email_source_url, email_source_field, confidence, status, review_reason, approval_status

## Stop Gates

Stop before:

- running paid actors beyond approved cost;
- using login/session cookies;
- scraping private/restricted communities;
- high-volume likers/followers collection;
- validating/enriching emails at scale;
- sending any outreach;
- uploading emails to CRM/ad/email platforms;
- exporting full contact rows to Google Sheets, Airtable, Telegram, Drive, buyer, or any external system;
- selling or transferring lead details.

## Retention And Redaction

- Keep raw engagement only in local run artifacts unless external export is approved.
- Reports intended for Telegram or any external channel must redact emails by default.
- Rejected/duplicate rows are retained for audit but must not be used for outreach.
- Do not store inferred sensitive traits.

## Acceptance Criteria

- Every lead candidate has a source post and engagement evidence.
- Seller/spam rows are filtered or marked review, never silently deleted.
- Public email source is explicit when present.
- No row is marked approved for outreach without human approval.
- Batch report includes actor_id, run_id, dataset_id, cost, item count, duplicate rate, confidence split, and next safe action.
- Public-only check passes: no private group, login-only panel, session cookie, or evasion setup.
- Offer-fit score has evidence phrase and is not based only on like/follow.



