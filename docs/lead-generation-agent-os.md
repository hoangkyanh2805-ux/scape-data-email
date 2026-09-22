# Lead Generation Agent OS

This project turns the source guide into an approval-gated agent operating system for lead generation.

## System Shape

market intelligence -> evidence capture -> asset creation -> batch preparation -> approval gate -> response capture -> reporting

## Pipelines

| Pipeline | Use when | Main output |
|---|---|---|
| Pipeline 1: Digital product leads | You have a product, checkout, page, or offer | Buyer profile, creative plan, ad draft, daily report |
| Pipeline 2: Physical/local leads | You can detect demand from public property/business data | Candidate table, renders, property pages, outreach batch |
| Pipeline 3: Lead resale | You have captured local leads and want to sell them to businesses | Matched business list, sample PDF, delivery dashboard |

## Agents

| Agent | Responsibility |
|---|---|
| Market Intel Agent | Understand product/trade, buyer profile, buyer habitats, visible demand signals |
| Scrape And Profile Agent | Collect recent source evidence and count repeated questions, complaints, and desires |
| Creative Planner Agent | Convert source language into angles, hooks, media plans, and ad drafts |
| Candidate Scanner Agent | Find local candidates from one public source and one qualifier |
| Render Agent | Create review-ready visual fixes without inventing property details |
| Outreach Prep Agent | Prepare email, SMS, postcard, page, and PDF batches |
| Lead Capture Agent | Log visits, scans, replies, form fills, lead status, and timestamps |
| Business Sales Agent | Match leads to businesses and prepare owner outreach samples |
| Reporting Agent | Produce daily spend, lead, sale, cost, and review reports |

## Files

- Skill entrypoint: .codex/skills/lead-generation-agent-os/SKILL.md
- Pipeline references: .codex/skills/lead-generation-agent-os/references/
- Source distillation: knowledge/distilled/playbooks/automated-lead-generation-source-distillation.md

## Operating Rule

The agent may prepare drafts, tables, profiles, reports, and review batches autonomously. It must stop before sending outreach, spending money, publishing pages, launching ads, sharing lead details, or marking leads sold.

## MVP Build Map

1. Create a spreadsheet/database from the output schemas.
2. Run one small Pipeline 2 batch for a single trade and city.
3. Manually review every candidate and render.
4. Approve one outreach channel only.
5. Capture responses and inspect quality.
6. If leads are real, run Pipeline 3 with three-lead sample PDFs.
7. Add automation only after the manual batch proves the signal.

## Acceptance Criteria

- Every lead has source evidence, status, timestamp, and review state.
- Every paid or external action has an approval record.
- Every creative/render is traceable to a source profile or public candidate.
- Every uncertain candidate is marked review, not treated as approved.
- Daily report shows spend, leads, sales, cost per lead/sale, winners, and blocked items.

## Runtime Layer

The system can be handed to Grok Bot, Hermes, or another persistent agent runtime, but the runtime does not change the rules. The skill package remains the source of truth.

Read .codex/skills/lead-generation-agent-os/references/runtime-grok-hermes.md before deployment or runtime handoff.

Runtime must start with a draft-only run, inventory tools and missing inputs, and stop before spend, outreach, publishing, or lead transfer.

## Additional Source

- Grok + Hermes X post distillation: knowledge/distilled/playbooks/grok-hermes-leadgen-x-post-distillation.md
