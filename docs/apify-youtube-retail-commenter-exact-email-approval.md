# Approval Packet: YouTube Retail Commenter Exact Email Test

Status: draft, not approved, do not run.
Date: 2026-09-22
Prepared by: Briantom Social Email Architect

## Goal

Test whether a slightly larger set of qualified YouTube retail commenters can produce sourced public emails when using exact profile/channel enrichment only.

This is not a creator, seller, IB, affiliate, or course-owner scrape.

## Budget

Budget ceiling: `$0.05`

Stop if projected or actual cost reaches the ceiling.

## Safety Rules

- Public data only.
- No login.
- No cookies.
- No private contact panels.
- No guessed/generated emails.
- No validation at scale.
- No outreach.
- No external export.
- Local CSV/Markdown artifacts only.
- Every retained email must include `email_source_url` and `email_source_field`.

## Input Source

Use existing qualified commenter evidence first:

```text
data/forex-social-intent/runs/20260922-190136/filtered_leads.csv
```

Candidate selection:

```text
seller_filter_status in QUALIFIED_CUSTOMER / retained customer review
max_profiles = 10
must have source_post_url + comment evidence + profile/channel URL or exact handle
```

Do not include:

- channel/video owner unless they are the commenter.
- seller, IB, affiliate, broker partner, signal provider, course seller.
- weak generic praise rows.

## Actor Sequence

### Step 1: Exact YouTube Channel/Profile Email Probe

Preferred actor:

```text
crawlerbros/youtube-email-scraper
```

Fallback actor:

```text
email_scraper/youtube-email-scraper
```

Exact input template:

```json
{
  "channelUrls": [
    "{{qualified_commenter_channel_url_1}}",
    "{{qualified_commenter_channel_url_2}}",
    "{{qualified_commenter_channel_url_3}}"
  ],
  "followExternalProfiles": true,
  "maxExternalPerChannel": 2,
  "autoProxyFallback": true
}
```

If selected actor schema does not support `channelUrls`, stop and fetch actor schema before running.

### Step 2: Exact SERP Fallback

Only run if Step 1 finds no sourced email and budget remains.

Actor:

```text
apify/google-search-scraper
```

Exact input template:

```json
{
  "queries": [
    "\"{{exact_channel_url}}\" email OR gmail",
    "\"{{exact_handle}}\" \"{{display_name}}\" email"
  ],
  "maxPagesPerQuery": 1,
  "resultsPerPage": 10,
  "languageCode": "en"
}
```

## Keep Criteria

Keep only if:

- email appears on a public page/snippet/profile/website.
- identity matches exact channel/profile/handle.
- `email_source_url` is public and recoverable.
- `email_source_field` is one of: `bio`, `about`, `website`, `contact_page`, `search_snippet`.
- comment evidence proves retail customer intent.

## Reject Criteria

Reject if:

- seller/IB/affiliate/creator/trainer page.
- Google redirect only and no recoverable source URL.
- email has no source field.
- identity match is weak.
- email appears generated, guessed, inferred, or validation-derived.
- actor requires login/private contact panel.

## Required Outputs

Write only under:

```text
data/forex-social-intent/runs/<timestamp>-retail-commenter-email-exact/
```

Files:

```text
actor_input.json
raw_items.json
enriched_profiles.csv
lead_candidates.csv
rejected_candidates.csv
batch_report.md
run_final.json
summary.json
```

## Expected Result

Retail commenter email yield is expected to be low. If this test returns zero sourced public emails from the selected qualified commenters, stop retail email extraction and use the commenter dataset for VOC/content while shifting email acquisition to operator/business website extraction.


## Schema Check

Checked on 2026-09-22 from Apify Store page for `crawlerbros/youtube-email-scraper`.

Supported input fields confirmed:

```text
channelUrls
followExternalProfiles
maxExternalPerChannel
autoProxyFallback
```

The actor page says it reads public YouTube About pages plus public Instagram/TikTok/Linktree profiles, does not need login/cookies/API key, and does not support click-to-reveal YouTube emails behind login gates. Output includes `emails` and `sources` with `sourceUrl` and `sourceType`.

## Local Verification

The approved runner and safety checks have local tests:

```powershell
python agent-lead-scraper\test_youtube_retail_commenter_email.py
```

Verified on 2026-09-22:

```text
Ran 5 tests
OK
```

The tests cover evidence mapping, seller-language rejection, safe word-boundary matching for IB/subscriber cases, and refusal to run without the exact approval phrase.
## Approval Needed

Run only if the human approves exactly:

```text
approve run youtube retail commenter exact email budget 0.05
```

## Exact Input File

Prepared exact local input:

```text
docs/apify-youtube-retail-commenter-exact-email-input.json
```

The file uses the 4 currently qualified YouTube customer commenters from the previous discovery/enrichment run:

```text
@judymugo6751
@AfrosterGerald
@MaxwellLouis-d5h
@ChartMe_Avi
```

Schema has been checked for `crawlerbros/youtube-email-scraper`; the prepared input uses the supported `channelUrls` field.
