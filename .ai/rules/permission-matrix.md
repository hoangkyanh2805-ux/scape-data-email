# Permission Matrix

Default rule: if an action affects money, customer-facing output, production data, access control, account reputation, privacy/contact data, or irreversible state, require human approval.

| Action | Autonomous | Approval Required | Forbidden |
|---|---:|---:|---:|
| Read repo docs/configs/public references | Yes | No | No |
| Create draft docs, tables, reports, copy, renders | Yes | No | No |
| Capture public source evidence with URL/timestamp | Yes | No | No |
| Run mock/local tests | Yes | No | No |
| Run approved scraper within quota ceiling | Yes | If no ceiling exists | No |
| Prepare Apify actor input packet | Yes | No | No |
| Run paid/high-volume Apify actor | Only within written ceiling | Yes | No over-ceiling use |
| Collect public comments/replies in approved small batch | Yes | If no ceiling exists | No |
| Collect likers/followers at scale | No | Yes | No autonomous scale scrape |
| Use paid APIs/media/ad tools | Only within written ceiling | Yes | No over-ceiling use |
| Discover public email from profile/bio/search snippet | Yes, draft/review only | For scale/export/validation | No private contact panels |
| Validate/generate/enrich emails at scale | No | Yes | No autonomous validation/generation |
| Export full contact rows to Sheets/Airtable/CRM/Drive/Telegram/buyer | No | Yes | No autonomous external export |
| Send email/SMS/DM/postcard/outreach | No | Yes | No autonomous sending |
| Login, post, comment, vote, or DM on social platforms | No | Human-only | Agent automation forbidden |
| Use login cookies/session tokens/private groups | No | Yes for explicitly scoped private access | No silent use |
| Publish pages, ads, dashboards, or public assets | No | Yes | No autonomous publishing |
| Launch/pause/change ad budget | No | Yes | No autonomous budget changes |
| Transfer or sell lead details | No | Yes | No autonomous transfer/sale |
| Mark lead sold/exclusive | No | Yes | No autonomous marking |
| Delete or overwrite records/history | No | Yes plus backup | No autonomous deletion |
| Self-improve prompts/configs | Propose and log only | Yes before production apply | No silent mutation |
| Use proxy/VPN/fingerprint workaround to evade limits | No | No | Forbidden |

## Evidence Required For Approval

Approval packets must include goal, exact action, affected records, source evidence, estimated cost, risk notes, rollback/undo option, expiry, and requested scope.

## Contact Data Rules

- Public email is a review signal, not consent.
- Every email must have `email_source_url`, `email_source_field`, and `source_date` when available.
- External reports should redact emails unless full-contact export is explicitly approved.
- Rejected and duplicate rows must remain auditable but cannot be used for outreach.
