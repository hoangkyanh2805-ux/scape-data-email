# Lead Scraper Agent

`agent-lead-scraper` is the local prototype for the `scape-data` public social-email pipeline. It is a draft-first Apify runner and self-improvement loop for testing actor inputs, error handling, quality scoring, RAG retrieval, and memory compression.

It is not an outreach system, CRM sync, Telegram gateway, or permission to run paid/high-volume actors. Use mock runs by default. Real Apify runs require the approval packet described in [HERMES_ADAPTER.md](HERMES_ADAPTER.md) and the repo permission matrix.

## Scape-Data Runtime Defaults

```yaml
research_only: true
public_data_only: true
outreach_enabled: false
external_export_enabled: false
max_cost_requires_approval: true
emails_redacted_in_reports: true
```

Use this component only for public social engagement workflows, starting with Forex-related TikTok and YouTube sources.

## Quick Start

See [QUICKSTART.md](QUICKSTART.md) for a mock-first walkthrough.

```python
from orchestrator import SelfImprovingOrchestrator
from apify_integration import MockApifyClient

mock_client = MockApifyClient()
orchestrator = SelfImprovingOrchestrator(
    apify_client=mock_client,
    initial_config={
        "platform": "tiktok",
        "query": "xauusd forex beginner",
        "search_query": "xauusd forex beginner public comments",
        "max_posts": 5,
        "max_comments_per_post": 25,
        "batch_size": 25,
        "public_data_only": True,
    },
    actor_name="mock_public_social_engagement_actor",
    max_iterations=3,
)
result = orchestrator.run_improvement_loop()
```

## Project Structure

```text
agent-lead-scraper/
  README.md                       # This file
  QUICKSTART.md                   # Mock-first setup and usage
  HERMES_ADAPTER.md               # Hermes safety wrapper and approval contract
  soul.md                         # Agent identity and accountability loop
  orchestrator.py                 # Main self-improving loop coordinator
  apify_integration.py            # Apify client wrapper and mock client
  requirements.txt                # Python dependencies
  rag/
    embed.py                      # Semantic embedding
    retrieve.py                   # Cosine similarity retrieval
    config.yaml                   # Retrieval settings
  loop/
    evaluation.py                 # Quality evaluation engine
    terminate.py                  # Quality gate and stop conditions
    config.yaml                   # Loop settings
  error_fix/
    detect.py                     # Error detection
    fix_prompt.py                 # Proposed config fixes and versioning
    config.yaml                   # Error handling strategy
    prompt_history/               # Versioned fix proposals
  memory/
    compress.py                   # Memory snapshot generation
    config.yaml                   # Compression settings
    snapshots/                    # Summaries and pointers
```

## Architecture

```text
validate scope -> run mock/approved actor -> detect errors -> propose config fix -> evaluate quality -> retrieve similar runs -> write run history -> stop or request approval
```

The loop optimizes data quality and actor configuration. It must not convert candidates into approved leads, send messages, export full contact rows, or bypass platform/privacy limits.

## Components

| Component | File | Purpose |
|---|---|---|
| Orchestrator | `orchestrator.py` | Coordinates actor runs, fixes, evaluation, RAG, and memory |
| Apify Integration | `apify_integration.py` | Real client wrapper plus mock client for local tests |
| Evaluation | `loop/evaluation.py` | Scores dedupe, validation, volume, and error recovery |
| Termination | `loop/terminate.py` | Stops after plateau, quality target, max iterations, or errors |
| Error Fix | `error_fix/` | Detects rate limit/config/parsing/validation failures and proposes fixes |
| RAG | `rag/` | Retrieves similar prior configs when embeddings are available |
| Memory | `memory/` | Creates compact run summaries with local fallback |

## Approval Gates

Stop and produce an approval packet before:

- any paid or high-volume Apify run;
- collecting contact data at scale;
- increasing batch size, retry count, actor count, or spend ceiling;
- using cookies, login sessions, private groups, proxies, or evasion settings;
- exporting full contact rows outside local approved storage;
- validating, generating, or guessing emails at scale;
- sending outreach, Telegram messages, CRM syncs, or lead transfers.

## Expected Outputs

A safe run should emit local, reviewable artifacts only:

```text
actor_runs.yaml
lead_candidates.csv
batch_report.md
approval_packet.md
```

Emails in reports should be redacted unless a full-contact export is explicitly approved.

## Status

Local prototype: ready for mock testing and approval-gated Apify experiments. Not production automation.


