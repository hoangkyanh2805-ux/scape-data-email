# Bundle Index

## Files

- `README.md`: bundle overview and non-negotiable rules.
- `bundle.yaml`: machine-readable manifest.
- `agents/*.AGENT.md`: six default agent contracts.
- `rules/permission-matrix.md`: autonomous vs approval vs forbidden actions.
- `rules/human-approval-gates.md`: stop gates and approval record.
- `schemas/*.schema.yaml`: audit record schemas.
- `runbooks/install-and-adapt.md`: copy/adapt into another project.
- `runbooks/sop-self-improving-agent-os.md`: operating SOP.
- `runbooks/run-agent-loop.md`: execution runbook.
- `checklists/self-improving-agent-checklist.md`: preflight/runtime checklist.

## Copy Target

```text
<target-project>/agent-os/self-improving-agent-os/
```

Then copy or symlink subfolders into the target project's `.ai/` layer.

## Clone Agent

- gents/project-map-cloner.AGENT.md: maps and clones the bundle into a new project.
