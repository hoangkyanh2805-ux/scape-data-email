# Approval Packet - TikTok Video Link Discovery

approval_id: apify-tiktok-video-link-discovery-001
approval_status: requested
created_for: scape-data
actor_id: clockworks/tiktok-scraper
actor_url: https://apify.com/clockworks/tiktok-scraper
agent: source-finder

## Purpose

Find public TikTok video URLs for Forex/XAUUSD keywords so the operator can choose which videos should be used for a tiny comments test.

## Proposed Keywords

- xauusd
- forex beginner
- forex funded trader
- prop firm trading
- ict trading
- smart money concept forex
- forex signals
- gold trading xauusd

## Proposed Search Input Draft

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

## Limits

- Public TikTok search only.
- No comments collection in this step.
- No profile follower/following scrape.
- No downloads.
- No outreach/export/contact extraction.
- Output only a review table of candidate video links.

## Cost Ceiling

Actor page currently shows from about $1.70 / 1,000 results. For 8 keywords x 5 results, expected max is about 40 results.

Requested ceiling: $0.15 total for discovery.

## Stop Conditions

Stop if:

- current schema does not support search mode;
- estimated cost exceeds $0.15;
- actor would collect comments or profile follower/following data;
- output would exceed 40 search results;
- private/login-only content is required.

## Next Approval

After candidate links are listed, operator chooses 1-3 URLs for `clockworks/tiktok-comments-scraper`.
