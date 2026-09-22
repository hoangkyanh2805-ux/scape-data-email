# @precisox Self-Improving AI Agent Video Notes

## Source Inventory

- Type: X video post metadata and local reconstructed notes
- Primary URL: https://x.com/precisox/status/2076152320585343132/video/1
- Public text mirror: https://threadnavigator.com/thread/2076152320585343132/
- Local prior notes: `repo.md`, `AGENT-SELF-IMPROVING-GUIDE.md`
- Author/context: @precisox shared a 61:41 video about building self-improving AI agents from zero.
- Confidence: medium. Thread Navigator exposes title, duration, and chapter timestamps, but no full public transcript was available during capture. This file is a paraphrased reconstruction from public timestamps plus existing local notes, not a verbatim transcript.

## Public Timestamp Outline

| Timestamp | Public chapter label | Working interpretation |
|---|---|---|
| 00:00 | How a self-building agent is born | Agents need an operating identity and improvement loop, not only a model call. |
| 03:01 | `soul.md`, the file that controls everything | Put concise identity, hard rules, accountability, and uncertainty behavior in a small markdown contract. |
| 30:16 | Smart RAG: retrieve 20 relevant messages, not 2,000 | Use semantic retrieval and bounded context instead of dumping history into the prompt. |
| 31:48 | The loop that knows when to stop | Add quality gates and stop after repeated non-improvement. |
| 35:14 | Detect the error and fix the prompt in the moment | Detect failures, propose a fix, version it, rerun, compare, and keep only useful changes. |
| 50:22 | How Claude compresses and optimizes memory automatically | Periodically summarize long-running context into compact snapshots with pointers to exact records. |

## Non-Verbatim Script Reconstruction

### 00:00 - Opening Thesis

The video frames the common failure mode of agents as an architecture problem. The model may be strong, but the agent drifts or collapses because it lacks a stable identity, bounded memory, an evaluation loop, and a clean way to learn from errors.

Reusable mechanism: an agent should start from a compact operating contract, then improve through a loop of execution, evaluation, correction, and memory compression.

### 03:01 - `soul.md` As Identity Contract

The core pattern is a small `soul.md`: who the agent is, what rules it must never break, how it checks itself, and what it does when uncertain. The useful part is not personality theater. The useful part is behavioral consistency plus accountability.

Project implication: every runtime agent in this repo should have a short contract that includes identity, scope, hard rules, self-check, stop conditions, and human approval boundaries.

### 30:16 - Semantic RAG Instead Of Context Dumping

The video argues against loading huge histories into context. The better pattern is retrieval: embed the task and records, retrieve the most relevant chunks, and keep `top_k` bounded. A baseline around 20 chunks is a starting point, not a law.

Project implication: Hermes and scraper agents should retrieve source evidence, prior runs, and approval records by relevance, while keeping pointers to exact source records for audit.

### 31:48 - Termination By Quality Gate

The loop should not run forever. It needs a measurable improvement function and a convergence rule. If two iterations do not improve, the agent should stop, report why, and hand off for review.

Project implication: `agent-lead-scraper/loop/terminate.py` already implements this pattern. Hermes should reuse the same rule for drafts, scrape runs, and self-improvement proposals.

### 35:14 - Error Detection And Prompt/Config Self-Fix

Errors should be turned into versioned learning. The safe loop is: detect error, classify it, propose a fix, save the proposed change, rerun only within permission limits, compare before/after, then keep or reject the fix.

Project implication: prompt/config self-improvement must stay draft-first. Production behavior changes require an approval gate.

### 50:22 - Memory Compression With Pointers

Long-running agents need compact memory. The video pattern is to compress accumulated context into a dense summary while preserving pointers to full records. Summaries are useful for continuity, but critical decisions need exact source lookup.

Project implication: memory snapshots belong in `agent-lead-scraper/memory/snapshots/` and audit summaries should include source ids, run ids, and approval ids.

## Copyright And Accuracy Note

This file does not contain a verbatim transcript. It is a project-oriented reconstruction from public chapter metadata, local notes, and domain interpretation. If a legally available transcript is later obtained, store it separately under `knowledge/raw/video-notes/` and regenerate the distilled playbook.