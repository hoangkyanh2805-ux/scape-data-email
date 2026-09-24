# Public Email Enrichment Research

Date: 2026-09-22
Project: `scape-data`
Mode: research only, public data only, no outreach, no external export.

## Research Question

How can `scape-data` legally and safely find email leads when YouTube, TikTok, or Instagram personal profiles do not display an email?

Known failure mode:

```text
offer keyword -> email scraper -> creator / IB / affiliate / seller email
```

Project goal:

```text
offer-fit engagement evidence
-> real customer or operator intent
-> public identity/contact enrichment
-> sourced email only when available
-> local review table
```

## Bottom Line

If a personal social profile has no public email, no public website, no public link hub, and no exact-match indexed contact page, there is no reliable public-only method to get that person's email without crossing into guessing, private contact panels, enrichment databases, or false matches.

For this project, do not force email extraction from personal commenters. Change the source mix:

1. Keep YouTube/TikTok/Instagram comments for intent and content mining.
2. Enrich email only when the commenter has a public website/link/profile that exposes contact data.
3. Add higher-yield public-email sources where the target has reason to publish contact info: public websites, profile links, newsletters/blog/contact pages, and Google Maps/business websites for the AI Sales Agent/operator bucket only.

## Method Matrix

| Method | Use for scape-data? | Expected yield | Safety notes | Actor/tool candidates |
|---|---:|---:|---|---|
| Exact channel/profile public enrichment | Yes, after comment scoring | Low for personal commenters, medium for operators | Only public About/bio/links; no logged-in contact buttons | `crawlerbros/youtube-email-scraper`, `hipersoft/youtube-scraper` channel data |
| Website contact extraction from profile link | Yes | Medium/high when a website exists | Source URL required; do not guess role-specific emails | `automation-lab/website-email-extractor`, `insight.solutions/website-contact-extractor`, `haketa/email-extractor` |
| Exact identity SERP probe | Yes, last-mile only | Very low to low | High false-match risk; exact handle/channel URL only | `apify/google-search-scraper` or equivalent SERP actor |
| Keyword-to-email social scraper | Mostly no | High records, low customer precision | Pulls creators/sellers/affiliates; only use for `ai_sales_agent` operator research with review | `email_scraper/youtube-email-scraper`, `email_scraper/x-twitter-email-scraper`, `email_scraper/instagram-email-scraper` |
| Google Maps -> website email | Yes, but only B2B/operator bucket | Medium/high for businesses | Not retail trader customers; good for signal/course operators, agencies, trading schools, brokers | Google Maps Email Extractor actors, website contact actors |
| GitHub public email mining | No for this offer | Medium technically, poor fit | Security/phishing risk, wrong audience | Avoid unless project changes to developer/B2B tool |
| Contact panels / login / cookies | No | N/A | Forbidden by project rules | Do not use |
| Guessed/generated emails or validation at scale | No | N/A | Forbidden by project rules | Do not use |

## Sources And Patterns

### YouTube channel exact enrichment

`crawlerbros/youtube-email-scraper` accepts channel URLs or handles, scans public About descriptions, public advertised links, and linked Instagram/TikTok/Linktree bios. Its page says it uses no cookies/login/API keys and cannot extract YouTube click-to-reveal emails that require login.

Source: https://apify.com/crawlerbros/youtube-email-scraper

Use only after:

```text
commenter passed offer-fit scoring
-> channel URL is known
-> channel belongs to the commenter identity
```

Recommended input shape:

```json
{
  "channelUrls": [
    "https://www.youtube.com/channel/UC..."
  ],
  "followExternalProfiles": true,
  "maxExternalPerChannel": 3,
  "autoProxyFallback": true
}
```

### Website email extraction from public links

`automation-lab/website-email-extractor` crawls supplied public URLs/domains, follows bounded same-site contact/about/team/support/legal/impressum links, records exact source pages, and says it does not guess addresses, generate email patterns, verify mailboxes, or access logins.

Source: https://apify.com/automation-lab/website-email-extractor

This is the best public-only email step when a commenter/profile exposes a website, Linktree, portfolio, blog, school, Telegram landing page, or community page.

Recommended input shape:

```json
{
  "startUrls": [
    { "url": "https://example.com/contact" }
  ],
  "maxItems": 10,
  "maxPagesPerWebsite": 5,
  "maxDepth": 1,
  "includeSubdomains": false,
  "proxyConfiguration": { "useApifyProxy": false }
}
```

### Google Maps/business website enrichment

Apify's Google Maps email extraction guides describe the common pattern: scrape business listings, collect website URLs, then crawl business websites because emails usually are not inside the Maps payload itself.

Sources:

- https://blog.apify.com/how-to-extract-emails-from-google-places/
- https://apify.com/x_guru/google-maps-email-extractor
- https://n8n.io/workflows/6307-google-maps-lead-generation-with-apify-and-email-extraction-for-airtable/

Use for these offer buckets only:

```text
ai_sales_agent
broker_partnership_operator
trading_school_operator
signal_group_operator
course_or_community_operator
```

Do not use Google Maps for retail trader/customer leads. It will produce businesses/operators, not personal customers.

### SERP exact identity probe

SERP actors can search exact handles/channel URLs and return indexed pages/snippets. This is useful only as a last-mile check after profile enrichment returns no email.

Source: https://apify.com/simpleapi/google-search-results-scraper

Allowed query pattern:

```text
"https://www.youtube.com/channel/UC..." email OR gmail
"@exactHandle" email OR gmail
```

Disallowed query pattern:

```text
forex beginner need help gmail
xauusd signal customer email
```

The broad form finds sellers and unrelated creators.

### n8n/GitHub workflow patterns

Useful architecture references:

- `sirlifehacker/lead-gen-hacker`: multi-source lead generation and enrichment with n8n, Apify, and AI agents. Source: https://github.com/sirlifehacker/lead-gen-hacker
- `TheNextGenNexus/n8n-nodes-nexgendata`: n8n nodes wrapping Apify actors including website email extraction. Source: https://github.com/TheNextGenNexus/n8n-nodes-nexgendata
- `willowridge1234/n8n-ai-lead-scoring`: score scraped leads against an ICP before storing results. Source: https://github.com/willowridge1234/n8n-ai-lead-scoring
- n8n Google Maps + Apify email extraction workflow: Maps -> website -> email extraction. Source: https://n8n.io/workflows/6307-google-maps-lead-generation-with-apify-and-email-extraction-for-airtable/

Use these as architecture references only. Do not copy outreach/CRM-sync steps unless the user explicitly approves export or outreach.

## Legal / Safety Notes

This is not legal advice. For this repo, use these as operational guardrails:

- US CAN-SPAM compliance still matters for any later commercial email. FTC guidance says commercial messages need truthful headers/subject, sender identification, valid physical address, and opt-out. Source: https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business
- CAN-SPAM has special risk around harvested addresses and dictionary/generated emails, especially where a site says addresses may not be transferred for commercial email. Source: https://uscode.house.gov/view.xhtml?edition=prelim&path=%2Fprelim%40title15%2Fchapter103
- GDPR/UK/EU privacy guidance requires a legal basis and attention to fairness, transparency, expectation, data minimization, and objection rights. Public availability alone is not a blank check. Sources: https://www.edpb.europa.eu/topics/key-gdpr-concepts/legal-basis_en, https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/direct-marketing-guidance/collect-information-and-generate-leads/, https://www.cnil.fr/fr/node/165906

Project rule:

```text
public-only collection is allowed for local review;
outreach/export/CRM sync requires separate explicit human approval.
```

## Recommended Next Workflow For scape-data

### Track A - Customer intent, low email yield, high content value

Use for retail trader customers:

```text
YouTube/TikTok/Instagram comments
-> offer-fit scoring
-> seller/IB/affiliate filter
-> retain high-intent customer comments
-> enrich only public channel/about/link
-> if no public email/link, stop
-> save as VOC/content insights, not email lead
```

This track is good for:

```text
content ideas
ad angles
offer copy
lead magnet topics
comment-based retargeting ideas if platform-native ads are later approved
```

It is weak for direct public email acquisition.

### Track B - Operator/business email, higher yield

Use for `ai_sales_agent`, broker/operator, course/community/signal owner buckets:

```text
find operator intent sources
-> identify public business/profile/channel/site
-> crawl public website/contact/about pages
-> extract sourced email
-> classify as operator lead, not retail customer lead
```

This track can produce email because operators publish contact routes.

### Track C - Hybrid

Use comments for demand, then find businesses that already serve that demand:

```text
comments show repeated pain
-> infer demand theme
-> search for public businesses/operators serving that theme
-> collect business websites/emails
-> mark lead_type=operator_supply_side
```

This is not customer email, but it can fit the AI Sales Agent offer because the buyer is the operator with leads to handle.

## Agent Sequence

For personal commenter enrichment:

```text
approval-gate-reporter
-> profile-enricher
-> lead-normalizer
-> compliance-reviewer
-> approval-gate-reporter
```

For a new email-yield batch:

```text
approval-gate-reporter
-> source-finder
-> buyer-intent-scorer
-> seller-spam-filter
-> profile-enricher
-> website-contact-enricher
-> lead-normalizer
-> compliance-reviewer
-> approval-gate-reporter
```

## Decision Rule

If the lead is a personal commenter:

```text
public email visible? keep
public website/link exists? crawl
no email/link/exact match? stop, keep as VOC/content lead only
```

If the lead is an operator/business:

```text
public business/channel/profile/site exists? crawl
public sourced email found? keep as review
no source URL? reject
```

## Next Approval Packet Recommendation

Do not run another exact probe on the same four users. Expected yield is near zero.

Recommended next paid test:

```yaml
approval_id: apify-operator-website-email-tiny-test-001
goal: Find public emails for operator/business leads that fit the AI Sales Agent offer bucket.
source: Google Maps / Google Search / YouTube operator channels
max_sources: 10
website_contact_extraction: true
budget_ceiling_usd: 0.05
rules:
  - public data only
  - no login/cookies/contact panels
  - no guessed/generated emails
  - no outreach/export
  - every email needs source URL and source field
output:
  - lead_candidates.csv
  - enriched_profiles.csv
  - batch_report.md
```

Recommended next free/local step:

```text
Save high-intent YouTube comments as VOC/content assets for a separate YouTube content project.
```
