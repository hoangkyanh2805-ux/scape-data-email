# Human Approval Gates

Agents must stop and request approval before any of these gates.

## Gates

- Spend money or use paid API capacity beyond an existing ceiling.
- Run any Apify actor without an approved actor run packet when the run is paid, high-volume, or touches contact data.
- Scrape high-volume likers/followers or any source without text intent evidence.
- Use login cookies, session tokens, private/restricted communities, or connected external accounts.
- Validate, generate, infer, or enrich emails at scale.
- Export full contact rows to Google Sheets, Airtable, CRM, Drive, Telegram, a buyer, or any external system.
- Send outreach through email, SMS, DM, postcard, phone, or social account.
- Publish a landing page, property page, public dashboard, ad, or downloadable asset.
- Launch, pause, or modify ads, audiences, budgets, or tracking destinations.
- Share full lead details with a buyer, partner, or external system.
- Mark a lead sold, exclusive, transferred, or closed-won.
- Use credentials, secrets, or a connected external account not already scoped for the run.
- Apply a self-improving prompt/config change to production behavior.
- Retry after 3 tool failures, a rate-limit, quota warning, budget warning, or conflicting source-of-truth state.

## Apify Run Approval Record

```yaml
approval_id:
requested_by_agent:
platform:
actor_id:
actor_url:
input_summary:
max_sources:
max_posts:
max_comments_per_post:
max_profiles_to_enrich:
estimated_cost_usd:
budget_ceiling_usd:
uses_login_or_session: false
uses_private_sources: false
storage_target:
risk_notes:
rollback_plan:
approver:
status:
expires_at:
```

## Contact Export Approval Record

```yaml
approval_id:
requested_by_agent:
export_destination:
record_count:
fields_included:
redaction_mode:
evidence_refs:
privacy_risks:
rollback_plan:
approver:
status:
expires_at:
```

## Stop Report Format

```text
Stopped because:
Goal affected:
Evidence:
Safe next options:
Recommended option:
Approval/input needed:
```

## Approval Record

```yaml
approval_id:
requested_by_agent:
action:
scope:
evidence_refs:
budget_ceiling:
risk_notes:
rollback_plan:
approver:
status:
expires_at:
```
