# Workflow

## Goal

Transform public YouTube comments into reusable content research for another project.

Do not optimize for leads, email yield, creator contacts, or sales outreach. Optimize for:

```text
audience language
repeated pains
questions
objections
misconceptions
desired outcomes
content hooks
scriptable stories
```

## Inputs

Accept any of these:

- topic or niche;
- offer or product brief;
- target audience description;
- seed YouTube channels/videos;
- local comment datasets;
- approved actor output.

## Video Discovery

Prefer videos where the audience is likely to reveal problems:

- beginner tutorials;
- "mistakes" videos;
- reviews and comparisons;
- "why I quit/failed" stories;
- case studies;
- controversial or myth-busting videos;
- Q&A/live replay videos.

Avoid over-sampling creator announcement videos where comments are mostly praise.

## Comment Collection

Collect public comments only. For tiny tests, use:

```yaml
max_queries: 3
max_videos_per_query: 3
max_comments_per_video: 50
replies: optional
login: false
cookies: false
```

Store raw output locally if a run is approved. Keep source URLs and comment IDs so every insight can be traced.

## Clustering

Cluster comments by audience meaning, not exact wording.

Recommended cluster types:

```text
pain
question
objection
desired_outcome
confusion
mistake
comparison
tool_request
story
phrase_bank
```

For each cluster, extract:

```text
what they are struggling with
what they already tried
what they fear
what words they repeat
what they want next
what content would help
```

## Content Outputs

Produce:

- 5-15 content angles;
- hook lines in the audience's words;
- short-form script outlines;
- long-form video outlines when useful;
- FAQ/questions list;
- objection-handling content ideas;
- phrase bank for titles/thumbnails.

Every angle should include evidence:

```text
angle
source_cluster
evidence_comment_ids
why_it_matters
suggested_format
hook
outline
```

## Quality Loop

After drafting clusters and angles, run a review pass:

1. Remove angles that are generic or not supported by comments.
2. Merge duplicate clusters.
3. Split clusters that mix different pains.
4. Check that hooks use real audience language.
5. Flag low-evidence clusters as `needs_more_data`.

Stop after two passes with no meaningful improvement.

## Error Detection

Flag a run as flawed when:

- clusters are based on creator claims instead of audience comments;
- more than 30% of angles lack evidence comment IDs;
- praise comments dominate the dataset;
- the result turns into lead scraping or email enrichment;
- comments are too generic to support content decisions;
- the source set is too narrow for the user's stated audience.
