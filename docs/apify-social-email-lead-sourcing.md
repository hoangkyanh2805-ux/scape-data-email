# Apify Social Email Lead Sourcing Playbook

## Purpose

Design a safe, reviewable workflow for discovering public social contacts and business emails from social platforms using Apify Store actors.

This is a sourcing and research workflow only. It does not approve sending email, DMs, SMS, outreach, ads, or lead resale.

## Safety Boundary

Allowed in draft/research mode:

- collect public profile/post/search-result data within approved Apify quotas;
- extract public business/contact emails that are visibly surfaced in bios, pages, websites, or search-result snippets;
- keep source URL, keyword, platform, date, and confidence for every email;
- dedupe, score, and mark rows for human review.

Stop for approval before:

- paid high-volume runs without a cost ceiling;
- accessing private/restricted communities;
- using login cookies or session tokens;
- sending outreach or uploading emails to any ad/email platform;
- enriching personal data beyond public source context;
- selling, sharing, or transferring lead details.

Avoid:

- bypassing login walls or privacy controls;
- scraping private accounts;
- collecting sensitive personal data;
- treating any scraped email as opt-in consent.

## Actor Shortlist

| Platform | Primary actor(s) | Use case | Email strategy | Notes |
|---|---|---|---|---|
| X / Twitter | `scrapers/twitter`, `email_scraper/x-twitter-email-scraper` | profile/search/tweet discovery; indexed email snippets | Use X Email Scraper for SERP-snippet emails; use Twitter scraper for profile/context only | X Email Scraper searches public Google snippets with `site:x.com` and domain filters. |
| Threads | `webdata_labs/threads-scraper`, `lergassy/threads-scraper` | posts, profiles, keyword search, accounts | Prefer profile bio/bio links; `lergassy` advertises emails/phones in bio/profile data | Threads search can be shallow; use account/profile modes for volume. |
| Instagram | `apify/instagram-profile-scraper`, `instagram-scraper/instagram-profile-finder`, `email_scraper/instagram-email-scraper`, `khadinakbar/instagram-profile-scraper` | creator/business profile discovery and qualification | Use profile contact fields/bio links first; use Email Scraper or Profile Finder email discovery for indexed emails | Prefer official Apify actor for stable profile data; community actors may expose parsed contact fields. |
| TikTok | `clockworks/tiktok-scraper`, `email_scraper/tiktok-email-scraper`, `apidojo/tiktok-scraper` | creator/profile/video/hashtag discovery | Use TikTok Email Scraper for public SERP snippets; use profile/video actor for context and scoring | TikTok Email Scraper does not access private info; coverage depends on public snippets. |
| YouTube | `streamers/youtube-scraper`, `email_scraper/youtube-email-scraper` | channel/video/topic discovery | Use YouTube Email Scraper for public Google snippets; use YouTube Scraper for channel/video metrics | Useful for creator lead discovery by niche + location. |
| Facebook | `apify/facebook-pages-scraper`, `apify/facebook-ads-scraper` | public pages, businesses, ads intelligence | Facebook Pages Scraper can return public page email/website; Ads Scraper is for signal, not email | Avoid personal profiles and private groups unless explicitly approved and allowed. |
| LinkedIn | `scraper-engine/linkedin-profile-scraper`, `dev_fusion/Linkedin-Profile-Scraper`, company scrapers | B2B/person/company context | Use only public guest-view data and business/work emails; high compliance risk | Treat as personal data; legal review recommended for bulk use. |
| Cross-platform fallback | `apify/google-search-scraper` | query-based discovery across social domains | Build `site:` queries and extract/verify emails downstream | Good for controlled niche search and auditability. |
| Non-social lead supplement | `compass/crawler-google-places` | local business contacts | public business email/phone/website | Useful when social email yield is low. |

## Recommended Pipeline

1. Define target niche and allowed platforms.
2. Start with broad discovery actors:
   - X/Twitter scraper for profiles and tweets.
   - Threads search/profile scraper.
   - Instagram Profile Finder or Profile Scraper.
   - TikTok Scraper by keyword/hashtag/user.
   - YouTube Scraper by channel/topic.
3. Run email-specific actors only for public indexed contacts:
   - `email_scraper/x-twitter-email-scraper`
   - `email_scraper/instagram-email-scraper`
   - `email_scraper/tiktok-email-scraper`
   - `email_scraper/youtube-email-scraper`
4. Normalize into one candidate table.
5. Dedupe by lowercased email + platform + source URL.
6. Score confidence:
   - high: business email in official profile/page bio or website;
   - medium: email in indexed search snippet with matching social URL;
   - review: free-mail address, unclear owner, stale snippet, mismatch between keyword and profile.
7. Validate only at review/prep level. Do not send.
8. Produce an approval packet before any outreach.

## Candidate Table Schema

Use these fields:

```text
id
run_id
platform
actor_id
keyword
profile_or_page_name
handle
source_url
source_date
email
email_domain
email_source_field
bio_or_snippet
website_url
followers_or_metric
niche
location_hint
confidence
status
review_reason
approval_status
created_at
updated_at
notes
```

Suggested status values:

```text
draft, review, approved, rejected, duplicate, blocked
```

Suggested approval values:

```text
not_required, needed, requested, approved, denied
```

## Starter Inputs

### X Email Scraper

```json
{
  "keywords": ["ai consultant", "fitness coach"],
  "customDomains": ["@gmail.com", "@company.com"],
  "location": "United States",
  "maxEmails": 50
}
```

### Instagram Profile Finder

```json
{
  "queries": ["beauty influencer", "saas founder"],
  "emailDiscoveryMode": true,
  "searchCountry": "us"
}
```

### TikTok Email Scraper

```json
{
  "keywords": ["skincare creator", "fitness coach"],
  "customDomains": ["@gmail.com"],
  "location": "New York",
  "maxEmails": 50
}
```

### YouTube Email Scraper

```json
{
  "keywords": ["fitness coach", "ai automation agency"],
  "customDomains": ["@gmail.com", "@outlook.com"],
  "location": "United States",
  "maxEmails": 50,
  "excludeWords": ["jobs", "hiring", "template"]
}
```

## Docs, Repos, And Videos To Study

### Official docs

- Apify Store: https://apify.com/store
- Apify Academy: https://docs.apify.com/academy
- Getting started with Apify scrapers: https://docs.apify.com/academy/apify-scrapers/getting-started
- Creating Actors: https://docs.apify.com/academy/getting-started/creating-actors
- Python API client quick start: https://docs.apify.com/api/client/python/docs/introduction/quick-start
- Run Actor/task and retrieve data via API: https://help.apify.com/en/articles/3224035-run-actor-task-and-retrieve-data-via-api
- Apify MCP server: https://docs.apify.com/integrations/mcp

### Repositories

- Python API client: https://github.com/apify/apify-client-python
- JavaScript/TypeScript SDK: https://github.com/apify/apify-sdk-js
- Apify MCP server: https://github.com/apify/apify-mcp-server

### Videos / webinars

- Scraping with Apify 101: https://apify.com/resources/scraping-with-apify
- Social media scraping for lead gen, trends, and sentiment analysis: https://apify.com/events/social-media-scraping-webinar

## First Safe Experiment

Run a small test batch before scaling:

```text
Platforms: Instagram + TikTok + YouTube
Niche: one narrow niche
Location: one country/city
Limit: 25-50 candidate emails per actor
Budget ceiling: user-approved Apify spend only
Output: candidate table + duplicate report + confidence review
No outreach
```

Stop after the first batch and review:

- number of unique emails;
- percentage with source URLs;
- high/medium/review confidence split;
- actor cost;
- duplicate rate;
- platform yield;
- legal/compliance risks;
- recommended next actor or query refinement.

## Forex Engagement Pipeline

For Forex, use engagement actors first and email actors second. Customer prospects are usually commenters/repliers/likers on Forex posts, not the creators or sellers posting the content.

Use the dedicated research map and runbook:

- `docs/forex-social-engagement-lead-research.md`
- `docs/runbook-forex-social-engagement-lead-batch.md`
- `.ai/agents/forex-social-intent/`

## Briantom Customer-First Correction

For this repo's retail customer goal, do not start with broad `keyword + @gmail.com` social email actors. The Facebook actor test on 2026-09-22 returned 2 raw emails and 0 accepted customer leads because snippets matched seller/training/creator-side pages.

Use this order instead:

```text
public comments/replies -> customer intent scoring -> seller/IB/affiliate rejection -> exact profile/link enrichment -> website/contact extraction only if a public link exists
```

Broad keyword email actors may be used only for a separately labeled `operator_business` track, such as trading schools, signal group operators, communities, or AI Sales Agent buyers with public websites. Do not mix those rows with `retail_customer` leads.

See `docs/briantom-social-email-customer-pipeline.md` before preparing the next Apify approval packet.
