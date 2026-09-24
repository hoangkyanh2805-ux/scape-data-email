# Approval Packet - Exact YouTube Customer Handle Email Probe

approval_id: `apify-youtube-exact-handle-email-probe-001`

## Agent Routing

```text
profile-enricher
-> lead-normalizer
-> approval-gate-reporter
```

## Why This Exists

The 4 retained YouTube commenters are valid customer-intent leads, but their public YouTube channel enrichment returned:

```text
public_email: 0
public_website_links: 0
```

This packet proposes one tiny final public-data probe using exact YouTube handles/channel URLs only. It must not use broad offer keywords because that previously returned creator/seller/affiliate emails.

## Input Source

```text
data/forex-social-intent/runs/20260922-190911/lead_candidates.csv
```

Qualified handles:

```text
@judymugo6751
@AfrosterGerald
@MaxwellLouis-d5h
@ChartMe_Avi
```

## Proposed Actor

Preferred actor:

```text
email_scraper/youtube-email-scraper
actor_id: xZgGtDhmOGEL0AzX7
```

Role: exact public search-snippet email probe for retained customer handles only.

Fallback if this actor cannot constrain to exact handles:

```text
Do not run. Stop and report no safe public email source for this batch.
```

## Exact Input

```json
{
  "keywords": [
    "site:youtube.com/@judymugo6751 @judymugo6751 email",
    "site:youtube.com/@AfrosterGerald @AfrosterGerald email",
    "site:youtube.com/@MaxwellLouis-d5h @MaxwellLouis-d5h email",
    "site:youtube.com/@ChartMe_Avi @ChartMe_Avi email"
  ],
  "location": "",
  "customDomains": ["@gmail.com"],
  "maxEmails": 1,
  "excludeWords": [
    "recovery",
    "guaranteed profit",
    "account manager",
    "binary",
    "onlyfans",
    "sponsorship",
    "partnership",
    "business inquiries",
    "promo",
    "affiliate"
  ]
}
```

## Cost / Budget

- Scope: 4 exact handle queries x 1 domain x max 1 result.
- Budget ceiling: `$0.03`.
- Abort guard: stop if Apify usage reaches `$0.025`.

## Acceptance Rules

Retain an email only if all are true:

- result keyword contains the exact retained handle;
- source URL/title/description ties to that exact YouTube handle or channel;
- email appears in public snippet/source field;
- row keeps `email_source_url` and `email_source_field`;
- status remains `review`, not approved.

Reject result if:

- it belongs to video creator, seller, IB, affiliate, sponsor, vendor, or unrelated site;
- source only matches broad Forex/YouTube keyword;
- email cannot be tied to the retained customer handle;
- actor requires login/cookies/contact panel.

## Hard Safety Rules

- Public data only.
- No login/cookies.
- No YouTube contact panel reveal.
- No guessed/generated email.
- No validation at scale.
- No outreach.
- No external export.

## Approval Status

```yaml
approval_status: requested
run_actor_now: false
human_approval_required: true
```

To approve, reply:

```text
duyet exact youtube handle email probe budget 0.03
```
