# Apify Actor Test Protocol - Instagram Comments

Date: 2026-09-21
Repo: `scape-data`
Actor observed in Console: `apify/instagram-comment-scraper`
Pipeline role: `engagement-collector`

## Test Goal

Validate that the actor can collect public Instagram comments from public post/reel URLs and produce enough evidence for the `scape-data` email pipeline.

This actor does not prove email collection by itself. It collects commenters/engagement. Email enrichment must happen in a later `profile-enricher` step using a public profile/email actor or manual public-profile inspection.

## Safe Console Test

Use the Apify Console form with a tiny public-only test:

```yaml
instagram_posts_or_reels_urls:
  - https://www.instagram.com/p/DN8-GjPkgjS
  - https://www.instagram.com/reel/DDlJAfeyemG
number_of_comments: 15
include_replies: false
run_options:
  memory: 128 MB
  timeout: 30000s
```

Notes:

- Free usage may return only the top 15 comments sorted by newest.
- Keep `include_replies` off for the first test to reduce cost/noise.
- Do not use login cookies or private sources.
- Do not export full contact rows externally.

## Steps

1. Click `Save & start`.
2. Wait for the run to finish.
3. Open the run detail page.
4. Record:

```yaml
actor_id:
actor_name: apify/instagram-comment-scraper
run_id:
dataset_id:
started_at:
finished_at:
item_count:
actual_cost_usd:
status:
```

5. Open the dataset table.
6. Confirm whether output rows include these fields or equivalents:

```text
post_url / input_url
comment_id
comment_text / text
owner_username / username / author
owner_profile_url / profile_url / owner_id
timestamp / created_at
likes_count
replies_count
```

7. Export/download JSON or CSV only for local review.
8. Store local artifacts under:

```text
data/forex-social-intent/runs/<YYYYMMDD-HHMM>/
```

## Pass Criteria

Pass if:

- run status is succeeded;
- dataset has comment rows;
- each row points back to a public Instagram post/reel;
- each row has commenter identity or profile pointer;
- each row has comment text or a clear empty-text reason;
- no login/private/cookie source was used.

## Fail Criteria

Fail or mark review if:

- actor returns no rows for public URLs;
- rows lack commenter handles/profile pointers;
- rows lack post URL/source URL;
- actor requires login/session/private data;
- run cost exceeds the approved ceiling;
- dataset cannot be mapped to `engagement_table`.

## Mapping To Pipeline Table

Map actor output into `engagement_table`:

```text
platform              = instagram
post_url              = source post/reel URL
user_handle           = commenter username
profile_url           = commenter profile URL if available
engagement_type       = comment
text                  = comment text
likes                 = comment like count
replied_to            = parent comment id if available
collected_at          = run time or comment timestamp
actor_id              = actor id or apify/instagram-comment-scraper
run_id                = Apify run id
```

## Next Step After Pass

Run `buyer-intent-scorer` on the comments.

Do not try to get emails directly from this actor unless its dataset explicitly contains public profile/contact fields. If it only returns commenters/comments, pass the retained handles to `profile-enricher`.
