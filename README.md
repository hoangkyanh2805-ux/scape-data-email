# scape-data

`scape-data` is a focused social-email data collection repo.

Its only goal is to collect reviewable public email/contact data from social platforms, starting with people who engage with Forex content. This repo is not a course project, not a CRM, not an outreach bot, not a Telegram gateway, and not a generic self-improving-agent template.

## Mission

Find people on social platforms who regularly engage with Forex content, especially comments and replies that show buyer, learner, funded-trader, prop-firm, XAUUSD, ICT, SMC, or trading-education intent. Then enrich only public profile/contact fields and prepare a local lead candidate dataset for human review.

Primary outcome:

```text
public social engagement -> buyer intent score -> seller/spam filter -> public email enrichment -> local candidate table
```

The repo prepares data. It does not send outreach, upload contacts, sell leads, run Telegram automation, or sync full emails to external tools without explicit human approval.

## Repo Identity

- Repo: `scape-data`
- Workspace: `G:\Other computers\My Computer\Project\scape-data`
- Hermes profile: `scapedata`
- Hermes project: `scape-data`
- Hermes project id: `p_8a6b3b15`
- Default gateway: Hermes Desktop Local gateway
- Default output: local CSV/Markdown artifacts

When Hermes or any agent reads this repo, it must use this identity only. Do not import context, tokens, customers, brands, courses, VPS settings, or Telegram gateways from older profiles or other repos.

## Scope

Allowed focus:

- Social data discovery for email collection.
- Public Forex content sources.
- Public comments, replies, and other engagement evidence.
- Public profile/bio/website/email fields.
- Apify actor research and approved actor runs.
- Local dedupe, scoring, filtering, and reporting.
- Hermes multi-agent orchestration for the data pipeline.

Out of scope:

- Course operations.
- Azzam, NCI, old Forex desk profiles, or old bot identities.
- Telegram gateway automation.
- WhatsApp automation.
- n8n scheduling in phase 1.
- Outreach email, DMs, SMS, or comment posting.
- CRM, ad audience, Google Sheets, Airtable, Drive, buyer, or Telegram export with full emails.
- Private groups, login-cookie scraping, or bypassing platform privacy controls.

## Default Runtime Flags

Every run starts with:

```yaml
research_only: true
public_data_only: true
outreach_enabled: false
external_export_enabled: false
max_cost_requires_approval: true
emails_redacted_in_reports: true
```

Any agent must stop if a requested action conflicts with these flags.

## Target Platforms

Phase 1 priority:

- TikTok public videos and comments.
- YouTube public videos/channels and comments.

Phase 2 only after a clean phase 1:

- Instagram public posts, comments, and profiles.
- X/Twitter public posts, replies, and profiles.
- Threads public posts and profiles.
- Facebook public pages only.
- Reddit public posts/comments only.

For Forex, do not start from sellers as leads. Start from posts/videos about Forex, then collect the people who comment or reply with intent.

## Apify Actor Shortlist

Fetch current Apify Store docs before any live run because actor schemas and pricing change.

Discovery and post collection:

```text
clockworks/tiktok-scraper
apidojo/tiktok-scraper
get-leads/all-in-one-tiktok-scraper
streamers/youtube-scraper
hipersoft/youtube-scraper
apify/instagram-scraper
apify/instagram-post-scraper
vortex_data/instagram-scraper
scrapers/twitter
scrapesmith/twitter-x-scraper-tweets-profiles-replies
atomus/twitter-scraper
webdata_labs/threads-scraper
lergassy/threads-scraper
```

Engagement collection:

```text
clockworks/tiktok-comments-scraper
get-leads/all-in-one-tiktok-scraper
simpleapi/youtube-comments-scraper
hipersoft/youtube-scraper
vortex_data/instagram-scraper
apify/instagram-comment-scraper
api-empire/twitter-x-reply-scraper
scrapesmith/twitter-x-scraper-tweets-profiles-replies
webdata_labs/threads-scraper
lergassy/threads-scraper
```

Public email/profile enrichment:

```text
apify/instagram-profile-scraper
instagram-scraper/instagram-profile-finder
vortex_data/instagram-scraper
clockworks/tiktok-scraper
email_scraper/tiktok-email-scraper
streamers/youtube-scraper
hipersoft/youtube-scraper
email_scraper/youtube-email-scraper
scrapers/twitter
email_scraper/x-twitter-email-scraper
webdata_labs/threads-scraper
lergassy/threads-scraper
apify/google-search-scraper
```

Actor rules:

- Use only public data modes.
- Do not use login cookies, session tokens, private communities, or evasion settings.
- Email must be visible in a public profile, public bio, public website, public page, or public search snippet.
- Do not infer, generate, guess, or validate emails at scale without approval.

## Hermes Multi-Agent Set

Canonical agent contracts live in:

```text
.ai/agents/forex-social-intent/
```

Install/use these 8 agents:

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

Runtime sequence:

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

The final agent, `approval-gate-reporter`, is mandatory. It blocks paid scale-up, external export, outreach, Telegram, CRM sync, and unclear contact-data handling.

## Core Workflow

1. Define niche keywords:

```text
XAUUSD, gold trading, Forex beginner, FTMO, funded trader, prop firm, ICT, SMC, price action
```

2. Find public posts/videos with active Forex engagement.
3. Collect comments and replies from approved public actors.
4. Score buyer/learner intent from the engagement text and profile context.
5. Filter sellers, brokers, IBs, spam, and unrelated users.
6. Enrich retained profiles only with public contact data.
7. Normalize into a candidate table.
8. Produce a local report and approval packet.
9. Stop before any outreach or external export.

## Output Artifacts

Default local path:

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

Main candidate fields:

```text
platform
handle
profile_url
source_post_url
engagement_text
intent_score
seller_filter_status
bio
website_url
public_email
email_source_url
email_source_field
confidence
status
review_reason
approval_status
```

Every retained email must include `email_source_url` and `email_source_field`.

## Approval Gates

Create an approval packet before any paid/live Apify run:

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

Stop before:

- paid actor runs beyond approved budget;
- high-volume liker/follower scraping;
- private or restricted communities;
- login/session/cookie-based scraping;
- email validation at scale;
- sending outreach;
- uploading full emails to CRM, Google Sheets, Airtable, Drive, ad tools, or Telegram;
- lead resale or transfer to a buyer;
- n8n schedule or Telegram gateway automation.

## Hermes Desktop Setup

Use a fresh Hermes Desktop session:

```text
profile: scapedata
project: scape-data
gateway: Local gateway
cwd: G:\Other computers\My Computer\Project\scape-data
```

Sanity prompt:

```text
Bạn đang ở profile nào, project nào, cwd nào? Chỉ trả lời profile/project/cwd.
```

Expected:

```text
profile: scapedata
project: scape-data
cwd: G:\Other computers\My Computer\Project\scape-data
```

If Hermes mentions courses, Azzam, NCI, old Telegram bots, old VPS profiles, or unrelated repos, stop the session and start again with the correct `scapedata` profile.

## Important Files

- `AGENTS.md`: repo guardrails and context boundary.
- docs/apify-active-actors.md: active Apify actor whitelist for this repo.
- docs/apify-instagram-comments-test-protocol.md: tiny safe test for Instagram Comments Scraper.
- `docs/apify-social-email-lead-sourcing.md`: Apify actor research and email sourcing playbook.
- `docs/forex-social-engagement-lead-research.md`: Forex engagement-first research map.
- `docs/runbook-forex-social-engagement-lead-batch.md`: main runbook for batch collection.
- `docs/audit-hermes-multi-agent-readiness.md`: readiness audit for Hermes multi-agent setup.
- `docs/self-improving-agent-os-agent-review.md`: guide-based review of the agent set against self-improving OS criteria.
- `knowledge/distilled/playbooks/question-first-social-demand-mining.md`: distilled guide for finding question-rich public sources before email enrichment.
- `knowledge/reusable-assets/prompts/hermes-question-first-social-demand-mining.prompt.md`: Hermes prompt for question-first sourcing batches.
- `.ai/commands/run-question-first-source-research.md`: command prompt for a tiny public-only source research batch.
- `.ai/agents/forex-social-intent/`: 8 canonical agent contracts.
- `.ai/agents/multi-agent-contracts.md`: multi-agent routing map.
- `.ai/rules/permission-matrix.md`: allowed, approval-required, and forbidden actions.
- `.ai/rules/human-approval-gates.md`: approval records and gates.
- `agent-lead-scraper/`: local Python prototype for Apify-backed collection workflows.

## Current Status

- Repo identity is `scape-data`.
- Hermes profile is `scapedata`.
- README now treats email data collection as the only project mission.
- 8 Hermes-ready agent contracts exist for the Forex social email pipeline.
- Dry-run/research mode is ready.
- Live Apify scraping still requires `APIFY_TOKEN`, actor approval packet, budget ceiling, batch size, and local storage confirmation.

## First Safe Run

Recommended MVP:

```text
Platforms: TikTok + YouTube
Source type: public Forex videos/posts
Engagement: public comments/replies only
Batch size: small
Output: local CSV/Markdown
Outreach: disabled
External export: disabled
Telegram/n8n: disabled
```

The first run should produce only:

```text
lead_candidates.csv
duplicate_report.csv
batch_report.md
approval_packet.md
```

After review, decide which platform and actor has the best public-email yield before scaling.




