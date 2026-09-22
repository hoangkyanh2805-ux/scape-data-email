# Runbook - Map And Clone To A New Project

## Purpose
Clone the self-improving agent OS bundle into a target project and adapt it without enabling unsafe autonomy.

## Inputs

- Target project path.
- Copy mode: `bundle-only` or `active-runtime`.
- Target domain/workflow.
- Source bundle path, default: `bundles/self-improving-agent-os/`.

## Procedure

1. Inspect target project docs, scripts, existing agent folders, and runtime notes.
2. Inspect source bundle manifest.
3. Identify conflicts before writing files.
4. Copy bundle to `agent-os/self-improving-agent-os/` in target project.
5. For active runtime, adapt `.ai/agents`, `.ai/rules`, `.ai/schemas`, `.ai/runbooks`.
6. Write `docs/self-improving-agent-os-project-map.md`.
7. Write `docs/self-improving-agent-os-install-report.md`.
8. Verify copied files and list any skipped conflicts.
9. Stop before live external tools or production behavior changes.

## Install Report Minimum

```yaml
target_project:
source_bundle:
copy_mode:
files_added:
files_updated:
files_skipped:
conflicts:
agent_map:
approval_gates:
missing_inputs:
next_safe_action:
```

## Pass Criteria

- No target file was overwritten unexpectedly.
- Approval gates remain intact.
- Six-agent map is present or gaps are explicit.
- Target has a next safe action.