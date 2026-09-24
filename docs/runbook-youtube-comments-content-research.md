# YouTube Comments Content Research Runbook

## Purpose

Use public YouTube comments to create content strategy assets for another project:

```text
find videos -> collect public comments -> cluster pains/questions/phrases -> content angles/scripts -> memory note
```

This runbook is not for lead generation or email scraping.

## Skill

Use:

```text
youtube-comments-content-research
```

## File Structure

```text
.codex/skills/youtube-comments-content-research/
|-- SKILL.md
`-- references/
    |-- workflow.md
    `-- self-improvement.md

.ai/agents/content-research/
`-- youtube-comments-content-research.AGENT.md

.ai/commands/
`-- run-youtube-comments-content-research.md
```

## Minimal Operating Steps

1. Read the project/topic brief.
2. Retrieve only relevant prior artifacts for the same topic.
3. Prepare video discovery queries.
4. If a live/paid actor is needed, prepare exact input and budget for approval.
5. Collect public comments only.
6. Cluster comments by repeated pains, questions, objections, and phrases.
7. Convert clusters into content angles and scripts.
8. Run quality checks and remove unsupported ideas.
9. Write a memory note for reuse.

## Output Schema

Cluster rows:

```text
cluster_id
cluster_name
pain_or_question
audience_phrase
evidence_comment_ids
frequency
emotional_intensity
content_angle
recommended_format
script_hook
status
```

Script bank:

```text
angle_id
source_cluster_id
hook
problem
insight
steps_or_story
cta_or_next_action
evidence_comment_ids
```

## Quality Loop

Improve until either:

- unsupported angles are removed;
- duplicate clusters are merged;
- weak clusters are marked `needs_more_data`;
- two passes produce no meaningful improvement.

## Memory Output

Write:

```text
topic
audience
queries
source_video_count
comment_count
top_clusters
best_phrases
angles_created
failure_mode
next_safe_action
```
