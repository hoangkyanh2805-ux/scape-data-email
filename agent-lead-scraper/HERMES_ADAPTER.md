# Hermes Adapter For Lead Scraper

This adapter defines how Hermes should wrap `agent-lead-scraper` safely.

## Role

`agent-lead-scraper` is the Scrape/Profile Agent implementation. It may run approved actors, collect metrics, detect errors, propose config fixes, retrieve similar past runs, and write memory snapshots.

## Default Mode

Hermes must start this component with `draft_only: true` and a mock or explicitly approved Apify client. Real paid actor execution requires an approval record with actor allowlist, query scope, max runs, timeout, and spend ceiling.

## Required Inputs

- `actor_name`
- `initial_config`
- `source_scope`
- `quota_ceiling`
- `storage_destination`
- `approval_id` for real paid runs

## Output Contract

Each run should emit:

```yaml
run_id:
actor_name:
status:
config_hash:
lead_count:
deduplication_rate:
lead_validation_rate:
processing_time:
error:
error_type:
source_refs:
cost_estimate:
approval_id:
next_action:
```

## Gates

Stop before:

- paid actor usage without approval;
- increasing batch size, retries, or actor count beyond ceiling;
- exporting full lead details outside the approved storage destination;
- treating unreviewed scrape output as approved leads;
- retrying after 3 failures or any 429/rate-limit loop;
- applying self-improved config to production without review.

## Safe Hermes Loop

```text
load contract -> validate inputs -> run mock/free batch -> collect metrics -> propose fixes -> write audit -> request approval or stop
```

## Notes

RAG and memory compression depend on external APIs. If `OPENAI_API_KEY` or `ANTHROPIC_API_KEY` is absent, Hermes should continue with local/mock operation and log that the enhancement was skipped.