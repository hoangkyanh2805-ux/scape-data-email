# Command - Run Question-First Source Research

Purpose: use the info-product social demand mining framework only as research logic for `scape-data`.

Read first:

```text
README.md
AGENTS.md
docs/apify-active-actors.md
docs/runbook-forex-social-engagement-lead-batch.md
knowledge/distilled/playbooks/question-first-social-demand-mining.md
knowledge/project-maps/scape-data/question-first-social-demand-mining-map.md
```

Prompt:

```text
Plan a tiny public-only source research batch for `scape-data` using question-first demand mining.

Constraints:
- use only active Apify actor whitelist;
- no outreach;
- no external export;
- no Telegram/n8n;
- no private groups;
- no login cookies;
- preserve exact repeated phrases;
- stop at approval packet before any live/paid actor run.

Output:
1. source/query candidates;
2. repeated phrases to test;
3. expected actor role;
4. batch limits;
5. approval packet;
6. pass/fail criteria.
```
