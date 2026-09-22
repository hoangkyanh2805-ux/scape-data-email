---
name: lead-generation-agent-os
description: Turn a product, trade, or local market into an approval-gated lead generation agent system with buyer profiling, candidate detection, creative/render prep, outreach batches, lead capture, lead resale, and reporting. Use when building or operating lead generation workflows; never use to send outreach, spend budget, publish campaigns, or transfer leads without explicit approval.
---

# Lead Generation Agent OS

Use this skill when the user wants to design, prepare, or operate a lead generation pipeline. The skill must be self-contained: an agent that has not read the original guide should be able to run from this file plus the referenced files.

## Core Operating Model

find existing demand -> gather source evidence -> create a buyer/property-specific asset -> prepare the next action -> stop for approval before external contact or spend -> capture response -> report results

The agent prepares work. Humans approve risky actions. No live sending, ad spend, page publishing, paid API scale-up, or lead transfer happens without explicit approval.

## Pipeline Selection

| User situation | Pipeline | Read first |
|---|---|---|
| User has a digital product, checkout, course, paid community, SaaS, template, or offer | Pipeline 1: Digital Product Leads | references/pipeline-1-digital-product.md |
| User owns a local business and wants leads for themselves | Pipeline 2: Physical / Local Leads | references/pipeline-2-physical-local.md |
| User has no product/business and wants to generate leads then sell them | Pipeline 2 then Pipeline 3 | references/pipeline-2-physical-local.md, then references/pipeline-3-lead-resale.md |
| User already has captured local leads and wants buyers | Pipeline 3: Lead Resale | references/pipeline-3-lead-resale.md |

## Required Inputs

| Pipeline | Minimum inputs |
|---|---|
| Digital product leads | Product/page/offer, price, checkout/page URL, target market if known, ad budget ceiling |
| Physical/local leads | Trade, city/area, target buyer type if known, batch size, API/spend ceiling |
| Lead resale | Trade, city/area, existing lead table, exclusivity/pricing assumptions |

If a required input is missing, ask only for that input. If the next step would be external or paid, stop and request approval using references/stop-conditions.md.

## Mandatory Read Order

1. This SKILL.md.
2. The selected pipeline reference.
3. references/output-schemas.md before creating tables or dashboards.
4. references/agent-contracts.md before assigning work to sub-agents or documenting roles.
5. references/tool-access-checklist.md before claiming a tool can run.
6. references/runtime-grok-hermes.md when deploying or handing the workflow to Grok Bot, Hermes, or another persistent runtime.
7. references/permission-matrix.md before any action involving money, outreach, publishing, private data, or lead transfer.
8. references/stop-conditions.md whenever data quality, budget, permissions, or tool state is uncertain.
9. references/run-output-template.md before returning the final operator handoff.

## Operating Rules

- Use one table per trade, city, product, or niche. Never mix unrelated niches when judging quality or status.
- Mark uncertain evidence as review. Do not guess, pad, or silently include weak rows.
- Use one qualifier for physical lead detection until real response data justifies adding another.
- Keep source URLs, dates, engagement, imagery dates, batch cost, contact validation status, and confidence fields.
- Prepare outreach, ad campaigns, landing pages, PDFs, and postcards as drafts unless the user explicitly approves publication, sending, or spend.
- Stop before contacting a real person, spending money, publishing externally, using paid APIs at scale, sharing lead details, or marking a lead sold/exclusive.
- Never invent income claims, testimonials, contact data, property state, business coverage areas, or consent status.
- Treat stale imagery, borderline qualifiers, rejected creative, unsupported claims, and data conflicts as review items.
- Separate source facts from agent inference in every report.

## Execution Protocol

1. Select pipeline and state why.
2. Inventory available inputs, credentials, tools, tables, and missing fields.
3. Create a run plan with safe autonomous steps and approval-gated steps.
4. Execute only safe draft/prep steps.
5. Write outputs into the schemas from references/output-schemas.md.
6. Run checks from the selected pipeline reference.
7. Stop at the first approval gate or after producing the requested draft package.
8. Return the run output template with artifacts, evidence, review rows, costs, and next approval needed.

## Expected Outputs

Every run should return: selected pipeline, inputs used, missing inputs, tools available/unavailable, artifacts created, evidence-backed findings, review items, cost/quota notes, approval gates reached, and next safe action.

## Tooling Boundary

Potential tools include web search, platform scrapers, Apify, Google Places, property/business records, imagery APIs, image/video generation, page builders, spreadsheets/databases, email/SMS/postcard senders, ads dashboards, Whop, analytics, and payment/dashboard tools. Use only tools the user has provided, connected, or approved.

When a required integration is unavailable, produce the draft artifact and list the exact tool/API access needed to run that step.

