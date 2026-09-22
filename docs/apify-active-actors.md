# Active Apify Actors - scape-data

Date: 2026-09-21
Repo: `scape-data`
Purpose: lock the project to the Apify actors that actually work in the user's Apify Console.

## Active Actor Whitelist

Only these actors are considered active for live/dry-run setup right now:

```text
BDec00yAmCm1QbMEI
SbK00X0JYCPblD2wp
```

Console input pages:

```text
https://console.apify.com/actors/BDec00yAmCm1QbMEI/input?addFromActorId=BDec00yAmCm1QbMEI
https://console.apify.com/actors/SbK00X0JYCPblD2wp/input?addFromActorId=SbK00X0JYCPblD2wp
```

All other Apify Store actors mentioned in older research docs are reference candidates only. Do not run them unless the user confirms they work in the Apify Console and approves adding them to this whitelist.

## Required Inspection Before Use

Before either actor can be used in a run, Hermes must record:

```yaml
actor_id:
actor_name:
actor_console_url:
role:
  one_of:
    - source_or_post_collector
    - engagement_collector
    - profile_email_enricher
    - all_in_one_social_scraper
input_schema_summary:
required_inputs:
output_fields:
email_fields_available:
public_source_fields_available:
needs_login_or_cookie: false
uses_private_sources: false
pricing_or_cost_note:
last_test_status:
```

If the actor needs login/session cookies, private sources, or cannot preserve public source evidence, it must not be used for this repo.

## Runtime Rule

For now, every approval packet must use one of the two active actor IDs above.

```yaml
allowed_actor_ids:
  - BDec00yAmCm1QbMEI
  - SbK00X0JYCPblD2wp
```

Any other actor ID is blocked by default.

## How The Two Actors Fit The Pipeline

Because the current links are Console input links, this repo should not assume the actor role until the input/output schema is inspected.

Map each actor into one of these slots:

```text
source-finder/post-collector      -> actor that finds or collects public social posts/profiles
engagement-collector              -> actor that collects commenters/repliers/engagers
profile-enricher                  -> actor that returns public profile/contact/email fields
lead-normalizer                   -> normalizes output from both actors
approval-gate-reporter            -> reports cost/yield/risk and stops before export/outreach
```

If one actor is all-in-one, use it as the collection/enrichment actor but still split the output through the 8-agent review pipeline.

## Minimal First Test

Run only a tiny test after approval:

```yaml
max_sources: 3
max_posts: 5
max_comments_per_post: 50
max_profiles_to_enrich: 50
storage_target: local_csv_markdown
outreach_enabled: false
external_export_enabled: false
```

Required local outputs:

```text
data/forex-social-intent/runs/<YYYYMMDD-HHMM>/actor_runs.yaml
data/forex-social-intent/runs/<YYYYMMDD-HHMM>/lead_candidates.csv
data/forex-social-intent/runs/<YYYYMMDD-HHMM>/batch_report.md
data/forex-social-intent/runs/<YYYYMMDD-HHMM>/approval_packet.md
```

## Acceptance Checks

- Actor ID is one of the two active IDs.
- Actor input is saved in the approval packet.
- Actor run ID and dataset ID are saved after the run.
- Every email has source URL/field or is marked `review`/`rejected`.
- No external export, outreach, Telegram, CRM, Sheets, or n8n action occurs.
