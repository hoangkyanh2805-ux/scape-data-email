# SOP - Self-Improving Agent OS

## Objective
Operate a six-agent self-improving system based on the video pattern: identity contract, bounded retrieval, quality-gated loop, versioned self-fix, and compressed memory with source pointers.

## Operating Principles

- Start draft-only.
- Retrieve relevant context, not full history.
- Stop by quality gates, not vibes.
- Version every prompt/config fix.
- Summarize memory with exact pointers.
- Convert external-impact actions into approval requests.

## Roles

| Agent | Responsibility |
|---|---|
| Runtime Orchestrator | Run lifecycle, delegation, gates, report |
| Soul Contract | Contracts, hard rules, accountability loops |
| RAG Context | Bounded context and evidence pointers |
| Scrape Profile | Scrape/profile execution and metrics |
| Error Fix | Error classification and versioned fixes |
| Memory Audit | Snapshots, audit completeness, next safe action |

## Procedure

1. Define goal and required output.
2. Create run id and run record.
3. Load permission matrix and approval gates.
4. Retrieve source context with pointers.
5. Execute only mock, draft, local, or in-ceiling actions.
6. Evaluate quality with metrics.
7. Propose and version any fixes.
8. Stop on approval gates or continue if fully autonomous.
9. Write memory snapshot and final report.
10. File follow-up tasks for missing tests, schemas, or approvals.

## Quality Gates

- Two non-improving iterations stop the loop.
- Three repeated tool failures stop the loop.
- Missing evidence stops approval-sensitive outputs.
- Compressed memory must not replace exact evidence.
- Production behavior changes require approval.

## Evidence Standard

Every important claim must trace to one of:

- file path;
- URL;
- source evidence id;
- run id;
- approval id;
- prompt/config version id;
- memory snapshot id plus exact source pointer.

## Handoff

A handoff is complete only when the next operator can answer:

- What was attempted?
- What evidence was used?
- What changed?
- What stopped the run?
- What approval/input is needed?
- What is the next safe action?