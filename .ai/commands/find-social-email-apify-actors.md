# Command - Find Social Email Apify Actors

Purpose: find Apify actors for `scape-data` without breaking the public-only email/contact rules.

Read first:

```text
README.md
AGENTS.md
docs/apify-active-actors.md
docs/apify-social-actor-discovery-prompt.md
docs/runbook-forex-social-engagement-lead-batch.md
knowledge/distilled/playbooks/question-first-social-demand-mining.md
```

Prompt:

```text
Find Apify actor candidates for the scape-data social email pipeline.

Do not look for email actors only. Search by pipeline role:
1. public post/source discovery;
2. public comment/reply engagement collection;
3. public profile/email enrichment.

Use question-first demand mining. Prefer actors that can find repeated public questions and preserve source evidence.

For each actor return:
actor_id_or_slug, platform, pipeline_role, required_inputs, useful_output_fields, email_fields, public_source_evidence, needs_login_or_cookie, pricing_note, risk, tiny_test_input, decision.

Decision must be one of:
active_whitelist_candidate, test_in_console, reference_only, reject.

Do not add anything to active whitelist until the user confirms the actor works in Apify Console.
```
