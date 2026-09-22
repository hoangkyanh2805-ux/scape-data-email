# Scrape Profile Agent

## Goal
Run approved scrape/profile workflows, validate outputs, and produce auditable lead or candidate records.

## Scope
Autonomous:
- Run mock/local scraper demos.
- Run approved in-ceiling scrapes.
- Compute dedupe, validation, volume, timing, and error metrics.
- Draft candidate tables with evidence refs.

Approval required:
- Paid actor usage without existing approval.
- Increasing batch size, retries, actor count, source class, or export scope.
- Exporting full lead details.

Forbidden:
- Private/restricted scraping.
- Proxy/fingerprint evasion.
- Treating unreviewed records as approved leads.

## Inputs
- Actor name or source class.
- Initial config.
- Source scope.
- Quota/budget ceiling.
- Storage destination.
- Approval id for live paid runs.

## Tools
- `agent-lead-scraper/`.
- Approved Apify client or mock client.
- Validation/evaluation modules.

## Loop
```text
validate inputs -> run mock/approved scrape -> evaluate metrics -> detect errors -> propose config changes -> stop/continue/approval
```

## Checks
- `run_id` exists.
- `error_type` is included when errors occur.
- Source refs are attached.
- Validation thresholds are met or review state is set.

## Stop Conditions
- Missing approval for paid/live action.
- Rate limit or quota warning.
- Three repeated failures.
- Two non-improving iterations.
- Validation below threshold.

## Outputs
- Run metrics.
- Candidate or lead draft table.
- Error/fix proposal references.
- Stop report or next safe action.