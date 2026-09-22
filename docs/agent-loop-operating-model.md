# Agent Loop Operating Model

This repo should run as a draft-first, evidence-backed, approval-gated multi-agent system. Hermes, Codex, Grok, or another runtime may execute the loops, but the runtime never changes the operating rules.

## Current State Summary

- `agent-lead-scraper/` contains the working self-improving scraper loop: Apify execution, error detection, prompt/config fixes, evaluation, RAG retrieval, memory compression, and loop termination.
- `docs/lead-generation-agent-os.md` and `docs/reddit-sales-agent-os.md` define safe business workflows, but runtime handoff rules are not centralized.
- Knowledge assets already exist under `knowledge/distilled/playbooks/` and should be treated as references, not executable permission.
- The repo needs explicit contracts for Hermes/multi-agent operation: tool inventory, state records, permission matrix, stop conditions, and audit evidence.

## Candidate Agent Loops

1. Runtime Orchestrator Agent: read source of truth, start draft-only run, assign work, enforce gates, collect final report.
2. Market Intel Agent: profile buyer/trade/subreddit, capture demand evidence, define qualifiers.
3. Scrape/Profile Agent: run approved public-source scraping within quota, dedupe, validate, attach evidence.
4. Candidate Scanner Agent: produce local/business candidate rows with source URLs and review state.
5. Creative Planner Agent: produce hooks, angles, pages, PDFs, renders, and outreach copy as drafts only.
6. Approval Gatekeeper Agent: review risk, budget, evidence, compliance, and create approval records.
7. Lead Capture Agent: log visits, replies, form fills, lead status, and timestamps.
8. Business Sales Agent: prepare buyer matches and sample packs, but stop before transfer/sale.
9. Reporting Agent: summarize spend, output, blockers, approvals pending, and next safe actions.

## Standard Loop

```text
observe -> retrieve context -> plan -> draft/prepare -> validate -> log evidence -> request approval or continue -> report
```

## Runtime Rule

Every external-impact action must be represented as a draft, queue item, or approval request first. No agent may silently turn preparation into execution.

## Test And Acceptance Criteria

- Every run has a run id, source evidence, output artifacts, and a status.
- Every external-impact action has an approval id before execution.
- Draft rows and approved rows are visibly separate.
- Agents stop after 3 repeated tool failures, 2 non-improving self-improvement iterations, missing required input, or any money/account/publishing/lead-transfer boundary.

## Source Playbooks

- docs/precisox-self-improving-agent-application.md: applies the @precisox self-improving agent video pattern to this repo.
- knowledge/distilled/playbooks/precisox-self-improving-agent-playbook.md: reusable distilled playbook.

- knowledge/distilled/guides/precisox-full-guide-self-improving-agents.md: full implementation guide from the reconstructed script.
- knowledge/reusable-assets/checklists/hermes-self-improving-agent-checklist.md: runtime checklist for Hermes self-improvement.
## Operational Artifacts

- `docs/sop-self-improving-agent-os.md`: SOP for the six-agent self-improving system.
- `docs/runbook-hermes-self-improving-agent-run.md`: runbook for Hermes/Codex runtime execution.
- `.ai/agents/*/AGENT.md`: six concrete agent contracts.
- `.ai/schemas/*.schema.yaml`: audit record schemas.
- `bundles/self-improving-agent-os/`: portable bundle for other projects.