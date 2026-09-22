# Hermes Runtime Architecture

Hermes should be used as a persistent runtime and coordinator, not as a permission bypass. The source of truth remains the repo: docs, `.ai/` contracts, skill packages, and audit logs.

## Bootstrap Sequence

1. Read `docs/agent-loop-operating-model.md`.
2. Read `.ai/rules/permission-matrix.md` and `.ai/rules/human-approval-gates.md`.
3. Inventory available tools, credentials, budgets, and storage destinations.
4. Start in `draft_only: true` mode.
5. Run one small batch with mock or approved free tooling.
6. Produce an approval packet before any paid, published, account, outreach, or lead-transfer action.

## Runtime Components

- Scheduler: starts daily/weekly/manual runs.
- Queue: holds agent tasks and approval requests.
- State Store: keeps candidates, sources, drafts, leads, approvals, spend, and audit records.
- Tool Adapter Layer: wraps Apify, browser/scraper, CRM/sheets, render tools, email/SMS/postcard providers, and notification channels.
- Audit Logger: writes immutable records for each run and approval.
- Gatekeeper: blocks actions that cross the permission matrix.

## Minimal State Records

- `run`: run_id, agent, started_at, ended_at, status, goal, input_ref, output_refs.
- `source_evidence`: source_id, url_or_path, fetched_at, hash_or_snippet, screenshot_ref, confidence.
- `candidate`: candidate_id, source_ids, qualifier, confidence, review_state.
- `draft`: draft_id, type, target, source_ids, risk_notes, status.
- `approval`: approval_id, scope, approver, evidence_refs, budget_ceiling, expires_at, status.
- `spend`: spend_id, provider, estimate, actual, approval_id.
- `lead_transfer`: transfer_id, lead_ids, buyer, terms, approval_id, status.

## Tool Boundaries

Hermes may autonomously read files, search approved public sources, run mock/local tests, create draft docs/tables, and write audit records. Hermes must stop before paid API usage beyond a pre-approved ceiling, external publishing, account login/posting, outreach sending, ad launch/change, or lead sale/transfer.

## First Production Handoff

The first live handoff must be a dry run. Required output: tool inventory, missing secrets, proposed schedule, expected costs, source list, draft outputs, risk notes, and approval requests.

## Self-Improvement Integration

Hermes should read docs/precisox-self-improving-agent-application.md before running self-improving workflows. The pattern is: identity contract, semantic retrieval, quality-gated loop, versioned self-fix, and compressed memory with source pointers. Production changes still require the approval gates in .ai/rules/human-approval-gates.md.
## Six-Agent Runtime

Hermes should use these project contracts by default:

1. `.ai/agents/runtime-orchestrator/AGENT.md`
2. `.ai/agents/soul-contract/AGENT.md`
3. `.ai/agents/rag-context/AGENT.md`
4. `.ai/agents/scrape-profile/AGENT.md`
5. `.ai/agents/error-fix/AGENT.md`
6. `.ai/agents/memory-audit/AGENT.md`

Execution runbook: `.ai/runbooks/hermes-self-improving-run.md`.

Portable bundle: `bundles/self-improving-agent-os/`.
## Desktop + Telegram Gateway

Use `docs/runbook-hermes-desktop-telegram-gateway.md` when this project needs Hermes Desktop plus Telegram as the operator channel. This differs from WhatsApp runs because Telegram uses a BotFather token and allowed chat/user ids instead of WhatsApp pairing or Cloud API credentials.

Hermes Desktop is global state and may contain old repo profiles, separate VPS connections, and unrelated Telegram gateways. This repo should only store SOPs, agent contracts, bundles, and approval gates. Treat tokens and gateway status as relevant only after the intended Hermes profile is explicitly selected and mapped to this repo.

