# Self-Improving Agent OS Review - scape-data Agents

Date: 2026-09-21
Repo: `scape-data`
Knowledge source: `AGENT-SELF-IMPROVING-GUIDE.md`
Project mission: collect reviewable public social email/contact data only.

## Verdict

The repo has the right building blocks for a self-improving agent OS, but the pieces are currently split into two layers:

1. OS layer: generic self-improving agents exist for orchestration, identity, RAG, scraping, error-fix, and memory.
2. Domain layer: 8 Forex social email agents exist for the actual data collection pipeline.

The next improvement is not adding more agents. The next improvement is wiring the 8 domain agents into the OS loop:

```text
soul contract -> bounded retrieval -> run domain pipeline -> quality gate -> error/config fix -> memory snapshot
```

Live scraping is still approval-gated. This review is about agent design readiness, not permission to run paid Apify jobs.

## Review Criteria From The Guide

The guide defines five self-improving pillars:

| Pillar | Practical criterion for this repo |
|---|---|
| `soul.md` identity | Every agent has concise identity, hard rules, stop rules, and accountability checks. |
| RAG retrieval | Agents retrieve only relevant docs/run artifacts/source evidence, with pointers. |
| Quality-gated loop | Agents stop after measurable non-improvement, not just after a fixed max loop. |
| Error detection + prompt/config fix | Failures produce versioned fix proposals, validation, and comparison before apply. |
| Memory compression | Long runs produce summaries with pointers to exact source, run, actor, and approval records. |

## Current Agent Inventory

### Self-Improving OS Agents

```text
.ai/agents/runtime-orchestrator/AGENT.md
.ai/agents/soul-contract/AGENT.md
.ai/agents/rag-context/AGENT.md
.ai/agents/scrape-profile/AGENT.md
.ai/agents/error-fix/AGENT.md
.ai/agents/memory-audit/AGENT.md
.ai/agents/project-map-cloner/AGENT.md
```

### Domain Data Agents

```text
.ai/agents/forex-social-intent/source-finder.AGENT.md
.ai/agents/forex-social-intent/post-collector.AGENT.md
.ai/agents/forex-social-intent/engagement-collector.AGENT.md
.ai/agents/forex-social-intent/buyer-intent-scorer.AGENT.md
.ai/agents/forex-social-intent/seller-spam-filter.AGENT.md
.ai/agents/forex-social-intent/profile-enricher.AGENT.md
.ai/agents/forex-social-intent/lead-normalizer.AGENT.md
.ai/agents/forex-social-intent/approval-gate-reporter.AGENT.md
```

## OS Layer Review

| Agent | Status | Review |
|---|---:|---|
| `runtime-orchestrator` | Strong | Has run record, routing, checks, stop gates, 2 non-improving iterations, memory pointer requirement. It is the correct root agent. |
| `soul-contract` | Good | Matches the guide's soul.md philosophy, but should enforce a 3-question accountability loop on every domain agent. |
| `rag-context` | Strong | Correctly forbids full-history loading and compressed-memory-as-evidence. Uses top_k 20 as default. |
| `scrape-profile` | Good | Has scrape/evaluate/error/propose loop. Needs to map directly to the 8 Forex agents instead of sounding generic. |
| `error-fix` | Strong | Matches detect -> classify -> root cause -> propose -> version -> validate -> compare. Production apply is approval-gated. |
| `memory-audit` | Strong | Matches compression-with-pointers. Good guardrail against treating summaries as exact evidence. |
| `project-map-cloner` | Not core | Useful for cloning bundles to other projects, but not part of the current email-data mission. Keep it dormant. |

## Domain Layer Review

The 8 Forex agents are well-scoped for data collection and have runtime fields: Goal, Scope, Inputs, Tools, Permissions, Loop, Checks, Stop Conditions, Human Approval Gates, Outputs, Acceptance Criteria.

Their previous gap was that they were workflow agents without explicit self-improvement hooks. That gap has now been patched: each domain agent has `Self-Improvement Hooks` for context retrieval, quality metric, non-improvement rule, error signals, and memory output.

### Required Self-Improving Add-On For Every Domain Agent

Each domain agent should be evaluated with this add-on:

```md
## Self-Improvement Hooks

Context retrieval:
- Read only relevant runbook, contract, prior run artifact, and source evidence pointers.
- Do not load unrelated Hermes profile memory or old project context.

Quality metric:
- Define one measurable output quality metric for this agent.

Non-improvement rule:
- If two attempts do not improve the metric, stop and hand off to `error-fix` or `approval-gate-reporter`.

Error signals:
- Missing required field.
- Actor/tool failure.
- Source evidence missing.
- Cost/quota/rate warning.
- Public-only/contact-data rule violated.

Memory output:
- Emit concise run notes with pointers to artifact rows, actor run ids, source URLs, and approval ids.
```

## Domain Agent Quality Metrics

| Agent | Quality metric | Stop if not improving |
|---|---|---|
| `source-finder` | number of public sources with buyer-engagement evidence and no login requirement | 2 iterations produce no better sources or sources are seller-only |
| `post-collector` | public post rows with source URL, post URL, actor/run metadata, and engagement potential | actor schema/cost/source quality does not improve after 2 config attempts |
| `engagement-collector` | comment/reply rows with user pointer, text, post URL, and dedupe rate | more volume lowers usable text/evidence quality or hits cost/quota warning |
| `buyer-intent-scorer` | high/medium scores with explicit evidence phrase and low false-positive seller bleed | scoring changes do not improve evidence quality or increase weak high-intent rows |
| `seller-spam-filter` | seller/spam rows flagged with evidence while preserving borderline review rows | filter changes hide evidence or over-reject likely buyers |
| `profile-enricher` | retained candidates with public profile fields and explicit email source URL/field | enrichment adds unsourced/generated emails or cost rises without email yield |
| `lead-normalizer` | reproducible candidate table with required fields, duplicate report, source pointers | dedupe/normalization loses source evidence or creates conflicting statuses |
| `approval-gate-reporter` | report completeness: cost, yield, confidence split, duplicate rate, risks, next gate | any approval gate is reached or report cannot verify artifacts |

## Recommended Runtime Wiring

Use this as the Hermes multi-agent control flow:

```text
runtime-orchestrator
  -> soul-contract checks the repo identity and agent contracts
  -> rag-context builds a bounded context packet
  -> source-finder
  -> post-collector
  -> engagement-collector
  -> buyer-intent-scorer
  -> seller-spam-filter
  -> profile-enricher
  -> lead-normalizer
  -> approval-gate-reporter
  -> error-fix only when an error/config issue occurs
  -> memory-audit writes the run snapshot
```

Do not run `project-map-cloner` for this repo's normal email-data work.

## Evidence And Memory Rules

Every run should produce these pointer types:

```text
run_id
actor_id
actor_run_id
dataset_id
source_url
source_post_url
profile_url
email_source_url
email_source_field
approval_id
artifact_path
memory_snapshot_id
```

Compressed memory can summarize decisions and patterns, but exact claims must point back to local artifacts or source URLs.

## Approval Boundaries

The self-improving loop may improve prompts, actor configs, scoring rubrics, and normalization rules only in draft form.

Human approval is required before:

```text
paid/high-volume Apify run
bigger batch size
new actor class
login/session/private source
email validation at scale
external export of full emails
CRM/Sheets/Airtable/Drive/Telegram sync
outreach or lead resale
production prompt/config apply
```

## Findings

### Finding 1 - Domain agents need explicit self-improvement hooks

Severity: medium.

The 8 Forex agents have strong operational contracts, but they do not explicitly say how they retrieve relevant context, how they judge improvement, or what memory notes they emit. The OS agents cover this generally, but Hermes will be more reliable if every domain agent exposes its own metric and error signals.

Fix: add or enforce the `Self-Improvement Hooks` block above.

### Finding 2 - `scrape-profile` is too generic for the new repo mission

Severity: medium.

The repo mission is now email-data collection from social engagement. The generic `scrape-profile` agent should either be treated as the implementation adapter behind `post-collector`, `engagement-collector`, and `profile-enricher`, or renamed/mapped clearly in docs.

Fix: in Hermes routing, do not let `scrape-profile` bypass the 8 Forex social intent agents.

### Finding 3 - `project-map-cloner` should be dormant

Severity: low.

It is useful for copying this OS into future projects, but it can confuse the active repo mission. It should not be loaded in normal data-collection runs.

Fix: mark it as optional/non-runtime in the orchestrator context.

### Finding 4 - Knowledge guide is source material, not runtime truth

Severity: low.

`AGENT-SELF-IMPROVING-GUIDE.md` is the design guide. Runtime truth for this repo should remain `README.md`, `AGENTS.md`, `.ai/rules/`, the 8 domain contracts, and the runbook.

Fix: use the guide only for design criteria, not as permission to run broad self-improvement or old profile workflows.

## Acceptance Criteria For A Self-Improving Hermes Run

A Hermes run is self-improving-agent-OS compliant when:

- repo identity is `scape-data` and profile is `scapedata`;
- only bounded context is loaded;
- every domain agent output has evidence pointers;
- every loop has a measurable metric;
- two non-improving attempts stop the loop;
- errors become versioned fix proposals;
- memory snapshot contains exact artifact/source/approval pointers;
- no approval-gated action occurs autonomously;
- final report says what improved, what did not, and why the run stopped.

## Patch Status

Implemented:

```text
.ai/agents/forex-social-intent/*.AGENT.md
```

Each of the 8 domain agents now includes `Self-Improvement Hooks` with context retrieval, quality metric, non-improvement rule, error signals, and memory output.

Remaining routing rule: Hermes should read the 8 domain agents as the active email-data pipeline and the OS agents as support services.

