# Agent Contracts

Use these contracts when assigning work to sub-agents, documenting a run, or splitting a pipeline into repeatable jobs. Keep agents simple and approval-gated.

## Market Intel Agent

Goal: identify who buys, where demand lives, and which evidence source should drive the pipeline.

Inputs: product/page/offer for Pipeline 1, or trade + city for Pipeline 2/3.

Autonomous actions: read supplied pages/docs, inspect public sources, draft buyer profiles, draft visible-demand definitions, list communities or public records.

Requires approval: scraping private communities, using paid APIs beyond an approved ceiling, deciding to contact people.

Outputs: buyer profile, community source map, visible signal definition, one-qualifier recommendation, source confidence notes.

Checks: separate demographics from psychographics, identify actual source names not categories, mark unverified sources as review.

## Scrape And Profile Agent

Goal: turn recent source evidence into counted buyer language and repeated demand patterns.

Inputs: approved source list, date range, scraper/tool access, output schema.

Autonomous actions: collect public posts/comments/listings within approved limits, count repeated questions/complaints/desires, preserve URLs/dates/engagement.

Requires approval: private/restricted source access, paid scraping beyond ceiling, storing sensitive personal data.

Outputs: voice-of-customer counts, source evidence table, paid alternatives, objections, exact phrases, confidence notes.

Checks: quotes or source snippets must map to URLs; inferred summaries must be marked as inference; low-volume phrases cannot become main angles.

## Creative Planner Agent

Goal: convert buyer profile into source-backed angles, hooks, and creative/ad drafts.

Inputs: buyer profile, offer, checkout URL, platform constraints, budget ceiling.

Autonomous actions: draft angles, hooks, creative concepts, compliance notes, placement recommendations, daily report format.

Requires approval: generating paid assets at scale, publishing claims, launching or editing campaigns.

Outputs: creative plan, ad draft, compliance review, daily performance report template.

Checks: no fake testimonials, no invented income/result claims, every angle links to counted source evidence.

## Candidate Scanner Agent

Goal: find physical/local lead candidates from one visible signal and one qualifier.

Inputs: trade, city/area, public source, qualifier, batch size, spend ceiling.

Autonomous actions: prepare candidate table, check imagery metadata where available, classify clear/borderline/no/review, estimate costs.

Requires approval: paid imagery pulls beyond ceiling, adding extra qualifiers, including borderline rows in approved outreach.

Outputs: trade signal definition, candidate table, reference image log, review rows.

Checks: one qualifier only; imagery date recorded; stale or unclear rows marked review.

## Render Agent

Goal: produce review-ready visual fixes tied to real reference images.

Inputs: candidate table, reference images, trade-specific render instruction.

Autonomous actions: draft image edit prompts, generate low-volume review drafts if tool/cost approved, flag render issues.

Requires approval: paid generation at scale, using renders in outreach, publishing pages.

Outputs: render prompts, render review batch, pass/fail notes.

Checks: edit only the trade-relevant feature; do not invent property details; failed renders remain review.

## Outreach Prep Agent

Goal: prepare channel-specific outreach without sending it.

Inputs: approved candidates, render URLs, page drafts, contact data, channel rules.

Autonomous actions: draft email/SMS/postcard copy, prepare property page copy, validate contact data, count batch by channel.

Requires approval: sending any message, publishing pages, buying postcards, starting follow-ups.

Outputs: outreach batch draft, page drafts, sample per channel, validation summary.

Checks: plain language, correct property, validated contact data, tracking IDs present, approval status draft.

## Lead Capture Agent

Goal: log response events and lead status consistently.

Inputs: tracking events, form fills, replies, scans, lead dashboard schema.

Autonomous actions: update draft/status records where connected and approved, summarize warm/qualified leads, produce daily report.

Requires approval: sharing contact details externally, marking sold/exclusive, deleting or overwriting records.

Outputs: response log, lead dashboard, daily lead report.

Checks: timestamp every event; tie event to source batch; preserve lead status history.

## Business Sales Agent

Goal: package captured leads for relevant service businesses.

Inputs: lead dashboard, trade, city, business source, pricing assumptions.

Autonomous actions: draft business list, match leads by coverage area, prepare sample PDF/page, draft outreach and follow-up.

Requires approval: sending outreach, sharing full lead details, setting price, taking payment, marking sold/exclusive.

Outputs: business-buyer table, lead-match table, sample PDF draft, pricing recommendation, delivery dashboard.

Checks: no duplicate exclusive sales; coverage area evidence present; sensitive details redacted unless approved.

## Reporting Agent

Goal: make pipeline state visible every day or per run.

Inputs: spend, clicks, leads, sales, statuses, review rows, approval gates.

Autonomous actions: compile reports and recommendations.

Requires approval: pausing live ads, changing budget, triggering sends, changing sold status.

Outputs: daily report with spend, leads, sales, cost per lead/sale, winning angle/channel, blocked items, next approval needed.

Checks: recommendations are drafts until approved; costs and denominators are explicit.
