# Install And Adapt Runbook

## Step 1 - Copy Bundle

Copy this bundle into the target project:

```text
agent-os/self-improving-agent-os/
```

## Step 2 - Map Project Folders

Recommended target structure:

```text
.ai/
  agents/
  rules/
  schemas/
  runbooks/
  audit/
docs/
  agent-loop-operating-model.md
  permission-matrix.md
  human-approval-gates.md
```

## Step 3 - Adapt Agent Contracts

For each agent, update:

- project name;
- allowed tools;
- output records;
- quality metrics;
- approval gates;
- stop conditions.

## Step 4 - Configure Runtime

Set:

```yaml
draft_only: true
max_iterations: 5
stop_after_non_improving_iterations: 2
stop_after_repeated_tool_failures: 3
default_retrieval_top_k: 20
```

## Step 5 - Inventory Tools

List:

- local file access;
- browser/search/scraper;
- storage/state store;
- CRM/sheets;
- content/render tools;
- email/SMS/posting/ad providers;
- budget ceilings;
- missing secrets.

## Step 6 - Dry Run

First run must produce:

- tool inventory;
- source list;
- draft outputs;
- risk notes;
- approval requests;
- final report;
- memory snapshot.

## Step 7 - Production Handoff

Enable live tools only when:

- permission matrix is project-specific;
- approval gates are explicit;
- schemas are being written;
- audit logger is working;
- external-impact actions are blocked before approval.