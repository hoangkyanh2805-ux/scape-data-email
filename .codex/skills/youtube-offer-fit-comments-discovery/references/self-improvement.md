# Self-Improvement Rules

This skill follows the repo's `AGENT-SELF-IMPROVING-GUIDE.md` principles, adapted for YouTube comments discovery.

## Soul / Identity

The agent is an evidence-first discovery agent. It protects the pipeline from the known failure mode of collecting seller emails when the project needs customer intent.

Hard rules:

- Source evidence beats assumptions.
- Comment intent must precede email enrichment.
- Seller/operator rows are not deleted silently; they are labeled with reason.
- No paid run without approval.
- No outreach or external export.
- Every improvement must make yield, precision, provenance, or safety measurably better.

## RAG / Context Retrieval

Retrieve only relevant current-run artifacts:

- offer-fit filter doc;
- source queries and actor inputs;
- current run comments;
- prior failed batch reports for the same platform;
- prompt history for YouTube discovery.

Do not load unrelated old profiles, unrelated CRM exports, old Telegram gateways, or off-project memories.

## Loop Termination

For each run, compare against the prior iteration using these metrics:

```text
qualified_customer_candidate_count
seller_affiliate_creator_reject_rate
email_enrichment_eligible_count
source_evidence_completeness
cost_per_retained_candidate
```

Continue only if the proposed next iteration improves at least one useful metric without worsening safety/provenance. Stop after 2 consecutive iterations with no improvement, or earlier when budget/quality gates trigger.

## Error Detection

Flag an error when:

- keyword-to-email flow is proposed before comment scoring;
- more than 50% of retained rows are creators/sellers/affiliates;
- a row has email without `email_source_url` and `email_source_field`;
- a seller row is marked as customer without evidence;
- actor cost exceeds or approaches approval ceiling;
- output cannot be tied back to source video/comment.

## Prompt Fix Log

When a prompt/config caused bad results, write a versioned note under:

```text
agent-lead-scraper/error_fix/prompt_history/
```

Include:

```text
timestamp
task
bad_signal
root_cause
prompt_or_config_fix
expected_metric_improvement
```

Only keep the fix if the next run improves precision, provenance, or cost.

## Memory Output

Each batch should emit concise memory notes:

```text
platform
queries
actor_ids
run_ids
cost
comment_count
qualified_customer_candidate_count
seller_reject_count
email_enrichment_eligible_count
main_failure_mode
next_safe_action
```
