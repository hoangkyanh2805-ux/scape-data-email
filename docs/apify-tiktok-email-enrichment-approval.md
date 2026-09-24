# Approval Packet - TikTok Public Email Enrichment Tiny Test

approval_id: `apify-tiktok-email-enrichment-001`

## Hermes / Agent Routing

- Hermes profile: `scapedata`
- Hermes project: `scape-data`
- Agent sequence: `approval-gate-reporter -> profile-enricher -> lead-normalizer -> approval-gate-reporter`

## Proposed Actor

- Actor: `email_scraper/tiktok-email-scraper`
- Actor id: `rIm7OKH3GyY6yHM2H`
- Actor URL: `https://apify.com/email_scraper/tiktok-email-scraper`
- Role: `profile_email_enricher`
- Whitelist status: not currently in `docs/apify-active-actors.md`; approval should allow this actor for this tiny test only.

## Input Source

Use the 25 TikTok commenter handles from:

```text
data/forex-social-intent/runs/20260922-132058/lead_candidates.csv
```

Source video:

```text
https://www.tiktok.com/@blissdgl_/video/7610602955712089366
```

## Exact Actor Input

```json
{
  "keywords": [
    "site:tiktok.com/@peakgentlegust peakgentlegust email",
    "site:tiktok.com/@s550.edi s550.edi email",
    "site:tiktok.com/@chipa_mvero chipa_mvero email",
    "site:tiktok.com/@vetgi0p vetgi0p email",
    "site:tiktok.com/@independent_kay independent_kay email",
    "site:tiktok.com/@graceshockleee graceshockleee email",
    "site:tiktok.com/@priska.graf priska.graf email",
    "site:tiktok.com/@victoria.noah8 victoria.noah8 email",
    "site:tiktok.com/@whitetoelover40 whitetoelover40 email",
    "site:tiktok.com/@toofreshrivers toofreshrivers email",
    "site:tiktok.com/@iyogobeads iyogobeads email",
    "site:tiktok.com/@shafiqa533 shafiqa533 email",
    "site:tiktok.com/@raynvibes0 raynvibes0 email",
    "site:tiktok.com/@kingdonlesch kingdonlesch email",
    "site:tiktok.com/@dirt_riderr dirt_riderr email",
    "site:tiktok.com/@josephsly7 josephsly7 email",
    "site:tiktok.com/@katelynbrumley14 katelynbrumley14 email",
    "site:tiktok.com/@user4872828351344 user4872828351344 email",
    "site:tiktok.com/@movieverse148 movieverse148 email",
    "site:tiktok.com/@gallo_025 gallo_025 email",
    "site:tiktok.com/@mavens_mind mavens_mind email",
    "site:tiktok.com/@twinglocks.s twinglocks.s email",
    "site:tiktok.com/@tanaville_scooby tanaville_scooby email",
    "site:tiktok.com/@11.22.6300 11.22.6300 email",
    "site:tiktok.com/@akeethagleaton akeethagleaton email"
  ],
  "location": "",
  "customDomains": [
    "@gmail.com",
    "@outlook.com",
    "@hotmail.com",
    "@icloud.com",
    "@yahoo.com"
  ],
  "maxEmails": 1,
  "excludeWords": [
    "jobs",
    "hiring",
    "template",
    "generator",
    "fake email",
    "example.com"
  ]
}
```

## Current Schema Summary

Based on the Apify Store page checked on 2026-09-22:

- Required field: `keywords`
- Optional fields: `location`, `customDomains`, `maxEmails`, `excludeWords`
- Expected output fields: `network`, `keyword`, `title`, `description`, `url`, `email`
- The actor searches public search-result descriptions associated with TikTok results.

## Cost Estimate

- Listed price: from `$1.49 / 1,000 results`
- Max configured combinations: `25 keywords x 5 domains x 1 maxEmails = 125 possible email records`
- Estimated actor-result cost if it fills the full cap: `125 / 1000 x 1.49 = $0.18625`
- Budget ceiling for this tiny test: `$0.25`

Actual cost may vary by Apify account plan, actor start/runtime events, and whether fewer matching emails are found.

## Safety Rules

- Public data only.
- No login or cookies.
- No private contact panels.
- No generated, inferred, or guessed emails.
- No email validation at scale.
- No outreach.
- No external export.
- Write only local CSV/Markdown artifacts.
- Every retained email must include `email_source_url`, `email_source_field`, `keyword`, and source handle/profile URL.

## Planned Local Outputs

If approved and run, write under a new local run directory:

```text
data/forex-social-intent/runs/<YYYYMMDD-HHMMSS>/
```

Expected artifacts:

```text
tiktok_email_scraper_raw.json
enriched_profiles.csv
lead_candidates_email_enriched.csv
duplicate_report.csv
batch_report.md
approval_packet.md
actor_runs.yaml
```

## Stop Plan

Stop immediately if:

- actor asks for cookies, login, session, or private source access;
- run cost approaches `$0.25`;
- output emails have no public `url` / `description` source evidence;
- output is not tied back to one of the 25 source handles;
- any step would export contacts or contact a person.

## Approval Status

```yaml
approval_status: requested
run_actor_now: false
human_approval_required: true
```

To approve the paid actor test, reply:

```text
duyet chay tiktok email scraper 25 handles budget 0.25
```
