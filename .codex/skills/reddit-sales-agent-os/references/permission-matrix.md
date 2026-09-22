# Permission Matrix

Default rule: the agent may read public data and prepare drafts. A human must perform or explicitly approve account actions, external publication, paid operations, and sensitive claims.

| Action | Agent may do autonomously | Human approval required | Evidence required |
|---|---:|---:|---|
| Pull public Reddit RSS feeds within rate limits | Yes | No | RSS URL, fetched_at, volume log |
| Store public post/comment history | Yes | No | Permalink/id and timestamp |
| Update subreddit profiles from public evidence | Yes | No | Source links and update log |
| Draft product briefs, guides, posts, replies, dashboards | Yes | No | Draft artifact |
| Queue copy-ready Reddit replies/posts | Yes | No | Direct link, draft text, risk notes |
| Log into Reddit or use a Reddit account | No | Yes, human only | Human browser/session |
| Post, comment, vote, DM, or edit on Reddit | No | Yes, human only | Draft and target link |
| Include product link or direct promotion | No | Yes | Subreddit rules and approved copy |
| Publish landing page or checkout | No | Yes | Page preview, price, claims review |
| Send notifications to operator | Yes if channel approved | Yes if not approved | Message preview and destination |
| Use paid tools, hosting, generation, or deployment | No | Yes | Cost estimate and ceiling |
| Handle DMs | No | Human only | N/A |
| Delete records or overwrite history | No | Yes | Backup and exact target |

## Forbidden

- Automating Reddit login, posting, voting, or DMs.
- Using proxies, VPN rotation, or fingerprint workarounds to evade platform limits.
- Posting promotional replies disguised as help.
- Ignoring subreddit rules or removal patterns.
- Creating fake proof, fake testimonials, fake numbers, or fake scarcity.
- Selling into credentialed or high-harm niches without explicit expert review.
- Treating private DMs as agent-readable unless the user manually provides excerpts.
