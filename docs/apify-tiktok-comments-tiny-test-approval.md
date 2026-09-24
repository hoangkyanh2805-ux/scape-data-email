# Approval Packet - Tiny TikTok Comments Test

approval_id: apify-tiktok-comments-tiny-001
approval_status: requested
created_for: scape-data
actor_id: clockworks/tiktok-comments-scraper
actor_url: https://apify.com/clockworks/tiktok-comments-scraper
mcp_tool: clockworks/tiktok-comments-scraper

## Purpose

Run one tiny public-data-only TikTok comments test for a Forex/XAUUSD video to validate output shape, cost behavior, and downstream normalization.

## Current Schema Fields Used

- `postURLs`: array of TikTok video URLs.
- `commentsPerPost`: maximum comments, replies included, per post.
- `topLevelCommentsPerPost`: maximum top-level comments per post.
- `maxRepliesPerComment`: maximum replies per comment; set to `0` for this test.

## Proposed Input

Replace `PASTE_PUBLIC_TIKTOK_VIDEO_URL_HERE` with one public Forex/XAUUSD TikTok video URL before approval.

```json
{
  "postURLs": [
    "PASTE_PUBLIC_TIKTOK_VIDEO_URL_HERE"
  ],
  "commentsPerPost": 25,
  "topLevelCommentsPerPost": 25,
  "maxRepliesPerComment": 0
}
```

## Scope And Limits

- One public TikTok video URL only.
- Maximum 25 top-level comments.
- Replies disabled with `maxRepliesPerComment: 0`.
- No profile/user batch scraping.
- No login, cookies, session tokens, private sources, proxies, or evasion settings.
- No outreach, DM, email, CRM sync, Telegram, Drive/Sheets export, or lead transfer.
- Output review only; store locally under `data/forex-social-intent/runs/<YYYYMMDD-HHMM>/` if run is approved.

## Cost Estimate

Fetched actor details show current pricing is pay-per-event / per comment. Store pricing shows `from $0.50 / 1,000 comments`, and actor metadata includes tiered per-comment prices around `$0.00125` down to `$0.00015` depending on plan.

- Max billable comments: 25.
- Conservative free-tier estimate at $0.00125/comment: 25 comments ~= $0.03125.
- Requested ceiling: $0.05 total for this test.

## Stop Conditions

Stop and do not continue if:

- the URL is private, deleted, sensitive, or requires login;
- actor input schema differs materially from this packet;
- estimated cost exceeds $0.05;
- run would collect more than 25 comments/replies;
- output includes contact details requiring separate review;
- any external export/outreach/automation is requested.

## Approval Needed

Human must approve the exact final JSON input and `$0.05` ceiling before running the actor through Apify MCP.


