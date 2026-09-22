# Run Output Template

Use this at the end of each run or when stopping at an approval gate.

## Run Summary

- Mode: <core monitoring / product discovery / selling / ops>
- Objective: <what the user asked for>
- Status: <draft complete / queued / blocked / approval needed>
- Inputs used: <subreddits, product, niche, dashboard target>
- Missing inputs: <only required missing items>

## Artifacts Created

| Artifact | Location or table | Status | Notes |
|---|---|---|---|
| <name> | <path/url/table> | draft/queued/review | <short note> |

## Subreddit And Feed Status

- Subreddits monitored: <list>
- Pull count: <number>
- Rate-limit status: <ok / warning / blocked>
- Profile changes: <summary>

## Queued Human Actions

| Action | Subreddit | Link | Urgency | Risk note |
|---|---|---|---|---|
| <reply/post/review> | <subreddit> | <permalink/submit link> | <high/medium/low> | <note> |

## Review Items

| Item | Why review is needed | Recommended decision |
|---|---|---|
| <niche/thread/draft/rule/account> | <uncertainty or risk> | <approve/reject/edit/inspect> |

## Skipped Items

- <item>: <reason>

## Approval Gate

- Gate reached: <post/comment/DM/link/publish/spend/notification/none>
- What approval or human action would allow: <specific next action>
- Evidence provided: <draft, count, cost, rule notes, source links>

## Next Safe Action

Recommended next safe action: <one action that does not violate the permission matrix>

## Stop Report

Stopped because: <condition>
Goal affected: <mode goal>
Evidence: <links, logs, profile notes, table rows, drafts>
Safe next options: <2-3 choices>
Recommended option: <one choice>
Approval/input needed: <specific request>
