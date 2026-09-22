# Architecture Note

This file replaces an older generic architecture writeup that described the prototype as production-ready. The current `agent-lead-scraper` architecture is draft-first and scoped to `scape-data`.

## Current Shape

```text
validate scope -> run mock or approved public actor -> collect metrics -> detect errors -> propose config fix -> evaluate quality -> optionally retrieve similar configs -> write audit notes -> stop or request approval
```

## Boundaries

- Mock/local runs are allowed.
- Real Apify runs require an approval packet with actor, input scope, max items, timeout, storage destination, and spend ceiling.
- Public social engagement sources only.
- No outreach, Telegram automation, CRM sync, external export, private/login-only scraping, cookies, or evasion settings.
- Optional RAG and memory compression must degrade gracefully when OpenAI or Anthropic dependencies are absent.

## Primary Files

- `README.md`: current overview and approval gates.
- `QUICKSTART.md`: mock-first usage.
- `HERMES_ADAPTER.md`: Hermes wrapper contract.
- `orchestrator.py`: loop coordinator.
- `apify_integration.py`: mock and real Apify clients.
- `rag/`: optional semantic retrieval.
- `memory/`: optional compression and local summaries.
