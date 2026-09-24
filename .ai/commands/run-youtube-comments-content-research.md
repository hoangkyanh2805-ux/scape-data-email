# Command: run-youtube-comments-content-research

Use this command when a project needs YouTube comments for content research, not lead/email scraping.

## Agent Sequence

```text
approval-gate-reporter
-> source-finder
-> video-collector
-> comment-collector
-> pain-clusterer
-> content-angle-builder
-> script-drafter
-> quality-reviewer
-> memory-writer
```

## Default Tiny Test

Prepare approval before any paid actor run:

```json
{
  "source": "youtube",
  "queries": [
    "PASTE_TOPIC beginner mistakes",
    "PASTE_TOPIC questions",
    "PASTE_TOPIC review"
  ],
  "maxVideosPerQuery": 3,
  "maxCommentsPerVideo": 50,
  "includeReplies": false,
  "login": false,
  "cookies": false,
  "email_enrichment": false,
  "outreach": false
}
```

## Required Outputs

```text
source_videos.csv
raw_comments.json
comment_clusters.csv
content_angles.md
script_bank.md
content_research_report.md
memory_note.json
```

## Review Gate

Reject the run if it turns into:

```text
email scraping
lead scoring
creator harvesting
outreach
unsupported generic content ideas
```
