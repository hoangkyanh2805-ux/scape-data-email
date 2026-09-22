# Command: Hermes Draft Run

Use this command when starting a Hermes or multi-agent batch.

1. Read `docs/hermes-runtime-architecture.md`.
2. Confirm `draft_only: true`.
3. Create a run id.
4. Inventory tools, secrets, quotas, budgets, and storage.
5. Run only autonomous actions allowed by `.ai/rules/permission-matrix.md`.
6. Write source evidence and draft artifacts.
7. Stop at the first approval gate and produce the stop report.
8. End with a report listing outputs, blockers, costs, and approval requests.