---
name: self-improving-agent-os-cloner
description: Map and clone this repo's self-improving agent OS bundle into a new project, adapting agents, rules, schemas, SOPs, runbooks, and approval gates without overwriting target project work.
---

# Self-Improving Agent OS Cloner

Use this skill when the user wants to copy, clone, install, port, map, or adapt the self-improving agent OS bundle into another project.

## Core Outcome

Produce a target-project operating layer that preserves the source pattern:

```text
identity contract -> bounded retrieval -> quality-gated loop -> versioned self-fix -> memory snapshot -> approval gate
```

## Required Behavior

- Inspect the target project before copying files.
- Keep target project files intact unless the user explicitly asks for replacement.
- Prefer creating or updating `.ai/`, `docs/`, and `agent-os/` layers rather than moving production files.
- Preserve draft-first, evidence-backed, approval-gated behavior.
- Stop before enabling spend, outreach, publishing, account actions, production prompt/config changes, or lead transfer.

## Source Bundle

Default source in this repo:

```text
bundles/self-improving-agent-os/
```

If the source bundle is missing or the task is in another repo, ask for the source bundle path or recreate the minimum bundle from this skill's references.

## Workflow

1. Inventory target project: docs, scripts, existing `.ai/`, permissions, deploy/runtime notes, tests, and data stores.
2. Read [references/clone-runbook.md](references/clone-runbook.md).
3. Read [references/project-mapping-checklist.md](references/project-mapping-checklist.md).
4. Copy the bundle into `agent-os/self-improving-agent-os/` or another user-specified path.
5. Adapt agent contracts for the target domain.
6. Add target-specific project map and install report.
7. Verify copied files exist and no external-impact actions were enabled.

## Default Deliverables

- `agent-os/self-improving-agent-os/` bundle copy.
- `.ai/agents/project-map-cloner/AGENT.md` or target equivalent.
- `docs/self-improving-agent-os-install-report.md`.
- `docs/self-improving-agent-os-project-map.md`.
- Optional target `.ai/rules/`, `.ai/schemas/`, `.ai/runbooks/` if the user wants active runtime setup.

## Stop Conditions

Stop and ask for input when:

- target path is unclear;
- copying would overwrite non-generated target files;
- target project already has conflicting agent rules;
- user asks to enable live external tools without approval gates;
- source bundle cannot be found and reconstruction would be incomplete.