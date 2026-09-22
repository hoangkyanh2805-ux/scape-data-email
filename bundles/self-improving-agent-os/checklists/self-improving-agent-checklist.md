# Hermes Self-Improving Agent Checklist

Use this checklist before running Hermes or any multi-agent workflow that claims to self-improve.

## 1. Identity

- [ ] Agent has an `AGENT.md`, `SOUL.md`, or equivalent contract.
- [ ] Contract defines role, scope, hard rules, and output contract.
- [ ] Contract names approval gates and forbidden actions.
- [ ] Agent has an accountability loop.

## 2. Retrieval

- [ ] Agent retrieves bounded context, not full history.
- [ ] Default `top_k` is documented.
- [ ] Retrieved items have source ids or file paths.
- [ ] Compressed memory is not used as exact evidence without pointer lookup.

## 3. Loop

- [ ] Loop has measurable quality metrics.
- [ ] Loop has max iterations.
- [ ] Loop stops after 2 non-improving iterations.
- [ ] Loop stops after 3 repeated tool failures.
- [ ] Loop logs termination reason.

## 4. Error Self-Fix

- [ ] Error is classified.
- [ ] Root cause is written down.
- [ ] Prompt/config fix is saved as a versioned proposal.
- [ ] Fix is tested in mock, dry-run, or approved quota.
- [ ] Production behavior change has approval id.

## 5. Memory

- [ ] Snapshot includes run ids.
- [ ] Snapshot includes source evidence ids.
- [ ] Snapshot includes approval ids when relevant.
- [ ] Snapshot names open questions and next safe action.
- [ ] Exact claims can be traced to original records.

## 6. Safety Gates

Stop and request approval before:

- [ ] spend or paid API usage beyond ceiling;
- [ ] outreach or messaging;
- [ ] publishing;
- [ ] login/account actions;
- [ ] lead transfer or sale;
- [ ] production prompt/config policy changes;
- [ ] larger batch sizes, new actors, or new source classes.

## 7. Run Record

Each run must include:

```yaml
run_id:
agent:
goal:
inputs:
retrieved_context_ids:
source_evidence_ids:
metrics:
prompt_or_config_version:
termination_reason:
approval_request_id:
memory_snapshot_id:
next_safe_action:
```

## Pass Condition

Hermes may continue autonomously only when every next action is inside the permission matrix, evidence is sufficient, quality is measurable, and the action has no external impact.