# Run Output Template

Use this shape at the end of every run or when stopping at an approval gate. Keep it concise but evidence-backed.

## Run Summary

- Pipeline: <1 / 2 / 3 / combination>
- Objective: <what the user wanted>
- Status: draft complete / blocked / approval needed / ready for next safe step
- Inputs used: <product, trade, city, table, offer, etc.>
- Missing inputs: <only required missing inputs>

## Artifacts Created

| Artifact | Location or table | Status | Notes |
|---|---|---|---|
| <name> | <path/url/table> | draft/review/approved | <short note> |

## Evidence Summary

- Source facts: <facts with source URLs/paths/dates>
- Agent inferences: <clearly marked inferences>
- Confidence: high / medium / low / review

## Review Items

| Item | Why review is needed | Recommended decision |
|---|---|---|
| <row/creative/candidate/tool> | <uncertainty or risk> | <approve / reject / inspect / provide input> |

## Cost And Quota Notes

- Estimated spend so far: <amount or none>
- Estimated next-step cost: <amount or unknown>
- Budget ceiling: <approved ceiling or missing>
- Quota/rate limit issues: <none or detail>

## Approval Gate

- Gate reached: <send / spend / publish / paid API / lead transfer / price / sold status / none>
- What approval would allow: <specific next action>
- Evidence provided for approval: <sample, count, cost, compliance notes>

## Next Safe Action

Recommended next safe action: <one action that does not violate permission matrix>

If approval is needed, ask for one specific approval. Do not bundle unrelated approvals.

## Stop Report

Use this if the run cannot continue safely:

Stopped because: <condition>
Goal affected: <pipeline goal>
Evidence: <source URLs, logs, table rows, costs, screenshots, or drafts>
Safe next options: <2-3 choices>
Recommended option: <one choice>
Approval/input needed: <specific approval or missing value>
