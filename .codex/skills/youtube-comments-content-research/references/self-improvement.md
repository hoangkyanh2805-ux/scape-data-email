# Self-Improvement Rules

This skill follows the repo's `AGENT-SELF-IMPROVING-GUIDE.md`, adapted for content research.

## Soul / Hard Rules

The agent's identity is evidence-first content research. Its job is to help creators hear the audience clearly.

Hard rules:

- Real comments beat assumptions.
- Content angles need traceable evidence.
- Do not convert content research into lead generation.
- Do not publish or outreach.
- Improve precision, usefulness, traceability, or cost per useful insight.

## RAG / Relevant Artifact Retrieval

Retrieve only the top relevant artifacts for the current content topic:

```text
offer_or_topic_brief
seed_queries
source_videos
raw_comments
prior_cluster_outputs
prior_content_angles
prompt_history_for_same_topic
memory_notes_for_same_topic
```

Do not load unrelated lead batches, old Telegram profiles, CRM exports, or unrelated project memories.

Use semantic relevance over keyword-only retrieval when selecting prior comments or insights. Start with top 20 relevant artifacts; expand only if the topic is broad or multi-segment.

## Quality Loop

Track these metrics per iteration:

```text
supported_angle_count
unsupported_angle_count
duplicate_cluster_count
average_evidence_per_angle
high_intensity_cluster_count
generic_angle_rate
```

Continue only when the next pass improves at least one useful metric without losing evidence traceability.

Stop when:

- two consecutive passes do not improve the output;
- the dataset is too thin and needs more comments;
- the user requested only a quick synthesis.

## Error Detection

Detect and log an error when:

- content ideas are generic and not comment-backed;
- comments were collected from videos that do not match the target audience;
- praise/noise dominates the sample;
- the run starts collecting emails, leads, or contact details;
- a prompt causes the model to invent pains not present in the comments;
- source evidence is missing from output rows.

## Prompt Fix Log

When a prompt or workflow causes bad output, write a versioned note under:

```text
content-research/error_fix/prompt_history/
```

Each note should include:

```json
{
  "timestamp": "",
  "task": "",
  "bad_signal": "",
  "root_cause": "",
  "prompt_or_workflow_fix": "",
  "expected_metric_improvement": "",
  "keep_fix_if": ""
}
```

Only keep the fix if a later run improves evidence coverage, specificity, cluster quality, or cost per useful insight.

## Memory Output

Each run should emit one concise memory note:

```json
{
  "topic": "",
  "audience": "",
  "source_queries": [],
  "source_video_count": 0,
  "comment_count": 0,
  "top_clusters": [],
  "best_audience_phrases": [],
  "content_angles_created": 0,
  "main_failure_mode": "",
  "next_safe_action": ""
}
```
