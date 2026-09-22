---
name: reddit-sales-agent-os
description: Build or operate an approval-gated Reddit sales copilot that monitors public Reddit RSS feeds, maintains subreddit profiles, discovers repeated problems, drafts helpful posts and replies, queues them on dashboards, and leaves all Reddit posting and DMs to a human. Use for Reddit-based product discovery, audience research, and organic sales systems; never use to log into Reddit, automate posting, spam, or bypass subreddit rules.
---

# Reddit Sales Agent OS

Use this skill when the user wants to turn Reddit communities into a product discovery, audience research, or organic sales workflow. The system reads public Reddit RSS feeds, stores history, profiles communities, drafts helpful content, and queues actions for a human operator.

Core rule: read public data -> understand the subreddit -> draft useful non-spam content -> queue with direct links -> human reviews and posts from their own browser.

## Non-Negotiable Boundary

The agent never logs into Reddit, posts to Reddit, sends DMs, votes, uses proxies to mimic users, or bypasses subreddit rules. It only reads public feeds, drafts, queues, logs, and reminds. Human operators click, paste, post, reply, and handle DMs.

## Modes

| User situation | Mode | Read first |
|---|---|---|
| User has no product yet | Product Discovery Mode | references/product-discovery-mode.md |
| User already has a product | Selling Mode | references/product-selling-mode.md |
| User wants the shared infrastructure | Core Monitoring Mode | references/core-reddit-monitoring.md |
| User wants dashboards or schedules | Ops Mode | references/dashboard-and-schedule.md |

## Required Inputs

| Mode | Minimum inputs |
|---|---|
| Core Monitoring | Subreddit list or product/audience description, storage destination, schedule preference |
| Product Discovery | Niche constraints, risk boundaries, initial subreddit candidates or permission to research them |
| Selling | Product description, price, who it is for, who it is not for, target subreddits or audience description |
| Ops | Dashboard destination, notification channel, account names handled by humans, posting windows if known |

If required inputs are missing, ask only for those inputs. If the next action would post, message, publish, spend money, or contact a person, stop and request approval or human action.

## Mandatory Read Order

1. This SKILL.md.
2. references/core-reddit-monitoring.md for RSS behavior and subreddit profiles.
3. The selected mode reference: product-discovery-mode.md or product-selling-mode.md.
4. references/output-schemas.md before creating tables, files, dashboards, or queues.
5. references/agent-contracts.md before splitting work into agents.
6. references/permission-matrix.md before any live, external, account, or publishing action.
7. references/stop-conditions.md when tool, data, account, rate-limit, or rule risk is unclear.
8. references/dashboard-and-schedule.md for recurring operation.
9. references/run-output-template.md before returning the handoff.

## Operating Rules

- Use Reddit public RSS feeds where available; add .rss to public subreddit, post, or comment URLs.
- Pace RSS pulls conservatively. Treat one request per minute per IP as the default ceiling unless a verified source says otherwise.
- On 429 or rate-limit signals, wait and reduce frequency; do not retry aggressively.
- Store history instead of only reading live posts.
- Keep one markdown profile per subreddit and update it daily from evidence.
- Separate subreddit voice, rules, and audience profile by community. Never write for one subreddit using another subreddit profile.
- Draft replies that stand alone as useful help. Do not mention or link the product unless the user explicitly asks and subreddit rules allow it.
- Queue everything with direct links and copy-ready text. Human reviews and posts manually.
- Log skipped opportunities and why.
- Do not create fake social proof, fake numbers, fake testimonials, or manipulative scarcity.
- Mark risky niches, credentials-required niches, medical/legal/financial harm risk, and moderation uncertainty as review.

## Execution Protocol

1. Select mode and state why.
2. Inventory inputs, subreddit targets, storage, notification channel, and unavailable tools.
3. Create a safe run plan with draft-only actions and approval-gated actions.
4. Pull or prepare RSS sources within the rate limit.
5. Update subreddit profiles, product files, queues, and dashboards using output schemas.
6. Run checks from the selected mode reference.
7. Stop before any Reddit account action or external publication.
8. Return the run output template with artifacts, review items, queued actions, and next human step.

## Expected Outputs

Every run should return selected mode, inputs used, missing inputs, subreddit list, tool access status, artifacts created, queued replies/posts, profile changes, skipped items, risks, approval gates, and next human action.
