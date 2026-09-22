# Command - Clone Self-Improving Agent OS

Use when cloning this project's self-improving agent OS to a new repo.

## Inputs

- Target project path.
- Copy mode: `bundle-only` or `active-runtime`.
- Target domain/workflow.

## Steps

1. Read `.ai/agents/project-map-cloner/AGENT.md`.
2. Inspect target project before writing.
3. Use source bundle `bundles/self-improving-agent-os/`.
4. Copy bundle to target `agent-os/self-improving-agent-os/` unless user specifies another path.
5. If active runtime is requested, adapt `.ai/agents`, `.ai/rules`, `.ai/schemas`, and `.ai/runbooks`.
6. Write target install report and project map.
7. Verify no unexpected overwrite happened.
8. Stop before enabling external-impact actions.