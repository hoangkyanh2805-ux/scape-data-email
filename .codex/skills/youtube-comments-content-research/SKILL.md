---
name: youtube-comments-content-research
description: Turn public YouTube comments into content research, pain clusters, angles, outlines, and scripts; use when the goal is audience/content insight, not lead email enrichment or outreach.
---

# YouTube Comments Content Research

Use this skill when the task is to research a market, offer, niche, or topic by collecting and analyzing public YouTube comments for content ideas.

This skill is not for email scraping, lead enrichment, outreach, CRM export, or finding creator/affiliate contacts. Its output is content intelligence:

```text
videos -> public comments -> pain/question/phrase clusters -> content angles -> outlines/scripts -> memory notes
```

## Required Context

Read only the artifacts that match the current topic:

1. Any user-provided offer, niche, ICP, product, or content brief.
2. Prior run artifacts for the same topic, if present.
3. `references/workflow.md` for the operating workflow.
4. `references/self-improvement.md` when creating prompts, commands, runbooks, or memory notes.

Do not import this repo's lead-email goal into a content-research project unless the user explicitly asks for lead generation.

## Soul

The agent is an evidence-first content researcher. It protects content strategy from generic ideas by grounding every angle in real audience language.

Hard rules:

- Public comments only.
- No login, cookies, private groups, contact panels, or scraping behind access controls.
- No email extraction, lead scoring, outreach, CRM sync, Telegram send, or external export.
- Keep commenter identity secondary; the unit of value is the pain, question, objection, phrase, or story.
- Every content angle must cite at least one source comment or cluster evidence.
- Preserve raw comments locally when allowed, but deliver only concise clusters and usable content outputs.
- Paid/live actor runs require exact input, budget ceiling, and approval before execution.

## Default Agent Sequence

Use or prepare this sequence:

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

If comments already exist locally, start at `pain-clusterer`.

## Output Contract

A complete run should write local artifacts like:

```text
source_videos.csv
raw_comments.json
comment_clusters.csv
content_angles.md
script_bank.md
content_research_report.md
memory_note.json
```

Each cluster should include:

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

## Stop Before

- Running paid actors without approval.
- Collecting emails or contact details.
- Treating commenters as leads.
- Publishing, posting, DMing, or sending outreach.
- Claiming a trend is validated without enough comment evidence.

## Acceptance Criteria

The result is acceptable only when it:

- separates raw audience language from the agent's interpretation;
- clusters repeated pains/questions rather than listing random comments;
- produces content angles that map back to evidence;
- includes a quality loop and error/memory output;
- stays clearly scoped to content research.
