# Precisox Self-Improving Agent Playbook For This Project

## Purpose

Turn the @precisox self-improving agent video pattern into reusable operating rules for this repo: lead generation, Reddit sales, Hermes runtime, and `agent-lead-scraper`.

## Source Formula

```text
soul.md -> semantic RAG -> quality-gated loop -> versioned self-fix -> compressed memory with source pointers
```

## Project Formula

```text
agent contract -> approved context retrieval -> draft/execute loop -> measurable checks -> stop or approval -> audit snapshot
```

## Current Project Equivalent

| Video pattern | Existing repo asset | Gap to close |
|---|---|---|
| `soul.md` identity | `agent-lead-scraper/soul.md`, `.ai/agents/multi-agent-contracts.md` | Add concise soul/contract files for each runtime agent role. |
| RAG top-k context | `agent-lead-scraper/rag/` | Add evidence retrieval specs for Hermes state records. |
| Quality-gated loop | `agent-lead-scraper/loop/terminate.py`, `docs/agent-loop-operating-model.md` | Use same convergence rule across creative drafts, reports, and approvals. |
| Error self-fix | `agent-lead-scraper/error_fix/` | Require approval before applying self-fixes to production runtime. |
| Memory compression | `agent-lead-scraper/memory/`, `.ai/audit/checklist.md` | Store summaries with exact source/run/approval pointers. |

## Agent Contract Template

Use this for every Hermes or Codex runtime agent.

```markdown
# <Agent Name>

## Who I Am
I am a <role> agent for <business workflow>. I optimize for verified output, auditability, and safe handoff.

## Scope
- I may: <autonomous actions>
- I must draft only: <external-impact work>
- I must never: <forbidden actions>

## Hard Rules
- Never fabricate sources, metrics, or approvals.
- Separate source facts from inference.
- Stop before money, outreach, publishing, account actions, or lead transfer.
- Preserve source pointers for every important claim.
- Log every config/prompt self-improvement proposal.
- If confidence is low, mark review instead of approved.

## Accountability Loop
Before every substantive output, check:
1. Did I attach evidence or say evidence is missing?
2. Did I stay inside the permission matrix?
3. Is the next action autonomous, approval-required, or forbidden?

If any answer fails, stop and produce the standard stop report.

## Stop Report
Stopped because:
Goal affected:
Evidence:
Safe next options:
Recommended option:
Approval/input needed:
```

## Implementation Playbook

### 1. Identity Layer

Create or verify a concise contract for each agent:

- Runtime Orchestrator Agent
- Scrape/Profile Agent
- Market Intel Agent
- Creative Planner Agent
- Approval Gatekeeper Agent
- Reporting Agent

Acceptance check: each contract includes scope, hard rules, accountability loop, stop conditions, and approval gates.

### 2. Retrieval Layer

Use semantic retrieval for:

- prior scrape runs;
- source evidence;
- candidate records;
- approval records;
- prior prompt/config fixes;
- memory snapshots.

Rules:

- Start with `top_k: 20` for normal tasks.
- Increase to 30-40 only for multi-hop or cross-agent synthesis.
- Never rely on compressed memory for exact claims. Follow the pointer to the source record.

### 3. Loop Layer

All self-improving loops should follow:

```text
run -> evaluate -> propose improvement -> validate -> log -> continue/stop/approval
```

Stop when:

- two iterations do not improve;
- three tool/API failures occur;
- rate limit or budget ceiling is hit;
- next action crosses an approval gate;
- the evaluation metric is missing or unreliable.

### 4. Error Self-Fix Layer

Allowed autonomously:

- classify an error;
- propose a config/prompt fix;
- save a versioned proposal;
- run mock or in-ceiling validation.

Approval required:

- applying fix to production runtime;
- increasing spend, batch size, actor count, retries, or external reach;
- changing permission/approval behavior.

### 5. Memory Layer

Every long-running agent should write compact memory while preserving pointers:

```yaml
snapshot_id:
created_at:
agent:
run_ids:
source_ids:
approval_ids:
summary:
open_questions:
blocked_items:
next_safe_action:
```

Acceptance check: a human can reconstruct why the agent chose a candidate, draft, or stop condition by following ids back to exact evidence.

## Project-Specific Next Actions

1. Add per-agent `SOUL.md` or `AGENT.md` style contracts under `.ai/agents/`.
2. Extend Hermes runtime docs with a state schema for `source_evidence`, `candidate`, `draft`, `approval`, `spend`, and `lead_transfer`.
3. Add deterministic tests for the scraper loop: no API key path, config path, RAG disabled, failure handling, and memory snapshot location.
4. Add a prompt/config fix approval record before production self-improvement.
5. Add an audit report command that prints: run id, evidence ids, approvals pending, cost status, and next safe action.

## What Not To Copy Blindly

- Do not treat `top_k: 20` as universal.
- Do not let compressed summaries replace exact evidence.
- Do not let agents self-edit production behavior silently.
- Do not automate outreach, Reddit posting, lead transfer, ad spend, or publishing.
- Do not use a personality file as a substitute for permissions, tools, tests, or audit logs.

## Suggested File Map

```text
knowledge/raw/video-notes/precisox-self-improving-agent-video-notes.md
knowledge/distilled/playbooks/precisox-self-improving-agent-playbook.md
.ai/agents/<agent-name>/SOUL.md
.ai/agents/<agent-name>/AGENT.md
docs/hermes-runtime-architecture.md
docs/agent-loop-operating-model.md
agent-lead-scraper/HERMES_ADAPTER.md
```

## Acceptance Criteria

- The source note clearly states that no public transcript was available.
- The distilled playbook gives reusable agent rules rather than a loose summary.
- Every proposed autonomous behavior is bounded by approval gates.
- The implementation map points to existing repo files and concrete next actions.
- The playbook can be handed to Hermes/Codex as an operating reference without rereading the video.