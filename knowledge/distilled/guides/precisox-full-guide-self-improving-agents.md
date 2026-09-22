# Full Guide - Building Self-Improving Agents For This Repo

## Goal

Convert the reconstructed @precisox video script into a practical implementation guide for `scape-data`: Hermes runtime, multi-agent lead generation, Reddit sales, and `agent-lead-scraper`.

## The Complete System

```text
SOUL/AGENT contract
  -> bounded context retrieval
  -> task execution or draft generation
  -> quality evaluation
  -> error classification
  -> versioned fix proposal
  -> memory snapshot
  -> stop, continue, or request approval
```

## 1. Identity Contract Layer

Every runtime agent needs a compact identity file.

Required sections:

- Who I Am
- Scope
- Hard Rules
- Accountability Loop
- Stop Conditions
- Approval Gates
- Output Contract

Minimum acceptance criteria:

- The agent knows what it may do autonomously.
- The agent knows what requires approval.
- The agent knows what is forbidden.
- The agent has a self-check before delivery.

Recommended repo paths:

```text
.ai/agents/runtime-orchestrator/AGENT.md
.ai/agents/scrape-profile/AGENT.md
.ai/agents/market-intel/AGENT.md
.ai/agents/creative-planner/AGENT.md
.ai/agents/approval-gatekeeper/AGENT.md
.ai/agents/reporting/AGENT.md
```

## 2. Retrieval Layer

Retrieval should fetch the smallest useful context.

Records to index:

- source evidence;
- candidate records;
- scrape run history;
- prompt/config versions;
- approval records;
- memory snapshots;
- docs and playbooks.

Retrieval rules:

```yaml
default_top_k: 20
complex_top_k: 30-40
must_include_source_pointer: true
summary_requires_exact_pointer_for_claims: true
```

Implementation map:

- Current: `agent-lead-scraper/rag/`
- Needed: Hermes-level retrieval over `.ai/audit`, docs, knowledge, and state records.

## 3. Quality-Gated Loop Layer

Every loop needs an evaluation metric.

Examples:

| Agent | Quality metric | Stop rule |
|---|---|---|
| Scrape/Profile | dedup rate, validation rate, lead count, error count | stop after 2 non-improving runs |
| Market Intel | evidence coverage, source freshness, confidence | stop when evidence is missing or conflicting |
| Creative Planner | source-grounded claims, compliance risk, clarity | stop after 2 drafts do not improve |
| Approval Gatekeeper | evidence completeness, permission scope | stop on ambiguity |
| Reporting | metric consistency, missing blockers | stop if audit records conflict |

Implementation map:

- Current: `agent-lead-scraper/loop/terminate.py`
- Needed: shared loop policy in Hermes runtime docs.

## 4. Error Detection And Versioned Self-Fix

Error taxonomy:

- rate_limit_error
- actor_config_error
- parsing_error
- validation_error
- missing_evidence
- permission_boundary
- compliance_risk
- evaluation_missing
- unknown_error

Fix flow:

```text
detect -> classify -> root cause -> propose fix -> save version -> validate -> compare -> approve/apply/reject
```

Implementation map:

- Current: `agent-lead-scraper/error_fix/`
- Needed: approval record before production prompt/config changes.

## 5. Memory Compression Layer

Memory compression should create orientation, not replace evidence.

Snapshot fields:

```yaml
snapshot_id:
created_at:
agent:
run_ids:
source_ids:
approval_ids:
summary:
patterns:
open_questions:
next_safe_action:
```

Implementation map:

- Current: `agent-lead-scraper/memory/compress.py`
- Needed: cross-agent snapshots for Hermes state.

## 6. Permission And Safety Layer

Autonomous:

- read docs;
- retrieve public/source evidence;
- run mock/local tests;
- draft plans, reports, copy, tables, and fixes;
- write audit records.

Approval required:

- paid API/spend;
- outreach;
- publishing;
- login/account actions;
- lead transfer/resale;
- production prompt/config changes;
- larger batch sizes or new source classes.

Forbidden:

- proxy/fingerprint evasion;
- automated Reddit posting/voting/DMs;
- silent deletion/overwrite of records;
- unsupported claims or fabricated evidence;
- selling/transferring leads without approval.

## 7. End-To-End Hermes Runbook

1. Read `docs/agent-loop-operating-model.md`.
2. Read `docs/precisox-self-improving-agent-application.md`.
3. Read `.ai/rules/permission-matrix.md` and `.ai/rules/human-approval-gates.md`.
4. Create a run id.
5. Retrieve relevant context only.
6. Run draft/mock/in-ceiling work.
7. Evaluate quality.
8. Propose fixes if needed.
9. Save versions and audit records.
10. Compress memory with pointers.
11. Stop at approval gate or report next safe action.

## 8. Implementation Backlog

### Now

- Keep `knowledge/raw/video-notes/precisox-full-reconstructed-script.md` as source reconstruction.
- Use this guide as the canonical implementation guide.
- Link the project map into Hermes docs.

### Next

- Add individual `AGENT.md` contracts under `.ai/agents/`.
- Add deterministic tests for no-key RAG skip, config path, memory path, error handling, and convergence.
- Add audit schema files for run, evidence, draft, approval, spend, and memory snapshot.

### Later

- Add a real state store.
- Add semantic index over knowledge/docs/audit records.
- Add dashboard for approvals and blocked runs.

## Acceptance Criteria

- Agent behavior is defined by files, not one-off prompts.
- Retrieval is bounded and source-linked.
- Loops stop by quality, not vibes.
- Fixes are versioned and reviewed.
- Memory summaries point back to exact records.
- Hermes cannot cross external-impact gates without approval.