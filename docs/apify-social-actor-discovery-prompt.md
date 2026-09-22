# Apify Social Actor Discovery Prompt - scape-data

Date: 2026-09-21
Repo: `scape-data`
Purpose: find and evaluate Apify actors for the public social email/contact pipeline.

## Core Rule

Do not search for email actors first. Search for actors by pipeline role:

```text
question/post discovery -> engagement/comment collection -> profile/email enrichment -> normalization/report
```

A social email actor is useful only if it can preserve public source evidence and does not require private/login-only access.

## Hermes Prompt

```text
You are finding Apify actors for the `scape-data` public social email/contact pipeline.

Goal: identify actors that help find public social users who show intent, then enrich only public emails with source proof.

Use the question-first framework:
1. Find actors that collect public posts/reels/threads/group posts by keyword, phrase, subreddit, group URL, post URL, or profile URL.
2. Find actors that collect public comments/replies/commenters from those posts.
3. Find actors that enrich public profiles/emails only when the email is visible in public bio/page/about/search snippet.
4. Reject actors that require login cookies, private groups, DMs, hidden contact panels, email guessing, or external export.
5. Prefer actors that expose API/MCP usage, clear input schema, output fields, source URL, author/profile pointer, comment count, run/dataset records, and pricing.

For every candidate actor, return this table:

actor_id_or_slug | platform | pipeline_role | why_relevant | required_inputs | useful_output_fields | email_fields | public_source_evidence | needs_login_or_cookie | pricing_note | risk | test_input | decision

Decision values:
- active_whitelist_candidate
- test_in_console
- reference_only
- reject

Never add an actor to the active whitelist until the user confirms it works in Apify Console.
```

## Pipeline Roles

### 1. Source/Post Discovery

Find public sources where people ask repeated concrete questions.

Useful input patterns:

```text
subreddits
search keywords
public Facebook group post keywords
Instagram post/reel URLs
TikTok video URLs
YouTube video URLs
X post/profile URLs
Threads search/profile URLs
```

Useful output fields:

```text
source_url
post_url
post_text/title/body
platform
community/group/source name
comment_count
reaction/score/like count
date
public author/profile pointer
```

### 2. Engagement Collection

Collect commenters/repliers first, because email only matters after intent.

Useful output fields:

```text
post_url
comment_id
comment_text
commenter_username
commenter_profile_url
likes/replies
timestamp
```

### 3. Profile/Email Enrichment

Only enrich retained users.

Useful output fields:

```text
profile_url
bio/about text
website_url
public_email
email_source_url
email_source_field
```

Reject if email is inferred, generated, guessed, or validated without public source.

## Candidate Actor Shortlist To Test

These are candidates from Apify research. They are not active until tested in the user's Console.

### Reddit

| Actor | Role | Why test |
|---|---|---|
| `solidcode/reddit-scraper` | source/post discovery + optional comments | Supports subreddit posts, Reddit search, top/month style use case, and specific post comments. |
| `crawlerbros/reddit-scraper` | source/post discovery | Scrapes subreddits without API key/login; posts with title/text/score/timestamps, optional comment threads. |
| `themineworks/reddit-scraper` | source/post discovery + comments | Supports subreddit/search/post modes and MCP; can pull top posts and comments. |
| `hipersoft/reddit-scraper` | source/post discovery + comments | No login; posts/comments/users/subreddits/search; useful if others fail. |

Reddit first test:

```json
{
  "subreddits": ["Forex", "Daytrading", "FTMO", "TradingView"],
  "sort": "top",
  "time": "month",
  "maxItems": 25,
  "skipComments": true
}
```

### Facebook

| Actor | Role | Why test |
|---|---|---|
| `lofomachines/facebook-groups-posts-search-scraper` | source/post discovery by phrase | Searches posts by keyword across public groups, no login/cookies/API key. Closest match to the article's Facebook method. |
| `automation-lab/facebook-group-posts-scraper` | public group posts | Public group URL input; output includes post URL, group URL, author, text, engagement. Good after groups are known. |
| `parseforge/facebook-groups-scraper` | public group posts | Public group posts by URL/slug; post text, author, timestamp, engagement. |
| `unseenuser/fb-posts` | pages/profiles/groups posts | General Facebook posts scraper for pages/profiles/public groups, no login. |

Facebook first test:

```json
{
  "keywords": ["how to pass FTMO", "XAUUSD help", "failed prop firm challenge", "ICT beginner help"],
  "maxPosts": 25,
  "dateRange": "last_month"
}
```

### Current Active / Observed Actors

Currently active or observed in this repo:

```text
BDec00yAmCm1QbMEI
SbK00X0JYCPblD2wp
apify/instagram-comment-scraper
```

`apify/instagram-comment-scraper` maps to `engagement-collector`, not direct email enrichment.

## Actor Evaluation Checklist

Pass if:

- public-only mode exists;
- no login/cookies/private group required;
- input schema is clear;
- output has source URL/post URL;
- output has author/commenter/profile pointer;
- engagement fields exist;
- pricing is visible;
- run/dataset IDs are available;
- actor can run a tiny test in Console.

Reject if:

- requires private groups or login session;
- collects hidden/private contact data;
- guesses emails;
- cannot preserve source evidence;
- mixes outreach/export into the actor;
- fails tiny Console test.

## Approval Boundary

Before any live actor run, create an approval packet with:

```yaml
actor_id:
actor_url:
pipeline_role:
input_summary:
max_items:
estimated_cost_usd:
budget_ceiling_usd:
uses_login_or_session: false
uses_private_sources: false
storage_target: local_csv_markdown
approval_status: requested
```
