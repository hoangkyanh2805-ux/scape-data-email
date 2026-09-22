# Self-Improving Agent OS Bundle

## Purpose
A portable operating-system layer for projects that need self-improving agents without unsafe autonomy.

The bundle implements this pattern:

```text
identity contract -> bounded retrieval -> quality-gated loop -> versioned self-fix -> compressed memory with source pointers -> approval gate
```

## Default Agent Set

- runtime-orchestrator
- soul-contract
- rag-context
- scrape-profile
- error-fix
- memory-audit

## Install

1. Copy this folder into the target repo, usually `agent-os/self-improving-agent-os/`.
2. Copy `agents/` into the target repo's `.ai/agents/` or adapt them to your runtime.
3. Copy `rules/` into `.ai/rules/`.
4. Copy `schemas/` into `.ai/schemas/`.
5. Read `runbooks/install-and-adapt.md`.
6. Run the first batch in `draft_only: true` mode.

## Non-Negotiable Rules

- No autonomous spend.
- No autonomous outreach.
- No autonomous publishing.
- No autonomous account login/posting.
- No autonomous lead transfer/sale.
- No silent production prompt/config mutation.

All external-impact actions become approval requests first.

## Project Map Cloner

Use gents/project-map-cloner.AGENT.md when installing this bundle into another project. It inspects the target, chooses bundle-only or active-runtime mode, writes an install report, and stops before overwriting files or enabling external-impact actions.
