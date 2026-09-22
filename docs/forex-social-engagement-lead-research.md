# Forex Social Engagement Lead Research Map

## What The Research Says

The right target is not primarily Forex creators or sellers. For buyer discovery, start from public Forex content and collect the people who engage with it: commenters, repliers, and sometimes likers/followers when available.

Useful external sources found:

- Apify Instagram scraping guide: https://blog.apify.com/scrape-instagram-posts-comments-and-more-21d05506aeb3/
- Apify TikTok lead generation walkthrough: https://blog.apify.com/tiktok-lead-generation/
- Twitter X Reply Scraper actor: https://apify.com/api-empire/twitter-x-reply-scraper
- Twitter/X tweets, profiles, replies scraper: https://apify.com/scrapesmith/twitter-x-scraper-tweets-profiles-replies/api
- YouTube Comments Scraper with commenter enrichment: https://apify.com/simpleapi/youtube-comments-scraper
- YouTube Scraper with comments/transcripts: https://apify.com/hipersoft/youtube-scraper
- Instagram all-in-one scraper with comments/likers/contacts modes: https://apify.com/vortex_data/instagram-scraper
- TikTok comments mode example: https://apify.com/get-leads/all-in-one-tiktok-scraper
- n8n TikTok prospect-list workflow gist: https://gist.github.com/triposat/71db8e59333901ed642e1bce4457c5fc
- n8n + Apify + AI lead gen repo: https://github.com/sirlifehacker/lead-gen-hacker
- Apify MCP server repo: https://github.com/apify/apify-mcp-server
- Apify Cursor plugin repo: https://github.com/apify/apify-cursor-plugin

## Actor Strategy

Use engagement actors first, email actors second.

| Platform | Engagement actor target | Profile/contact actor target | Notes |
|---|---|---|---|
| TikTok | TikTok Comments Scraper, `get-leads/all-in-one-tiktok-scraper` comments mode | TikTok profile scraper, TikTok email scraper | Strong first test platform because comments reveal buying pain. |
| YouTube | `simpleapi/youtube-comments-scraper`, `hipersoft/youtube-scraper` comments mode | YouTube email scraper, channel scraper | Good for educational Forex videos, prop firm videos, XAUUSD analysis. |
| Instagram | Instagram post/comment/liker scraper, all-in-one Instagram scraper | `apify/instagram-profile-scraper`, email discovery actors | Use posts/reels from Forex sellers, then commenters. |
| X/Twitter | X reply scraper, tweets/profiles/replies scrapers | X email scraper, profile scraper | Replies have better intent than raw tweet authors. |
| Threads | Threads scraper with replies/posts/accounts | profile bio/contact fields where exposed | Useful as a secondary source. |
| Facebook/Reddit | page/post/comment actors, Reddit scrapers | page email/website or profile context | Use only public pages/subreddits; avoid private groups. |

## Forex Buyer Intent Terms

High intent:

```text
how do I join
price?
can you teach me
I keep losing
how to pass FTMO
what entry is this
share strategy
DM me
I need mentor
beginner
funded challenge
XAUUSD entry
what broker
```

Seller/spam filters:

```text
join my VIP
signals group
account management
copy trading
broker promo
DM for signals
guaranteed profit
investment manager
```

## First Batch Recommendation

Start with TikTok + YouTube before X/Instagram:

1. Find 20-30 Forex/XAUUSD/FTMO videos with active comments.
2. Scrape up to 500-1000 comments per video within a user-approved Apify cost ceiling.
3. Dedupe commenters.
4. Score buyer intent.
5. Filter sellers/spam.
6. Enrich only high/medium candidates with public profiles/contact fields.
7. Produce review table. No outreach.
