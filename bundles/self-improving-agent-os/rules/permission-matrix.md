# Permission Matrix

Default rule: if an action affects money, customer-facing output, production data, access control, account reputation, or irreversible state, require human approval.

| Action | Autonomous | Approval Required | Forbidden |
|---|---:|---:|---:|
| Read repo docs/configs/public references | Yes | No | No |
| Create draft docs, tables, reports, copy, renders | Yes | No | No |
| Capture public source evidence with URL/timestamp | Yes | No | No |
| Run mock/local tests | Yes | No | No |
| Run approved scraper within quota ceiling | Yes | If no ceiling exists | No |
| Use paid APIs/media/ad tools | Only within written ceiling | Yes | No over-ceiling use |
| Send email/SMS/DM/postcard/outreach | No | Yes | No autonomous sending |
| Login, post, comment, vote, or DM on Reddit | No | Human-only | Agent automation forbidden |
| Publish pages, ads, dashboards, or public assets | No | Yes | No autonomous publishing |
| Launch/pause/change ad budget | No | Yes | No autonomous budget changes |
| Transfer or sell lead details | No | Yes | No autonomous transfer/sale |
| Mark lead sold/exclusive | No | Yes | No autonomous marking |
| Delete or overwrite records/history | No | Yes plus backup | No autonomous deletion |
| Self-improve prompts/configs | Propose and log only | Yes before production apply | No silent mutation |
| Use proxy/VPN/fingerprint workaround to evade limits | No | No | Forbidden |

## Evidence Required For Approval

Approval packets must include goal, exact action, affected records, source evidence, estimated cost, risk notes, rollback/undo option, expiry, and requested scope.