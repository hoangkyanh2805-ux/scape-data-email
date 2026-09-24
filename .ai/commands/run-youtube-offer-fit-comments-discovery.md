# Command - Run YouTube Offer-Fit Comments Discovery

Use Hermes profile `scapedata`.

Goal:
Find public YouTube comments that show customer intent for the offer ladder before any email enrichment.

Skill:
Use `.codex/skills/youtube-offer-fit-comments-discovery/SKILL.md`.

Agent sequence:

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

Important:
Do not run any email scraper first.
Do not run any paid actor until the exact input and budget are approved.

Read:

```text
docs/offer-fit-lead-filter.md
docs/runbook-youtube-offer-fit-comments-discovery.md
.ai/agents/offer-fit-youtube-comments/youtube-comments-discovery.AGENT.md
```

Prepare an approval packet for a tiny public-data-only YouTube comments discovery test:

```yaml
platform: youtube
candidate_actor: hipersoft/youtube-scraper
candidate_actor_id: eQFDaaFKkTIe3fplv
source_queries:
  - xauusd beginner need help
  - forex funded challenge help
  - need forex signal which broker
max_queries: 3
max_videos_per_query: 5
max_comments_per_video: 25
email_enrichment: false
uses_login_or_session: false
uses_private_sources: false
outreach_enabled: false
external_export_enabled: false
storage_target: local_csv_markdown
```

Before running:

1. Fetch current actor details/schema/pricing.
2. Prepare exact input JSON.
3. Estimate cost and set budget ceiling.
4. Wait for human approval.

Expected outputs after an approved run:

```text
source_map.csv
post_table.csv
engagement_table.csv
intent_score_table.csv
filtered_leads.csv
batch_report.md
approval_packet.md
actor_runs.yaml
```
