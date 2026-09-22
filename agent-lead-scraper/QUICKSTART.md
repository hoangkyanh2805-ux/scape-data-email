# Lead Scraper Agent - Quick Start

This guide runs `agent-lead-scraper` safely for `scape-data`.

Default path: mock-first, local-only, public-data-only. Do not run real Apify actors until an approval packet exists for the exact actor, input scope, item ceiling, storage destination, timeout, and spend ceiling.

## Setup

### 1. Install dependencies

```bash
cd agent-lead-scraper
pip install -r requirements.txt
```

### 2. Optional environment variables

Mock runs do not need API keys.

```bash
# Optional for real, approved Apify runs only
export APIFY_API_TOKEN="apify_..."

# Optional enhancements; the code should fall back when absent
export OPENAI_API_KEY="..."
export ANTHROPIC_API_KEY="..."
```

### 3. Verify the local test path

```bash
python test_orchestrator.py
```

## Usage

### Option A: Mock client, recommended

```python
from orchestrator import SelfImprovingOrchestrator
from apify_integration import MockApifyClient

mock_client = MockApifyClient(failure_rate=0.1)

initial_config = {
    "platform": "tiktok",
    "query": "xauusd forex beginner",
        "search_query": "xauusd forex beginner public comments",
    "max_posts": 5,
    "max_comments_per_post": 25,
        "batch_size": 25,
    "public_data_only": True,
    "login_required": False,
    "include_private_sources": False,
}

orchestrator = SelfImprovingOrchestrator(
    apify_client=mock_client,
    initial_config=initial_config,
    actor_name="mock_public_social_engagement_actor",
    max_iterations=3,
)

result = orchestrator.run_improvement_loop()
print(result)
```

### Option B: Real Apify actor, approval required

Use this only after the human approves a packet like this:

```yaml
approval_id:
actor_id:
actor_url:
platform:
input_scope:
max_items:
max_runs:
timeout_seconds:
estimated_cost:
budget_ceiling:
storage_destination:
public_data_only: true
outreach_enabled: false
external_export_enabled: false
approval_status: approved
```

Then keep the run small and scoped:

```python
from orchestrator import SelfImprovingOrchestrator
from apify_integration import ApifyClient

apify_client = ApifyClient()

approved_config = {
    "startUrls": ["https://www.tiktok.com/tag/xauusd"],
    "maxItems": 25,
    "maxCommentsPerPost": 25,
    "publicDataOnly": True,
}

orchestrator = SelfImprovingOrchestrator(
    apify_client=apify_client,
    initial_config=approved_config,
    actor_name="approved_actor_slug_here",
    max_iterations=1,
    conversation_pointer="data/forex-social-intent/runs/<run-id>/batch_report.md",
)

result = orchestrator.run_improvement_loop()
```

## Safe Loop

```text
validate scope -> run mock or approved actor -> collect metrics -> detect errors -> propose fix -> evaluate quality -> write run history -> stop or request approval
```

## Quality Metrics

The evaluator scores:

- deduplication quality;
- visible source/contact-field validation;
- usable candidate volume within the ceiling;
- error recovery.

A high score does not approve outreach or export. It only helps decide whether the source/actor/input deserves human review.

## Troubleshooting

### `ANTHROPIC_API_KEY not set`

Memory compression can use a local fallback. Mock runs can continue.

### RAG cannot embed configs

Check `OPENAI_API_KEY` if you need semantic retrieval. The loop can still run without RAG suggestions.

### Rate-limit errors repeat

Stop after repeated failures. Do not increase batch size, retry count, actor count, proxies, or spend ceiling without approval.

### Actor schema errors

Use the error-fix output as a proposed config patch. Confirm the current Apify Store schema before any live run because actor inputs and pricing change.

## Next Safe Steps

1. Run mock tests locally.
2. Draft an Apify actor approval packet for one platform and one tiny input scope.
3. Store outputs under `data/forex-social-intent/runs/<YYYYMMDD-HHMM>/`.
4. Review yield, evidence quality, and contact-data risk before scaling.

## Status

Ready for local mock testing and approval-gated Apify experiments. Not approved for production automation, outreach, external export, Telegram automation, or CRM sync.


