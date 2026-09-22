# Project Mapping Checklist

## Source Pattern

```text
identity -> retrieval -> quality loop -> versioned self-fix -> memory snapshot -> approval gate
```

## Target Mapping Questions

- What is the target project's main recurring workflow?
- What source evidence does the workflow rely on?
- Which actions are internal drafts only?
- Which actions affect users, money, production data, accounts, or external systems?
- What metrics prove improvement?
- What records must be audited?
- What memory should be compressed, and where are exact pointers stored?

## Six-Agent Mapping

| Default agent | Map to target project |
|---|---|
| runtime-orchestrator | Overall run coordinator |
| soul-contract | Agent contract maintainer |
| rag-context | Context/evidence retriever |
| scrape-profile | Domain executor or profiler |
| error-fix | Prompt/config fix proposer |
| memory-audit | Snapshot and audit reporter |

## Acceptance Criteria

- Target has a runbook and install report.
- Target has explicit approval gates.
- Target has audit schemas or equivalent records.
- No existing target files were overwritten unexpectedly.
- First live run is still draft-only or approval-gated.