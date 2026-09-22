# Reddit Sales System Source Distillation

## Source Inventory

- Type: pasted guide/transcript
- Path: C:\Users\Admin\.codex\attachments\233488c6-d61c-47f0-873b-41c598bd5e48\pasted-text.txt
- Context: guide for building a Reddit sales system with two agents: product discovery when no product exists, and selling support when a product exists
- Confidence: high for workflow design; platform behavior, rate limits, model names, hosting costs, and tool claims should be verified before live use

## One-Line Thesis

Reddit can become a safe organic sales channel when an agent reads public RSS, learns each community, drafts helpful content, queues actions, and leaves all account activity to a human.

## Mechanism

1. Pull public Reddit RSS without login.
2. Store posts and comments to build history.
3. Maintain one live profile per subreddit.
4. Use repeated problems to discover product opportunities.
5. Use product files and subreddit profiles to identify relevant threads.
6. Draft helpful replies and posts without links or product mentions by default.
7. Queue everything on dashboards for human posting.
8. Feed outcomes and DMs back into profiles manually.

## Reusable Principles

- Public reading is safer than account automation.
- Subreddit profiles are the core asset; drafts are downstream of them.
- Each subreddit has its own tone, rules, and buyer psychology.
- Repetition is the product discovery signal.
- Replies build trust; posts create traffic.
- DMs and posting remain human-led.
- Queues and sent logs prevent rushed spam and duplicate posting.

## Frameworks

Core monitor: subreddit list -> RSS pull -> normalized history -> subreddit profile -> dashboard.

Product discovery: niche constraints -> candidate communities -> monitoring window -> repeated problem analysis -> product brief -> landing page draft.

Product selling: product file -> subreddit profile -> thread matching -> reply queue -> post queue -> human posting -> sent log.

Ops loop: 30-minute pulls -> day matching -> nightly profile update -> morning drafts/dashboard -> weekly problem analysis.

## Constraints

- Reddit RSS and rate-limit behavior should be verified in the target environment.
- New or low-trust accounts may be removed by automod.
- Automating login/posting increases account risk and is outside the system.
- Subreddit rules vary and can change.
- Some niches are credentialed or high-harm and should be rejected or reviewed.
- The agent cannot read DMs unless the human supplies excerpts.

## Project Implications

Keep: no-login boundary, public RSS, one profile per subreddit, dashboard queues, human posting.

Improve: add explicit schemas, stop conditions, account-health notes, and product file boundaries.

Delete/defer: proxy automation, auto-posting, auto-DM, fake proof, and publishing checkout without approval.

New asset candidate: reddit-sales-agent-os Codex skill.

## Suggested First Test

Run one subreddit and one product for one week. Build the subreddit profile, product file, match queue, reply drafts, post drafts, sent log, and account health notes. No automated Reddit account actions.
