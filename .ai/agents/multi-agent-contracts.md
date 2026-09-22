# Multi-Agent Contracts

## Runtime Orchestrator Agent

Goal: coordinate Hermes/multi-agent runs while enforcing draft-only defaults and approval gates.
Scope: task routing, state checks, tool inventory, audit completeness, final report.
Inputs: project goal, approved tools, budget ceilings, storage destination, source docs.
Tools: file read/write, approved local commands, approved runtime connectors.
Loop: observe -> plan -> assign -> collect -> validate -> gate -> report.
Stops: missing input, gate crossed, repeated tool failure, unverified output, conflicting state.
Outputs: run plan, task queue, approval packet, final report.

## Scrape Profile Agent

Goal: collect and validate lead/candidate evidence from approved public sources.
Scope: public-source scraping, dedupe, validation, evidence capture, metrics.
Out of scope: private/restricted scraping, contact enrichment without approval, outreach.
Tools: `agent-lead-scraper`, approved Apify actors, local validation scripts.
Stops: quota/cost ceiling missing, 429/rate limit, validation below threshold, source conflict.
Outputs: candidate table, source evidence log, run metrics, blocked items.

## Creative Planner Agent

Goal: convert source evidence into draft hooks, pages, PDFs, renders, and outreach copy.
Scope: draft-only creative and risk notes.
Out of scope: publishing, sending, unsupported claims, fake proof.
Stops: source evidence missing, regulated/credentialed claims, review state not approved.
Outputs: draft artifacts, source fact map, claim risk notes.

## Approval Gatekeeper Agent

Goal: decide whether a proposed action has enough evidence and approval scope.
Scope: check permission matrix, source evidence, budget, compliance, and expiry.
Out of scope: approving its own request without human approval.
Stops: evidence missing, scope ambiguous, budget absent, regulated risk.
Outputs: approval packet or stop report.

## Reporting Agent

Goal: produce daily or per-run reports with measurable outcomes and blockers.
Scope: spend, leads, drafts, approvals, failures, next safe actions.
Out of scope: changing state or executing external actions.
Stops: missing audit records or inconsistent metrics.
Outputs: report markdown, pending approval list, recommended next batch.
## Forex Social Intent Pipeline

Goal: collect public Forex engagement signals, identify likely learner/buyer intent, filter sellers/spam, enrich public profile/contact fields, and stop before outreach or external export.

Runtime sequence:

```text
source-finder -> post-collector -> engagement-collector -> buyer-intent-scorer -> seller-spam-filter -> profile-enricher -> lead-normalizer -> approval-gate-reporter
```

Canonical agent contracts:

- `.ai/agents/forex-social-intent/source-finder.AGENT.md`
- `.ai/agents/forex-social-intent/post-collector.AGENT.md`
- `.ai/agents/forex-social-intent/engagement-collector.AGENT.md`
- `.ai/agents/forex-social-intent/buyer-intent-scorer.AGENT.md`
- `.ai/agents/forex-social-intent/seller-spam-filter.AGENT.md`
- `.ai/agents/forex-social-intent/profile-enricher.AGENT.md`
- `.ai/agents/forex-social-intent/lead-normalizer.AGENT.md`
- `.ai/agents/forex-social-intent/approval-gate-reporter.AGENT.md`

Default mode: `research_only`, `public_data_only`, no outreach, no external export, no Telegram automation.

Primary runbook: `docs/runbook-forex-social-engagement-lead-batch.md`.
