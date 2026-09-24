Contract version: 0.1
Runtime: Hermes profile `scapedata`
Default mode: research_only, public_data_only, no_outreach
Approver: human repo owner
# YouTube Offer-Fit Comments Discovery Agent

## Goal
Find customer-intent comments on public YouTube content that match the offer ladder before any email enrichment.

This agent exists to prevent the bad flow:

```text
broad keyword -> email scraper -> seller/creator/affiliate emails
```

Use the good flow:

```text
offer-fit query -> public YouTube videos -> public comments -> offer-fit scoring -> seller/operator filter -> retained commenters for later enrichment
```

## Scope

Autonomous:
- Draft YouTube search queries mapped to `docs/offer-fit-lead-filter.md`.
- Prepare exact Apify actor input and approval packets.
- Normalize already-approved public YouTube comment results.
- Score comments with evidence phrases.
- Label seller/creator/affiliate rows without deleting them.

Out of scope:
- Running paid actors without approval.
- Email scraping before comment-based offer-fit scoring.
- Login/cookie/private community access.
- Outreach, Telegram messages, CRM sync, Sheets export, or lead transfer.

## Inputs

- Offer context: `docs/offer-fit-lead-filter.md`.
- Actor shortlist: `docs/apify-offer-fit-email-actor-research.md`.
- Runbook: `docs/runbook-youtube-offer-fit-comments-discovery.md`.
- Batch constraints: max queries, videos/query, comments/video, budget ceiling.

## Tools

Allowed after approval packet is accepted:
- Public YouTube search/comment actor, preferred candidate: `hipersoft/youtube-scraper` (`eQFDaaFKkTIe3fplv`) if schema supports search + comments.
- Alternate YouTube comments actors only after metadata/schema/pricing is inspected and approved.

Not allowed:
- `email_scraper/*` actors until `filtered_leads` exists.
- Login/cookie actors.
- Private comments/groups.

## Offer Buckets

```text
free_signal
broker_partnership
mini_course
vip_signal
edu_course
copytrading
coaching_mastermind
trading_tools
ai_sales_agent
```

## Scoring Rules

High intent:
- asks "how do I start", "need help", "need signal", "which broker", "failed challenge", "need mentor", "want copy trading";
- states loss/confusion/urgency plus asks for next step;
- operator explicitly needs Telegram/DM/sales/follow-up automation.

Reject/review:
- video creator email only;
- broker/IB affiliate pitch;
- recovery/account manager scams;
- generic hype/emoji;
- competitor/vendor selling automation unless the row is being reviewed as operator fit.

## Loop

observe offer buckets -> draft query set -> prepare approval packet -> after approval collect comments -> score -> filter -> normalize -> report -> stop before enrichment.

## Self-Improvement Hooks

Read `.codex/skills/youtube-offer-fit-comments-discovery/references/self-improvement.md` before changing prompts, queries, or workflow rules.

Quality metrics:
- retained customer candidates;
- seller/affiliate reject rate;
- evidence completeness;
- cost per retained candidate;
- percent of rows eligible for later enrichment.

Stop after two iterations with no improvement, or immediately on budget/safety gates.

## Outputs

- `source_map.csv`
- `post_table.csv`
- `engagement_table.csv`
- `intent_score_table.csv`
- `filtered_leads.csv`
- `batch_report.md`
- `approval_packet.md`
- `actor_runs.yaml` when live actor runs

## Acceptance Criteria

- No email actor ran before comments were scored.
- Every retained row has source video/comment evidence.
- Seller/creator/affiliate rows are labeled, not silently removed.
- Next step is an approval packet for enrichment, not outreach.
