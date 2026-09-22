# Clone Runbook

## Inputs

- Source bundle path, default: `bundles/self-improving-agent-os/`.
- Target project path.
- Target project domain or workflow.
- Whether to copy only bundle docs or activate `.ai/` runtime files.

## Target Inventory

Inspect:

- README and docs;
- package/build/test files;
- existing `.ai/`, `.codex/`, `.agents/`, `docs/`, `scripts/`;
- deployment/runtime notes;
- data stores and external integrations;
- permission or compliance docs.

## Copy Modes

### Bundle-only mode

Copy to:

```text
agent-os/self-improving-agent-os/
```

Use when the user wants a reusable package but not active runtime setup.

### Active runtime mode

Copy/adapt:

```text
.ai/agents/
.ai/rules/
.ai/schemas/
.ai/runbooks/
docs/self-improving-agent-os-project-map.md
docs/self-improving-agent-os-install-report.md
```

Use when the user wants the target repo to run the agent OS.

## Mapping Rules

- Map existing workflows to six default agents before adding new agents.
- Keep production-specific tools behind approval gates.
- Mark all unknown external integrations as approval-required.
- Write target-specific quality metrics for each active agent.
- Keep memory snapshots pointer-based.

## Install Report Template

```markdown
# Self-Improving Agent OS Install Report

## Target Project

## Source Bundle

## Copy Mode

## Files Added

## Files Updated

## Existing Conflicts

## Target Agent Map

## Approval Gates Preserved

## Missing Inputs

## Next Safe Action
```