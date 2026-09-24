# Command - Find TikTok Forex Video Links

Purpose: use Apify MCP to find public TikTok video links for Forex/XAUUSD keywords, then stop for human selection before comment scraping.

Agent to use: `.ai/agents/forex-social-intent/source-finder.AGENT.md`

## Runtime Rules

- research_only: true
- public_data_only: true
- outreach_enabled: false
- external_export_enabled: false
- no login/cookies/session tokens
- no private sources
- no comments scrape in this step
- no email/contact extraction in this step

## Actor

Use actor: `clockworks/tiktok-scraper`

Read actor details/schema first with Apify MCP `fetch-actor-details`.

## Keywords

Start with this keyword set unless the operator changes it:

```text
xauusd
forex beginner
forex funded trader
prop firm trading
ict trading
smart money concept forex
forex signals
gold trading xauusd
```

## Tiny Search Input Draft

Use search mode, not profile/user batch mode.

```json
{
  "search": [
    "xauusd",
    "forex beginner",
    "forex funded trader",
    "prop firm trading",
    "ict trading",
    "smart money concept forex",
    "forex signals",
    "gold trading xauusd"
  ],
  "searchSection": "videos",
  "resultsPerPage": 5,
  "maxProfilesPerQuery": 0,
  "commentsPerPost": 0,
  "topLevelCommentsPerPost": 0,
  "maxRepliesPerComment": 0,
  "scrapeRelatedVideos": false,
  "shouldDownloadVideos": false,
  "shouldDownloadCovers": false,
  "shouldDownloadSubtitles": false,
  "shouldDownloadAvatars": false,
  "proxyCountryCode": "None"
}
```

If current schema uses a different search field name, adapt only after reading actor schema/details.

## Output Table

Return a markdown table with max 25 candidate videos:

| rank | keyword | video_url | caption | author | create_date | play_count | comment_count | buyer_intent_hint | seller_spam_risk | recommended |
|---:|---|---|---|---|---|---:|---:|---|---|---|

## Ranking Rules

Prefer videos where comments are likely to contain learner/buyer intent:

- beginner questions
- funded trader / prop firm context
- XAUUSD/gold trading questions
- ICT/SMC strategy questions
- pain around losses, entries, risk, psychology

Downrank obvious sellers, signal channels, spam, giveaways, unrealistic profit flexing, or videos with no comments.

## Stop Point

Stop after listing candidate video links. Ask the operator to choose 1-3 video URLs for the comment scraper.

Do not run `clockworks/tiktok-comments-scraper` until the operator approves exact selected URLs, input JSON, and cost ceiling.
