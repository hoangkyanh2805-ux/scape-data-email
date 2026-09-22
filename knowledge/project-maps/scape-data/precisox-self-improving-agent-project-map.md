# Project Map - Precisox Self-Improving Agent Pattern To Scape Data

## Source Formula

```text
identity -> retrieval -> quality loop -> versioned self-fix -> compressed memory
```

## Current Project Equivalent

| Source layer | Scape-data equivalent | Status |
|---|---|---|
| Identity | `agent-lead-scraper/soul.md`, `.ai/agents/multi-agent-contracts.md` | partial |
| Retrieval | `agent-lead-scraper/rag/` | implemented for scraper, missing Hermes-wide index |
| Quality loop | `agent-lead-scraper/loop/` | implemented for scraper |
| Error self-fix | `agent-lead-scraper/error_fix/` | implemented as proposal/versioning base |
| Memory compression | `agent-lead-scraper/memory/` | implemented for scraper |
| Approval gates | `docs/permission-matrix.md`, `docs/human-approval-gates.md` | documented |
| Hermes runtime | `docs/hermes-runtime-architecture.md`, `agent-lead-scraper/HERMES_ADAPTER.md` | documented, not fully automated |

## Knowledge Assets Created

- Raw/reconstructed script: `knowledge/raw/video-notes/precisox-full-reconstructed-script.md`
- Full implementation guide: `knowledge/distilled/guides/precisox-full-guide-self-improving-agents.md`
- Existing project application note: `docs/precisox-self-improving-agent-application.md`
- This project map: `knowledge/project-maps/scape-data/precisox-self-improving-agent-project-map.md`

## What To Apply Immediately

1. Treat `agent-lead-scraper` as the reference implementation.
2. Treat Hermes as the orchestrator and gatekeeper, not a permission bypass.
3. Keep all new leadgen/reddit workflows draft-first.
4. Require run ids, evidence ids, prompt/config version ids, approval ids, and memory snapshot ids.
5. Stop after two non-improving iterations or three repeated tool failures.

## Missing Assets

- `.ai/agents/<role>/AGENT.md` per specialist agent.
- `.ai/schemas/run.yaml`, `source_evidence.yaml`, `approval.yaml`, `memory_snapshot.yaml`.
- Test suite for `agent-lead-scraper` with deterministic mock behavior.
- Hermes approval dashboard or queue.
- Semantic index over docs, knowledge, and audit records.

## Implementation Sequence

### Phase 1 - Contracts

Create role-specific agent contracts for:

- runtime orchestrator;
- scrape profile;
- market intel;
- creative planner;
- approval gatekeeper;
- reporting.

### Phase 2 - Schemas

Create audit schemas for:

- run;
- source evidence;
- draft artifact;
- approval;
- prompt/config version;
- memory snapshot.

### Phase 3 - Tests

Add tests for:

- config path independence;
- RAG disabled without key;
- error_type in run history;
- memory snapshot path;
- termination after non-improvement;
- approval gate stop report.

### Phase 4 - Runtime

Wire Hermes to:

- read contracts;
- create run id;
- retrieve bounded context;
- execute draft/mock tasks;
- write audit records;
- stop at approval gates;
- emit final report.

## Acceptance Criteria

- New agents can onboard by reading docs and `.ai/` without inspecting old chat history.
- Every self-improvement proposal is traceable and reversible.
- Every external-impact action has approval evidence.
- Every memory summary points back to exact records.
- The system can run a dry-run Hermes batch safely.