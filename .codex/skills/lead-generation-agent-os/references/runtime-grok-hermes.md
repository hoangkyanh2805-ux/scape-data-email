# Runtime: Grok Bot + Hermes

Use this reference when the user wants to run the Lead Generation Agent OS on Grok Bot, Hermes, or another persistent agent runtime.

## Core Principle

The runtime is replaceable. The skill file is the operating system. Grok Bot or Hermes should read the same skill package, use the same tools, write to the same tables, and stop at the same approval gates.

## Runtime Options

| Runtime | Best fit | Operator pattern |
|---|---|---|
| Grok Bot | Lower setup, chat-driven operation, agent with browser/terminal/filesystem | Give it the skill package, credentials, tool access, and approval rules |
| Hermes | Scheduled persistent operation, Telegram-style operator loop, hosted service/VPS/Railway | Deploy once, persist storage, schedule runs, send summaries and approval requests |
| Codex/local agent | Building and maintaining the skill, docs, schemas, and tests | Prepare artifacts and run safe draft workflows |

## Required Runtime Capabilities

- Read this skill package and selected references.
- Persist files/tables between runs.
- Run scheduled jobs or receive scheduled prompts.
- Access approved tools only.
- Send operator summaries and approval requests.
- Log every run, cost, tool failure, approval, and stop reason.
- Resume from existing tables without rereading unrelated niches.

## Tool Access Bundle

Before running live, collect these as applicable:

- Product/page/checkout/Whop access for Pipeline 1.
- Source/community/scraper access for buyer-language collection.
- Image or video generation access for creative or render drafts.
- Google Places/property/business/permit/imagery access for Pipeline 2 and 3.
- Spreadsheet/database/dashboard access.
- Page builder access for draft property pages or lead dashboards.
- Email/SMS/postcard provider access, draft-only until approved.
- Ads dashboard access, draft/reporting-only until budget approval.
- Notification channel such as Telegram for summaries and approval gates.

## Scheduling Model

Default cadence:

- Daily: pull source data, update dashboards, report spend/leads/sales/review items.
- Pipeline 1 daily: compare spend, clicks, sales, cost per sale, revenue, and winning angle.
- Pipeline 2 daily: prepare candidate and outreach batches, but stop before sending.
- Pipeline 3 weekly or per batch: match leads to businesses and prepare sales samples.

The runtime may recommend pauses, sends, page publishing, or budget changes, but it must stop for approval before executing them.

## Funding And Spend Boundary

Claims that ads can be funded by sales are treated as an operating hypothesis, not permission. The agent must show spend, revenue, pending balance, and cash risk before recommending budget changes.

No runtime may:

- Launch or increase ad spend without explicit budget approval.
- Use paid APIs at scale without a ceiling.
- Send email/SMS/postcards without approved batch samples.
- Publish property pages or dashboards externally without approval.
- Transfer or sell lead details without approval.

## Runtime Handoff Checklist

Before handing the system to Grok Bot or Hermes, provide:

- Skill path or full skill package.
- Selected pipeline and target niche/trade/city/product.
- Approved tools and missing tools.
- Budget ceilings for ads, paid APIs, generation, and postcards.
- Table/dashboard destinations.
- Notification channel.
- Human approval rules copied from permission-matrix.md.
- Stop conditions copied from stop-conditions.md.
- First safe task: draft-only run with no external sends or spend.

## First Safe Runtime Prompt

Run the Lead Generation Agent OS in draft-only mode. Read SKILL.md, the selected pipeline reference, output-schemas.md, tool-access-checklist.md, permission-matrix.md, stop-conditions.md, runtime-grok-hermes.md, and run-output-template.md. Inventory missing inputs and tools, create the first draft tables/artifacts, and stop before any spend, publishing, outreach, or lead transfer.
