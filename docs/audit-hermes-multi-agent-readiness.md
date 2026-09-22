# Hermes Multi-Agent Readiness Audit - Forex Social Intent

Date: 2026-09-21
Repo: `scape-data`
Hermes profile: `scapedata`
Scope: review agent contracts and readiness for Hermes multi-agent setup.

## Verdict

Draft/dry-run ready: yes.
Live scraping ready: not until Apify token, actor run approval packet, budget ceiling, storage target, and fresh Hermes Desktop session are confirmed.

Do not run outreach, Telegram gateway automation, CRM sync, email export, private group scraping, login-cookie scraping, or n8n scheduling yet.

## Reviewers

- Agent Contract Reviewer: checked agent contract completeness and routing readiness.
- Safety & Compliance Reviewer: checked privacy/contact data, Apify cost/quota, export gates, public-only rules.
- Hermes Deployment Reviewer: checked profile/routing/gateway readiness and install steps.

## Findings Before Patch

- 8 Forex agents existed but were too human-readable, missing runtime-readable fields: Tools, Permissions, Loop, Checks, Stop Conditions, Human Approval Gates, Acceptance Criteria.
- Actor whitelist was not explicit enough.
- Buyer intent scoring lacked numeric scale.
- Profile enrichment needed clearer public-email rules.
- Runbook lacked batch artifact paths and actor run metadata schema.
- Permission gates lacked explicit Apify run, contact export, retention/redaction, and email validation gates.
- Multi-agent summary did not map the 8 Forex agents.
- Hermes Desktop remains global-state sensitive; old sessions can retain old course/project context.

## Patches Applied

- Standardized all 8 contracts in `.ai/agents/forex-social-intent/` with runtime fields.
- Added candidate Apify actor whitelists and forbidden actor classes.
- Added numeric buyer-intent scoring scale.
- Added public email source checks and no-generated-email rule.
- Rewrote `docs/runbook-forex-social-engagement-lead-batch.md` with:
  - default research-only flags;
  - Apify run approval packet;
  - batch artifact directory;
  - actor_runs.yaml schema;
  - retention/redaction rules;
  - acceptance criteria.
- Added Forex pipeline map to `.ai/agents/multi-agent-contracts.md`.
- Updated `.ai/rules/permission-matrix.md` with Apify/contact data/export rules.
- Updated `.ai/rules/human-approval-gates.md` with Apify run and contact export approval records.

## Canonical Agent List

```text
source-finder
post-collector
engagement-collector
buyer-intent-scorer
seller-spam-filter
profile-enricher
lead-normalizer
approval-gate-reporter
```

Canonical folder:

```text
.ai/agents/forex-social-intent/
```

## Hermes Setup Checklist

1. Open Hermes Desktop.
2. Select profile `scapedata`.
3. Select Local gateway.
4. Select project/workspace `scape-data`.
5. Create a new session.
6. Sanity prompt:

```text
Bạn đang ở profile nào, project nào, cwd nào? Chỉ trả lời profile/project/cwd.
```

Expected:

```text
profile: scapedata
project: scape-data
cwd: G:\Other computers\My Computer\Project\scape-data
```

7. Instruct Hermes orchestrator to read:
   - `AGENTS.md`
   - `README.md`
   - `.ai/agents/multi-agent-contracts.md`
   - `.ai/rules/permission-matrix.md`
   - `.ai/rules/human-approval-gates.md`
   - `docs/runbook-forex-social-engagement-lead-batch.md`

## Required Before First Live Apify Batch

- APIFY_TOKEN available to the runtime, without exposing it in repo.
- Approved actor run packet.
- Budget ceiling in USD.
- Batch size: max videos/posts and max comments per post.
- Storage target: local CSV/Markdown for MVP.
- Platforms: TikTok + YouTube recommended first.
- No Telegram gateway, no n8n schedule, no external export.

## Default Runtime Flags

```yaml
research_only: true
public_data_only: true
outreach_enabled: false
external_export_enabled: false
max_cost_requires_approval: true
emails_redacted_in_reports: true
```

## What Not To Run Yet

```text
Telegram gateway
Telegram test message
outreach email/DM
CRM upload
Google Sheets/Airtable sync with full emails
lead resale/export to buyer
paid Apify high-volume batch
login-cookie scraping
private group scraping
n8n scheduled automation
SSH/VPS gateway
```

## First Safe Dry Run

Use no live Apify if token/budget is not approved. Create mock artifacts under:

```text
data/forex-social-intent/runs/<YYYYMMDD-HHMM>/
```

Then verify:

- every candidate has source post evidence;
- every score has evidence phrase;
- seller/spam rows are retained with rejection/review reason;
- emails are redacted in reports;
- no external action happened.

## Acceptance For Hermes Multi-Agent Install

Pass when:

- all 8 contracts are present;
- orchestrator can list the sequence correctly;
- approval-gate-reporter is the final gate;
- runbook artifact paths are known;
- permission matrix blocks outreach/export/private/login/high-volume actions;
- Desktop sanity check returns `scapedata / scape-data / repo cwd`.
