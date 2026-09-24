---
name: youtube-offer-fit-comments-discovery
description: Run approval-gated YouTube public comments discovery for offer-fit lead intent before any email enrichment; use for scape-data social-email workflows where keyword-to-email scraping risks returning sellers, IBs, affiliates, or creators instead of customers.
---

# YouTube Offer-Fit Comments Discovery

Use this skill when the task is to find potential customers for the scape-data offer ladder by collecting and scoring public YouTube comments before public email enrichment.

Do not use this skill to run keyword-to-email scraping directly. The known failure mode is `keyword -> email scraper -> seller/creator/affiliate emails`. This skill enforces the safer sequence:

```text
offer context -> YouTube source discovery -> public comments -> offer-fit scoring -> seller/operator filter -> selected commenter/channel enrichment -> local lead table -> approval gate
```

## Required Context

Read these before acting:

1. `docs/offer-fit-lead-filter.md` for the offer buckets and customer/seller distinction.
2. `docs/runbook-forex-social-engagement-lead-batch.md` for repo gates and output schemas.
3. `references/workflow.md` for the YouTube comments discovery workflow.
4. `references/self-improvement.md` when creating or updating prompts, commands, runbooks, or agent contracts.

## Default Agents

Use or prepare this sequence:

```text
approval-gate-reporter
-> source-finder
-> post-collector
-> engagement-collector
-> buyer-intent-scorer
-> seller-spam-filter
-> profile-enricher
-> lead-normalizer
-> approval-gate-reporter
```

For this skill, `profile-enricher` must only run after comments are scored and filtered.

## Hard Rules

- Public YouTube data only.
- No login, cookies, private communities, or contact panels.
- Do not run email actors before comments/replies are scored.
- Do not treat creator emails as customer leads unless the row fits `operator_ai_sales_agent_fit` with explicit automation pain.
- Do not infer, generate, guess, or validate emails at scale.
- No outreach, no CRM sync, no Google Sheets/Airtable/Telegram export, no lead transfer.
- Every paid Apify run requires an approval packet with exact input and budget ceiling.
- Every retained email must include `email_source_url`, `email_source_field`, `offer_bucket`, `offer_fit_reason`, `confidence`, and `status=review`.

## Autonomous Work Allowed

- Draft search keywords and source maps.
- Prepare exact actor inputs and approval packets.
- Normalize local CSV/Markdown artifacts from already approved runs.
- Score comments with evidence phrases.
- Produce self-improvement notes and suggested prompt fixes.

## Stop Before

- Running any paid/live actor without approval.
- Increasing batch size or budget.
- Enriching email before a row has comment-based offer-fit evidence.
- Exporting contacts outside the local repo.
- Contacting any person.

## Tiny Test Shape

Recommended first live test after approval:

```yaml
platform: youtube
source_queries:
  - "xauusd beginner need help"
  - "forex funded challenge help"
  - "need forex signal which broker"
max_queries: 3
max_videos_per_query: 5
max_comments_per_video: 25
email_enrichment: false
output: local_csv_markdown
budget_ceiling_usd: requested_before_run
```

After the comment batch is reviewed, prepare a second approval packet only for retained rows:

```text
retained high/medium offer-fit commenters/channels -> public channel/about/bio/website enrichment -> website contact extractor if public link exists
```

## Acceptance Criteria

A completed discovery packet must include:

- `source_map.csv`
- `post_table.csv`
- `engagement_table.csv`
- `intent_score_table.csv` with `offer_bucket`, `offer_fit_score`, and `evidence_phrase`
- `filtered_leads.csv`
- `batch_report.md`
- `approval_packet.md`
- `actor_runs.yaml` when a live actor was run

The batch is successful only if it separates customer intent from seller/affiliate/creator supply.
