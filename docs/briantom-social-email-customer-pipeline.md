# Briantom Social Email Customer Pipeline

Date: 2026-09-22
Agent: Briantom
Mode: research/prep only, public data only, no paid actor run, no outreach, no external export.

## Goal

Find public social emails for real offer-fit customers using Apify actors, while rejecting creators, sellers, IBs, affiliates, signal providers, and spam unless they are explicitly operator-fit for the AI Sales Agent bucket.

Target state:

```text
public engagement evidence -> customer intent score -> seller/IB/affiliate rejection -> public profile/link enrichment -> sourced public email only -> local CSV/Markdown review artifacts
```

## 1. Diagnosis: Why Keyword-To-Email Fails

The failed pattern:

```text
keyword + @gmail.com -> email scraper -> Google/Facebook/YouTube snippets -> creator/seller/training pages
```

Why it returns the wrong people:

- The query asks Google for pages that publish emails, not for commenters with buyer pain.
- Real retail customers rarely publish email in social profiles; creators, sellers, trainers, IBs, and affiliate pages do.
- Seller pages use buyer words in marketing copy: "need mentor", "learn forex", "failed challenge", "how to start".
- Email-first actors lack engagement evidence. They cannot prove the email owner is the person asking for help.
- Free-mail snippets with weak redirect URLs are not enough unless the source URL and source field prove identity.

Evidence from the Facebook actor test:

```text
Actor: email_scraper/facebook-email-scraper
Run: ceVEhSElxJLRJ20Do
Cost: $0.0105
Raw emails: 2
Accepted customer leads: 0
Rejected: 2
Reason: seller/training/creator-side snippets, not customer pain comments
```

Decision:

```text
Do not scale broad keyword-to-email for retail customer leads. Use engagement-first discovery, then exact public enrichment.
```

## 2. Coordinated Actor Pipeline

### Stage A - Source Discovery

Purpose: find public posts/videos/pages where real customers ask questions or complain.

Actor candidates:

- YouTube videos/comments: `hipersoft/youtube-scraper`, `data_minds/youtube-comments-scraper`, equivalent YouTube comment actors.
- TikTok videos/comments: `clockworks/tiktok-scraper`, `clockworks/tiktok-comments-scraper`.
- Facebook public pages/groups/search snippets: `email_scraper/facebook-email-scraper` only in strict review mode; public page actors for page context when available.
- Instagram public posts/profiles: Instagram profile/post scraper for public bio/context only.
- Google SERP: `apify/google-search-scraper` for finding public source URLs, not for broad email harvesting.

Outputs: `source_map.csv`, `post_table.csv`, `engagement_table.csv`.

### Stage B - Customer Intent Scoring

Score comments before any email actor runs.

Keep signals:

- "how do I start"
- "need mentor"
- "which broker"
- "failed challenge"
- "need signal"
- "want copy trading"
- "can you teach me"
- "how can I apply"
- "I keep losing"
- "what app / capital / strategy"

Output: `intent_score_table.csv`.

### Stage C - Seller / IB / Affiliate Filter

Reject unless explicitly AI Sales Agent operator-fit:

- IB, broker partner, affiliate, ambassador, referral code.
- signal provider, VIP group, premium signals, account manager.
- managed account, copy my trades, investment manager.
- DM me, WhatsApp me, guaranteed profit, recovery scam.
- course seller, mentor selling slots, "join my class", "3-day training".

Preserve as review only if the operator has clear automation/follow-up/lead-handling pain.

Output: `filtered_leads.csv`.

### Stage D - Exact Profile Enrichment

Enrich only retained commenters/handles, not broad keywords.

Allowed enrichment:

- Public profile bio/about.
- Public website/link hub from the profile.
- Public search snippet for exact handle/channel/profile URL.
- Public page/profile email field if visible without login.

Forbidden:

- Login/cookies/private contact panels.
- Guessing/generated email.
- Validation at scale.
- Outreach/export.

Output: `enriched_profiles.csv`.

### Stage E - Website Contact Extraction

Only when the retained profile exposes a website/link hub/domain.

Actor candidates:

- `automation-lab/website-email-extractor`
- `insight.solutions/website-contact-extractor`
- `haketa/email-extractor`
- `harvestlab/contact-extractor`

Rules:

- Crawl shallow: contact/about/team/support/legal only.
- Keep `email_source_url` and `email_source_field`.
- Reject catch-all or unsourced emails.

Outputs: `lead_candidates.csv`, `batch_report.md`.

## 3. Scoring And Reject Rules

Use a 0-100 score:

- 80-100: direct customer pain or buying/learning request.
- 50-79: relevant question with weaker urgency.
- 20-49: generic praise or weak context.
- 0-19: spam, unrelated, seller pitch.

Required high-intent fields:

```text
platform, handle, profile_url, source_post_url, comment_text, evidence_phrase, offer_bucket, customer_intent_score, seller_filter_status
```

Customer keep signals:

- asks to learn, start, apply, join, get mentored, solve losses.
- asks for broker/funded/challenge help.
- asks for signals/entries as a buyer, not as a provider.
- wants copytrading/done-for-you as a buyer.
- shows confusion, failure, urgency, or direct request for help.

Seller reject signals:

```text
IB, affiliate, broker partner, signal provider, VIP signals, managed account, account management, copy my trades, join my group, DM me, WhatsApp me, mentor slots, course seller, trading academy, guaranteed profit, recovery, promo code
```

AI Sales Agent operator exception:

```text
lead_type = operator_ai_sales_agent_fit
```

Only preserve if evidence shows missed leads, manual DM/Telegram/WhatsApp follow-up pain, low conversion, onboarding/support bottleneck, or ownership of a signal/course/community business.

## 4. Actor Candidate Map

| Platform | Discovery actor | Email/enrichment actor | Use it for | Caution |
|---|---|---|---|---|
| YouTube | `hipersoft/youtube-scraper`, `data_minds/youtube-comments-scraper` | `crawlerbros/youtube-email-scraper`, `email_scraper/youtube-email-scraper`, SERP exact probe | comments -> channel/profile -> public bio/link/email | Do not use click-to-reveal email panels |
| TikTok | `clockworks/tiktok-scraper`, `clockworks/tiktok-comments-scraper` | `clockworks/tiktok-scraper`, `email_scraper/tiktok-email-scraper`, SERP exact probe | video/commenter -> public profile bio/link | Broad keyword email scraper pulls sellers |
| Facebook | public page/search actors, `email_scraper/facebook-email-scraper` | same actor only as review, plus website contact extractor | operator/business pages, public snippets | Failed retail test: high seller false positives |
| Instagram | public profile/post scraper | `email_scraper/instagram-email-scraper`, profile scraper contact fields, website contact extractor | exact handle/profile after qualification | Avoid private profiles/login-only contact data |
| Google | `apify/google-search-scraper` or equivalent SERP actor | exact handle/profile/domain search | last-mile identity/email proof | Broad queries cause false matches |
| Website | N/A | `automation-lab/website-email-extractor`, `insight.solutions/website-contact-extractor`, `haketa/email-extractor` | public websites linked by qualified profiles | Only crawl public pages; no guessing |

## 5. Next Tiny Test Approval Packet

Recommended next paid test:

```yaml
approval_id: apify-youtube-retail-commenter-exact-email-002
goal: Test whether a larger set of qualified retail commenters produces any public emails after exact profile/link enrichment.
do_not_run_without_approval: true
budget_ceiling_usd: 0.05
rules:
  - public data only
  - no login/cookies/private contact panels
  - no guessed/generated emails
  - no validation at scale
  - no outreach/export
  - every retained email needs email_source_url and email_source_field
input_source:
  prior_run: data/forex-social-intent/runs/20260922-190136/filtered_leads.csv
  target_rows:
    status: QUALIFIED_CUSTOMER or REVIEW with strong customer evidence
    max_profiles: 10
actor_sequence:
  - actor: crawlerbros/youtube-email-scraper
    purpose: exact channel/handle public email/link extraction only
    input:
      channelUrls:
        - "{{qualified_youtube_channel_url_1}}"
        - "{{qualified_youtube_channel_url_2}}"
        - "{{qualified_youtube_channel_url_3}}"
      followExternalProfiles: true
      maxExternalPerChannel: 2
      autoProxyFallback: true
  - actor: apify/google-search-scraper
    purpose: exact handle/profile fallback only if no email found
    input:
      queries:
        - "\"{{exact_channel_url}}\" email OR gmail"
        - "\"{{exact_handle}}\" \"{{display_name}}\" email"
      maxPagesPerQuery: 1
acceptance:
  keep_if:
    - email belongs to same exact handle/channel/profile identity
    - source_url is public
    - source_field is bio/about/website/snippet/contact_page
  reject_if:
    - seller/IB/affiliate/creator offer
    - email has no source URL
    - source is Google redirect only without recoverable public source
    - identity match is weak
outputs:
  - actor_input.json
  - enriched_profiles.csv
  - lead_candidates.csv
  - rejected_candidates.csv
  - batch_report.md
```

Expected result: low yield but clean measurement. If the selected qualified commenters return zero sourced public emails again, stop retail-email extraction and use comments for VOC/content while moving email acquisition to operator/business website extraction.

Alternative higher-yield test:

```yaml
approval_id: apify-operator-website-email-tiny-test-001
goal: Find public emails for operator/business accounts fitting AI Sales Agent offer.
budget_ceiling_usd: 0.05
source: public Google/YouTube/Facebook/Instagram operator profiles with websites
max_websites: 5
actor: insight.solutions/website-contact-extractor or automation-lab/website-email-extractor
rules:
  - public websites only
  - no outreach/export
  - source URL and source field required
```

## 6. Repo Artifacts To Update

Update/keep current:

- `docs/public-email-enrichment-research.md`
- `docs/offer-fit-lead-filter.md`
- `docs/apify-social-email-lead-sourcing.md`
- `.ai/agents/forex-social-intent/buyer-intent-scorer.AGENT.md`
- `.ai/agents/forex-social-intent/seller-spam-filter.AGENT.md`
- `.ai/agents/forex-social-intent/profile-enricher.AGENT.md`
- `.ai/agents/forex-social-intent/lead-normalizer.AGENT.md`

Add:

- `.ai/agents/forex-social-intent/briantom-social-email-architect.AGENT.md`
- `docs/briantom-social-email-customer-pipeline.md`
- `docs/apify-youtube-retail-commenter-exact-email-approval.md`

Future run output path:

```text
data/forex-social-intent/runs/<timestamp>-retail-commenter-email-exact/
```

## Briantom Decision

For retail customers:

```text
comments first -> exact profile enrichment -> stop if no public email
```

For email yield:

```text
operator/business profiles with public websites -> website contact extraction
```

Do not run another broad `keyword + @gmail.com` actor for retail customers.
