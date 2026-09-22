# Runbook - Hermes Self-Improving Agent Run

## Purpose
Run this project's six-agent self-improving loop safely and repeatably.

## Agent Set

1. `runtime-orchestrator`: coordinates the run and gates external impact.
2. `soul-contract`: checks agent identity contracts.
3. `rag-context`: retrieves bounded context with source pointers.
4. `scrape-profile`: runs mock/approved scrape workflows and metrics.
5. `error-fix`: proposes versioned fixes.
6. `memory-audit`: writes snapshots and audit summaries.

## Preflight

- Read `docs/agent-loop-operating-model.md`.
- Read `docs/precisox-self-improving-agent-application.md`.
- Read `.ai/rules/permission-matrix.md`.
- Read `.ai/rules/human-approval-gates.md`.
- Confirm `draft_only: true` unless an approval id exists.
- Confirm tool inventory, storage destination, and quota ceilings.

## Standard Run

```text
1. runtime-orchestrator creates run_id.
2. soul-contract verifies contracts.
3. rag-context retrieves context packet.
4. scrape-profile runs mock/free/approved work.
5. error-fix proposes and versions fixes if needed.
6. memory-audit writes snapshot.
7. runtime-orchestrator emits report or approval request.
```

## Stop Conditions

Stop immediately when:

- required input is missing;
- two iterations do not improve;
- three repeated tool failures occur;
- a rate limit, budget warning, or quota ceiling is reached;
- evidence is missing or contradictory;
- the next action touches spend, outreach, publishing, account login, production policy, or lead transfer.

## Stop Report

```text
Stopped because:
Goal affected:
Evidence:
Safe next options:
Recommended option:
Approval/input needed:
```

## Final Report

Each final report must include:

- run id;
- agents used;
- retrieved context ids;
- source evidence ids;
- metrics;
- prompt/config versions;
- approval request ids;
- memory snapshot id;
- termination reason;
- next safe action.