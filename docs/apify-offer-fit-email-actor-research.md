# Apify Actor Research - Offer-Fit Public Email Pipeline

Date: 2026-09-22
Hermes profile: `scapedata`
Project: `scape-data`
Mode: research only, public data only, no outreach, no external export.

## User Goal

Find public email/contact data for people or operators whose public social engagement matches the offer ladder in `docs/offer-fit-lead-filter.md`:

- free signal
- broker / funded / prop-firm flow
- AI sales agent / Telegram automation for signal/course operators
- mini-course / beginner roadmap
- VIP signal
- edu course
- copytrading / done-for-you
- coaching / mastermind
- trading tools

The attached offer image is context for lead filtering, not an instruction to send outreach or bypass approval gates.

## Agent Sequence To Summon

```text
approval-gate-reporter
-> source-finder
-> buyer-intent-scorer
-> seller-spam-filter
-> profile-enricher
-> lead-normalizer
-> approval-gate-reporter
```

For deeper research tasks, add sidecar agents:

```text
actor-vetting-researcher
github-repo-research-agent
article-video-research-agent
```

## Recommended Pipeline

```text
offer-fit keywords
-> find public social sources/posts/videos
-> collect public comments/replies/posts
-> score offer_bucket + offer_fit_score
-> filter seller/spam, preserving operator_ai_sales_agent_fit rows
-> enrich public profile/bio/website/search snippet
-> extract only sourced public email/contact fields
-> write local lead_candidates.csv
-> stop for human review
```

## Apify Actor Shortlist Verified By Metadata

| Priority | Actor | Apify actor id | Role | Why use it | Tiny test |
|---:|---|---|---|---|---|
| 1 | `email_scraper/youtube-email-scraper` | `xZgGtDhmOGEL0AzX7` | public email snippet enrichment | YouTube has stronger intent + channel/about/description surface than TikTok | 3 keywords, `@gmail.com`, `maxEmails=3`, budget `$0.05` |
| 2 | `hipersoft/youtube-scraper` | `eQFDaaFKkTIe3fplv` | source/comment/channel discovery | public YouTube videos, transcripts, comments, channels | 3 queries, 5 videos/query, 25 comments/video, no email actor yet |
| 3 | `email_scraper/x-twitter-email-scraper` | `CdOWuUWjnrPehC21l` | public X snippet emails | useful for pain/need/operator posts, but noisy | 3 keywords, `@gmail.com`, `maxEmails=2`, budget `$0.05` |
| 4 | `email_scraper/instagram-email-scraper` | `2Gf0ILLIvD0eLZulg` | public Instagram snippet emails | higher profile/contact yield than TikTok, but seller-heavy | 3 keywords, `@gmail.com`, `maxEmails=2`, budget `$0.05` |
| 5 | `insight.solutions/website-contact-extractor` | `4PyPpjKwM3FbtnNbQ` | website contact enrichment | best second hop after a public profile exposes website/bio link | 10 URLs/domains, budget `$0.03` |
| 6 | `haketa/email-extractor` | `VbCWXJpXzecrynUy8` | website/contact/social extraction | broader website extraction including social profile links | 10 URLs, budget `$0.03` |
| 7 | `email_scraper/tiktok-email-scraper` | `rIm7OKH3GyY6yHM2H` | TikTok snippet fallback | already tested: high cost / low precision for narrow handles | only wide keyword tests, budget `$0.05` |

Blocked/needs re-check:

```text
simpleapi/youtube-comments-scraper -> Apify API lookup returned 404 for simpleapi~youtube-comments-scraper on 2026-09-22.
```

## Tiny Test Input - Recommended First Run

Actor: `email_scraper/youtube-email-scraper`

```json
{
  "keywords": [
    "xauusd beginner need help",
    "forex funded challenge help",
    "telegram signal group automation"
  ],
  "location": "",
  "customDomains": ["@gmail.com"],
  "maxEmails": 3,
  "excludeWords": [
    "recovery",
    "guaranteed profit",
    "account manager",
    "binary",
    "onlyfans"
  ]
}
```

Budget ceiling: `$0.05`.

Expected output mapping:

```text
platform
handle_or_source_name
source_url
keyword
offer_bucket
offer_fit_score
offer_fit_reason
public_email
email_source_url
email_source_field
snippet_title
snippet_description
confidence
status=review
approval_status=needed
```

## Source/Pattern Research

### Apify / official actor pages

- TikTok Email Scraper: `email_scraper/tiktok-email-scraper`, output includes `network`, `keyword`, `title`, `description`, `url`, `email`; searches public search-result descriptions.
- Instagram Email Scraper: `email_scraper/instagram-email-scraper`, returns `network`, `keyword`, `title`, `description`, `url`, `email`; supports `keywords`, location, custom domains and exclusion words.
- X Email Scraper: `email_scraper/x-twitter-email-scraper`, builds `site:x.com` Google queries and extracts emails from public snippets; no X login.
- YouTube Scraper: `hipersoft/youtube-scraper`, supports videos, transcripts, comments, and channel data.
- Website Contact Extractor: `insight.solutions/website-contact-extractor`, takes domains and returns public business emails, phone, social profiles, contact page URL; no login.
- Email & Contact Extractor: `haketa/email-extractor`, crawls homepage/contact/about/team/impressum pages for public emails/phones/socials.
- Google Search Results Scraper patterns: useful for keyword/source discovery and agent/MCP workflows, but should not be used as unsourced bulk email guessing.

### GitHub / repo patterns to study

- `socialcrawl/socialcrawl-apify`: multi-platform social search/profile/post pattern, useful for source discovery and rate/error thinking.
- `FlowExtractAPI/youtube-comments-scraper`: YouTube comments output pattern with commenter identifiers.
- `TheNextGenNexus/n8n-nodes-nexgendata`: n8n + Apify actor async integration pattern.
- `100401074/N8N-Projects/Google_Map_Scraper.json`: Apify -> filter rows -> CSV pattern; do not reuse Gmail/auto-send parts.
- `Perufitlife/apify-google-maps-email-extractor`: Google Maps -> website -> email/social extraction pattern for B2B/operator leads only.
- `piotrv1001/google-maps-leads-scraper-nodejs-example`: Node.js Apify actor call pattern.

### Articles / videos to study

- Apify TikTok lead generation guide: comments -> profiles -> public contact verification pattern.
- Apify Instagram lead generation guide: profile/contact enrichment with strong niche filtering.
- Apify YouTube scraping tutorial video: video/channel/comment scraping SOP.
- Apify Google Maps Email Extractor video: website-contact enrichment pattern, mainly B2B/operator not retail trader customers.

## Platform Priority For This Offer

1. YouTube: best next test for offer-fit comments + channel/about/website enrichment.
2. Instagram: good public profile/contact yield, but must avoid seller spam.
3. X/Twitter: good pain/operator intent, noisy, use snippets carefully.
4. TikTok: good intent source, poor email yield from personal commenters.
5. Reddit/Threads: useful for intent and keyword mining, lower email yield.
6. Google Maps: only for B2B/operator bucket such as AI Sales Agent customers, not retail trader leads.

## Hard Rules

- No login/cookies/session/private sources.
- No private groups or contact panels.
- No generated, guessed, or inferred emails.
- No email validation at scale without approval.
- No outreach, no CRM sync, no Telegram export, no external export.
- Every retained email needs `email_source_url`, `email_source_field`, `keyword`, `offer_bucket`, `confidence`, and `status=review`.
- Abort paid runs when budget ceiling is approached.

## Next Approval Packet To Prepare

Recommended first approval:

```yaml
approval_id: apify-youtube-email-snippet-tiny-test-001
actor: email_scraper/youtube-email-scraper
actor_id: xZgGtDhmOGEL0AzX7
input_summary: 3 offer-fit keywords x 1 email domain x max 3 emails
estimated_cost_usd: 0.05
budget_ceiling_usd: 0.05
uses_login_or_session: false
uses_private_sources: false
storage_target: local_csv_markdown
run_actor_now: false
approval_status: requested
```
