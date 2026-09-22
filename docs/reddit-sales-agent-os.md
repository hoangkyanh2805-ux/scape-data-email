# Reddit Sales Agent OS

This project turns the Reddit sales guide into a safe agent operating system for product discovery, audience research, and organic Reddit sales.

## Core Principle

The agent reads public Reddit RSS feeds, builds community understanding, drafts useful content, and queues actions. A human uses their own Reddit session to post, comment, and handle DMs.

## System Shape

public RSS -> feed history -> subreddit profiles -> product discovery or selling queue -> dashboard -> human posting -> sent log -> profile updates

## Modes

| Mode | Use when | Main output |
|---|---|---|
| Core Monitoring | You need durable Reddit listening | Feed history, subreddit profiles, rate-limit reports |
| Product Discovery | You do not have a product yet | Repeated problem analysis, guide/product brief, landing page draft |
| Product Selling | You have a product | Product file, thread matches, reply drafts, post drafts |
| Ops | You want daily operation | Dashboards, morning summaries, reminders, sent log |

## Agents

| Agent | Responsibility |
|---|---|
| Reddit Feed Monitor Agent | Pull public RSS safely and store normalized history |
| Subreddit Profiler Agent | Maintain evidence-backed subreddit profiles |
| Product Discovery Agent | Find repeated urgent problems and draft product briefs |
| Product File Agent | Keep product promise, boundaries, objections, and proof quotes |
| Thread Match Agent | Find fresh threads where helpful replies fit |
| Reply And Post Draft Agent | Draft non-promotional, subreddit-native content |
| Dashboard Ops Agent | Update queues, reminders, sent log, and account health notes |

## Files

- Skill entrypoint: .codex/skills/reddit-sales-agent-os/SKILL.md
- References: .codex/skills/reddit-sales-agent-os/references/
- Source distillation: knowledge/distilled/playbooks/reddit-sales-system-source-distillation.md

## MVP Build Map

1. Start with one product and one subreddit, or one niche and one subreddit.
2. Pull public RSS on a conservative cadence.
3. Create one subreddit profile and update it nightly.
4. If selling, create the product file before drafting replies.
5. Queue replies only for directness score 4 or 5.
6. Draft five posts per morning at most, but human chooses what to post.
7. Track removals, sent items, and response quality.

## Acceptance Criteria

- Agent never logs into Reddit or posts.
- Every draft references the correct subreddit profile.
- Every queued action has a direct link, copy-ready text, urgency, and risk note.
- Every subreddit profile separates quotes from inference.
- Rate limits and 429s are logged.
- Sent log prevents duplicate replies.
