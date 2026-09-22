# Precisox Self-Improving Agent Application

## Source Status

Source video: https://x.com/precisox/status/2076152320585343132/video/1

Public mirror checked: https://threadnavigator.com/thread/2076152320585343132/

A public full transcript was not available during capture. This document is an application note based on public chapter timestamps, local reconstructed notes, and the current project architecture. It is not a verbatim transcript.

Detailed source note: `knowledge/raw/video-notes/precisox-self-improving-agent-video-notes.md`

Full guide: `knowledge/distilled/guides/precisox-full-guide-self-improving-agents.md`

Distilled playbook: `knowledge/distilled/playbooks/precisox-self-improving-agent-playbook.md`

Knowledge index: `knowledge/precisox-self-improving-agent-index.md`

## Five Pillars To Apply

```text
identity contract -> relevant memory -> quality-gated loop -> versioned self-fix -> compressed audit memory
```

## How This Maps To The Repo

| Pillar | Repo implementation | Hermes/multi-agent rule |
|---|---|---|
| `soul.md` identity | `agent-lead-scraper/soul.md`, `.ai/agents/multi-agent-contracts.md` | Every agent needs a short role contract with hard rules and accountability checks. |
| Semantic retrieval | `agent-lead-scraper/rag/` | Retrieve relevant evidence and run history. Do not load full history into the prompt. |
| Quality gate | `agent-lead-scraper/loop/terminate.py` | Stop after 2 non-improving iterations or missing metrics. |
| Error self-fix | `agent-lead-scraper/error_fix/` | Draft and version fixes. Approval required before production behavior changes. |
| Memory compression | `agent-lead-scraper/memory/` | Summaries must include pointers to exact run/source/approval records. |

## Hermes Bootstrap Checklist

1. Read `docs/agent-loop-operating-model.md`.
2. Read `docs/permission-matrix.md` and `docs/human-approval-gates.md`.
3. Read this file.
4. Start with `draft_only: true`.
5. Create a `run_id` and audit record.
6. Retrieve only relevant project context.
7. Produce draft artifacts and evidence logs.
8. Stop at any approval gate.
9. Save a memory snapshot with source pointers.

## Agent Contract Checklist

Each runtime agent must define:

- Who I am.
- What I may do autonomously.
- What requires approval.
- What is forbidden.
- Evidence requirements.
- Quality metric.
- Stop conditions.
- Accountability loop.

## Self-Improvement Loop

Use this loop for scraper configs, prompt fixes, creative drafts, reports, and runtime proposals:

```text
observe -> retrieve -> act/draft -> evaluate -> propose fix -> version -> compare -> continue/stop/approval
```

Stop when:

- two iterations do not improve;
- three tool failures repeat;
- a rate limit or budget ceiling is reached;
- evidence is missing or contradictory;
- evaluation cannot prove improvement;
- the next action touches spend, outreach, publishing, account login, lead transfer, or production policy.

## Audit Record Minimum

```yaml
run_id:
agent:
goal:
inputs:
retrieved_context_ids:
source_evidence_ids:
draft_artifact_ids:
prompt_or_config_version:
metrics:
termination_reason:
approval_request_id:
memory_snapshot_id:
next_safe_action:
```

## Direct Application To `agent-lead-scraper`

- Keep `LoopTerminator` as the canonical convergence pattern.
- Keep prompt/config fixes in `error_fix/prompt_history/`.
- Keep memory snapshots in `memory/snapshots/`.
- Treat RAG as optional enhancement when keys are missing, not a blocker for mock/draft runs.
- Add deterministic tests before using real Apify actors.
- Require approval for paid actor runs, bigger batches, exports, or production config changes.

## What To Avoid

- Do not store a long reconstructed transcript as if it were verified source text.
- Do not treat `top_k: 20` as universal.
- Do not let compressed memory replace exact source evidence.
- Do not let self-improvement mutate production prompts silently.
- Do not let Hermes execute outreach, publishing, spend, account actions, or lead transfer without approval.