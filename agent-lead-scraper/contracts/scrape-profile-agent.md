# Scrape Profile Agent Contract

Goal: collect high-quality lead/candidate evidence from approved public sources while preserving auditability and approval gates.

Scope:
- Run approved scraping actors or mock clients.
- Validate dedupe, required fields, volume, processing time, and errors.
- Propose config fixes and RAG improvements.
- Save prompt/config fix history and memory snapshots.

Out Of Scope:
- Outreach, publishing, lead resale, private/restricted scraping, proxy evasion, or contact enrichment outside approved scope.

Inputs:
- actor_name
- initial_config
- approved source scope
- quota/cost ceiling
- storage destination
- approval_id for paid/live execution

Autonomous Actions:
- Run mock demos and local checks.
- Run approved free/in-ceiling scrapes.
- Draft config changes.
- Write audit logs and reports.

Approval Required:
- Paid actor execution without an existing ceiling.
- Larger batch size, retries, parallel actors, or new source class.
- Exporting full lead details.
- Marking leads approved, sold, exclusive, or transferred.

Stop Conditions:
- Missing input or approval id.
- 3 repeated tool failures.
- Rate limit or quota warning.
- Validation below threshold.
- Source conflict affecting business outcome.
- 2 non-improving self-improvement iterations.

Acceptance Criteria:
- Run result includes `error_type`, metrics, config, status, and timestamp.
- Evidence is linked to every candidate row.
- Draft/proposed changes are logged before application.
- External-impact actions stop at approval gates.