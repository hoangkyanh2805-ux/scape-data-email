# Human Approval Gates

Agents must stop and request approval before any of these gates.

## Gates

- Spend money or use paid API capacity beyond an existing ceiling.
- Send outreach through email, SMS, DM, postcard, phone, or social account.
- Publish a landing page, property page, public dashboard, ad, or downloadable asset.
- Launch, pause, or modify ads, audiences, budgets, or tracking destinations.
- Share full lead details with a buyer, partner, or external system.
- Mark a lead sold, exclusive, transferred, or closed-won.
- Use credentials, secrets, or a connected external account not already scoped for the run.
- Apply a self-improving prompt/config change to production behavior.
- Retry after 3 tool failures, a rate-limit, quota warning, budget warning, or conflicting source-of-truth state.

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