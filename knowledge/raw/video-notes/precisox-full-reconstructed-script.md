# Full Reconstructed Script - Self-Improving AI Agent Video

## Source And Confidence

- Original source requested: https://x.com/precisox/status/2076152320585343132/video/1
- Public metadata mirror: https://threadnavigator.com/thread/2076152320585343132/
- Related English mirror: https://threadnavigator.com/thread/2075607221397012680/
- Duration visible in mirrors: 61:41
- Confidence: medium for chapter structure, low for exact wording.

Important: this is a reconstructed/paraphrased script for project use. It is not a verbatim transcript. Public search found chapter metadata but no complete public transcript.

## Chapter 00:00 - The Self-Building Agent

### Reconstructed Script

Most agent failures are not caused by weak models. They happen because the agent has no stable operating system around the model. It starts with vague instructions, gets a huge context dump, takes a few actions, loses the thread, and then either loops forever or collapses into generic chatbot behavior.

A real self-improving agent needs five layers. First, it needs identity: who it is, what it optimizes for, what it refuses to do, and how it handles uncertainty. Second, it needs retrieval: not every memory, only the relevant memory. Third, it needs a loop that can measure improvement. Fourth, it needs error detection and a way to propose fixes. Fifth, it needs compressed memory so it can keep running without drowning in its own history.

The goal is not an agent that magically rewrites itself without control. The goal is an agent that can observe its result, compare it against a standard, propose a better next run, and stop when further iteration no longer helps.

### Mechanism

```text
identity -> retrieval -> action -> evaluation -> fix proposal -> memory update -> stop/continue
```

### Project Takeaway

Use this as the base operating loop for Hermes and every specialized sub-agent in this repo.

## Chapter 03:01 - `soul.md` Runs Everything

### Reconstructed Script

The first file is `soul.md`. It should not be a giant essay. Long personality files usually make the agent worse because the important rules get buried. A good soul file is short enough to be read every time and specific enough to shape behavior.

The file should say who the agent is, how it thinks, which rules are non-negotiable, what it checks before delivering work, and what it does when it is unsure. The accountability loop is the important part. The agent should not simply answer; it should verify whether the answer is grounded.

Bad soul files say things like: be helpful, be friendly, do your best. Those are too abstract. Better soul files include rules like: never fabricate sources, separate facts from inference, state uncertainty, stop before external actions, and ask for approval when the permission matrix says so.

### Template

```markdown
# <Agent Name>

## Who I Am
I am a <role> agent. I optimize for <primary outcome> while preserving evidence, auditability, and safe handoff.

## Hard Rules
- Never fabricate sources, metrics, or approvals.
- Separate source facts from inference.
- Keep all external-impact work in draft state until approved.
- Preserve exact source pointers for important claims.
- Version every prompt/config self-fix.
- Stop when evidence, permission, or quality is insufficient.

## Accountability Loop
Before every substantial output, I check:
1. Did I verify the source or mark the gap?
2. Did I stay inside my permission scope?
3. Did I produce a measurable next action?

If any answer is no, I stop and report the blocker.

## When In Doubt
Say what is unknown, show the evidence, and ask for the smallest missing input.
```

### Project Takeaway

Each Hermes agent should have a compact identity contract. `agent-lead-scraper/soul.md` is the implementation example; `.ai/agents/` should contain the runtime contracts.

## Chapter 30:16 - RAG Memory: Pull Relevant Context, Not Everything

### Reconstructed Script

The common mistake is to put the whole conversation or all previous runs into context. That feels safe, but it makes the model less precise. The model starts paying attention to stale, irrelevant, or contradictory details.

The better pattern is semantic retrieval. Convert records into embeddings. Convert the current task into an embedding. Retrieve a bounded number of relevant chunks. Twenty relevant chunks is a reasonable starting point for simple tasks, but it is not a universal law. Harder tasks may need more. The key is that retrieval is selected, scored, and traceable.

The agent should also keep source pointers. A summary is useful for orientation, but important claims need a pointer back to the exact record, URL, run id, or approval id.

### Retrieval Policy

```yaml
retrieval:
  default_top_k: 20
  complex_task_top_k: 30-40
  require_source_pointer: true
  never_use_summary_as_exact_evidence: true
```

### Project Takeaway

Use RAG for source evidence, prior scrape runs, prompt versions, approval records, and memory snapshots. Do not dump full history into Hermes.

## Chapter 31:48 - The Loop That Knows When To Stop

### Reconstructed Script

A self-improving loop without a stop rule is dangerous. The agent can keep making changes that look different but are not better. A real loop has a quality gate.

The loop starts with a current result. It proposes an improvement. It evaluates whether the new result is better by a defined metric. If it improves, continue. If it does not improve, count that as a failed improvement. After two non-improving iterations, stop and return the best version.

Max iterations are only a safety rail. They are not the main stop condition. The main stop condition is lack of measurable improvement.

### Loop Template

```python
def self_improvement_loop(run, evaluate, improve, max_iterations=5, max_no_improve=2):
    current = run()
    best = current
    no_improve = 0

    for iteration in range(max_iterations):
        proposed = improve(current)
        score = evaluate(current, proposed)

        if score > 0:
            current = proposed
            best = proposed
            no_improve = 0
        else:
            no_improve += 1
            if no_improve >= max_no_improve:
                return best, "stopped: no measurable improvement"

    return best, "stopped: max iterations"
```

### Project Takeaway

The repo already has this pattern in `agent-lead-scraper/loop/terminate.py`. Reuse it for draft generation, scrape optimization, report generation, and prompt/config self-improvement.

## Chapter 35:14 - Find The Bug, Fix The Prompt

### Reconstructed Script

When an agent fails, do not just rerun blindly. Detect the error, classify it, identify the likely root cause, propose a fix, save the proposed fix with a timestamp, run again within safe limits, and compare the before/after result.

The important part is versioning. If the agent changes prompts or configuration without a history, the system becomes a black box. Every fix needs a record: what failed, what changed, why it changed, and whether the change improved the result.

For production systems, the agent may propose fixes autonomously, but applying a fix to production behavior should require approval when the change affects money, outreach, publishing, lead transfer, permissions, or external accounts.

### Fix Record Template

```yaml
fix_id:
timestamp:
agent:
run_id:
error_type:
root_cause:
previous_prompt_or_config:
proposed_prompt_or_config:
validation_result:
improvement_score:
status: proposed | approved | applied | rejected | reverted
approval_id:
```

### Project Takeaway

`agent-lead-scraper/error_fix/` should be treated as a proposal engine. Hermes may draft fixes, but approval gates decide when they become production behavior.

## Chapter 50:22 - Claude Compresses Memory

### Reconstructed Script

Long-running agents eventually hit memory pressure. The wrong solution is to keep stuffing old messages into the prompt. The better solution is periodic compression.

A compression snapshot should capture the important decisions, patterns, metrics, open questions, and next actions. It should be short enough to load quickly and dense enough to restore context. But it should never be the only record. It needs pointers back to the original messages, runs, sources, and approvals.

The agent can use a strong language model to summarize, but it must treat the summary as orientation. For exact facts, it must retrieve the original source.

### Snapshot Template

```yaml
snapshot_id:
created_at:
agent:
covered_run_ids:
source_ids:
approval_ids:
summary:
patterns:
open_questions:
blocked_items:
next_safe_action:
```

### Project Takeaway

Store scraper snapshots in `agent-lead-scraper/memory/snapshots/`. Store cross-agent audit snapshots under `.ai/audit/` or a future state store.

## Chapter 58:00 - Final Operating Checklist

### Reconstructed Script

To build the agent today, implement the five layers in order:

1. Write the compact identity contract.
2. Add semantic retrieval with source pointers.
3. Add the quality-gated improvement loop.
4. Add error detection and versioned self-fix proposals.
5. Add compressed memory snapshots with exact pointers.

Then add safety. A self-improving agent should not automatically spend money, send outreach, publish, login to accounts, transfer leads, or rewrite production policy. It should stop, present evidence, and request approval.

### Project Takeaway

This repo already has most of the technical skeleton. The next step is operational discipline: agent contracts, approval gates, deterministic tests, and audit records.