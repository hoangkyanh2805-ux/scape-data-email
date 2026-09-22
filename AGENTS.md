# AGENTS.md - scape-data Repo Guardrails

## Repo Identity

This workspace is `scape-data` at `G:\Other computers\My Computer\Project\scape-data`.

The active Hermes profile for this repo is `scapedata` and the Hermes project is `scape-data` (`p_8a6b3b15`). See `docs/hermes-profile-map-scape-data.md`.

## Context Boundary

Do not import assumptions, customers, brands, Telegram bots, VPS targets, or strategy from other Hermes profiles or older repos.

Specifically, do not reference unrelated projects such as Azzam, NCI Trading, forex profiles, or old Telegram gateways unless the user explicitly asks to compare against them and provides that context in the current turn.

Hermes Desktop is global state. Its `default`, `orchestrator`, `forex-*`, or remote VPS profiles are not evidence about this repo.

## Source Priority

When asked to read or analyze this project, use this order:

1. Files in this repo.
2. `docs/hermes-profile-map-scape-data.md` for Hermes profile mapping.
3. `docs/runbook-hermes-desktop-telegram-gateway.md` for Telegram gateway rules.
4. User-provided attachments in the current turn.

If a document is a framework or extracted video guide, say that clearly. Do not pretend it is application code.

## Telegram Rule

This repo does not own Telegram tokens. The `scapedata` profile must use a dedicated bot token if Telegram is needed. Do not copy or diagnose tokens from other profiles as if they belong to this repo.

No live Telegram messages, outbound notifications, posting, outreach, or gateway automation may be enabled without explicit human approval for the selected `scapedata` profile.

## Answering Rule

If a response starts mentioning a project, brand, CRM, course, trading desk, VPS, or gateway not present in the repo or user request, stop and ask for clarification instead of continuing.
