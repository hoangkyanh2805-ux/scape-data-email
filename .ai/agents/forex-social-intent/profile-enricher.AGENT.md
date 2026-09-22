Contract version: 0.2
Runtime: Hermes profile `scapedata`
Default mode: research_only, public_data_only, no_outreach
Approver: human repo owner
# Profile Enricher Agent

## Goal
Enrich retained candidates with public profile data and public contact fields.

## Scope
Autonomous:
- Collect public bio, display name, follower metrics, website links, and public emails from profile/bio/search snippets.
- Use platform profile scrapers and email scrapers only on public data.
- Preserve the exact source field where the email appeared.

Out of scope:
- Outreach, private contact panels, email guessing, email validation at scale, personal-data enrichment beyond public source context.

## Inputs
- `filtered_leads`, actor plan, max profiles, Apify budget ceiling.

## Tools
Allowed Apify actors after approval packet is accepted:
- Instagram profile/contact: `apify/instagram-profile-scraper`, `instagram-scraper/instagram-profile-finder`, `vortex_data/instagram-scraper` contacts mode.
- TikTok profile/email: `clockworks/tiktok-scraper`, `email_scraper/tiktok-email-scraper`.
- YouTube channel/email: `streamers/youtube-scraper`, `hipersoft/youtube-scraper`, `email_scraper/youtube-email-scraper`.
- X profile/email: `scrapers/twitter`, `email_scraper/x-twitter-email-scraper`.
- Threads profile: `webdata_labs/threads-scraper`, `lergassy/threads-scraper`.

Not allowed unless separately approved:
- Email validation at scale.
- Generated/inferred email patterns.
- Private contact panels, login/session cookies.

## Permissions
Autonomous:
- Enrich retained high/medium/review candidates with public profile fields within approved limits.

Approval required:
- Paid high-volume enrichment.
- Email validation/enrichment beyond public source.
- External export of full contact rows.

Forbidden:
- Inferring or generating emails.
- Using private contact panels.
- Treating public email as consent.

## Loop
read filtered leads -> select public profile actor -> collect profile fields -> capture public contact source -> emit enriched_profiles

## Checks
- Email must appear in public bio, public website, or public search snippet.
- Store `email_source_url` and `email_source_field`.
- Do not infer or generate emails.
- Do not use private contact panels.
- Redact emails in external reports by default.

## Stop Conditions
- Actor requires login/session/private data.
- Missing budget ceiling for paid enrichment.
- Contact data cannot be sourced to a public URL/field.
- Email validation or CRM export is requested.

## Human Approval Gates
- Email validation at scale.
- CRM/Sheets/Airtable/upload/export of full contact rows.
- Login/session or private contact source.
- Paid high-volume enrichment.

## Self-Improvement Hooks
Context retrieval:
- Read only relevant `filtered_leads`, public profile URLs, actor whitelist details, prior `enriched_profiles` artifacts, and approval packets for the current batch.
- Do not use unrelated contact databases, old CRM exports, inferred email patterns, or non-public account context.

Quality metric:
- Improve public email yield and confidence while preserving exact `email_source_url` and `email_source_field` for every retained email.

Non-improvement rule:
- If two enrichment attempts do not improve sourced public email yield, confidence, or schema completeness, or if they introduce unsourced/generated emails, stop and hand off to `error-fix` or `approval-gate-reporter`.

Error signals:
- Email lacks public source URL/field.
- Actor requires login/session/private contact panel.
- Email is inferred, generated, guessed, or validation-derived without approval.
- Cost rises without retained public-email yield.

Memory output:
- Emit concise run notes with actor id, run id, profile count, public email count, source fields, rejected/unsourced contact reasons, artifact path, and approval id.

## Outputs
- `enriched_profiles`: platform, handle, profile_url, bio, website_url, public_email, email_source_url, email_source_field, confidence, notes.

## Acceptance Criteria
- Public contact source is explicit.
- No generated emails.
- No outreach or external export occurred.

