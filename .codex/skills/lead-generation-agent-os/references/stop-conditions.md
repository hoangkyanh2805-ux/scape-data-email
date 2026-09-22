# Stop Conditions

Stop and report whenever one of these is true.

## Input Stops

- Product, trade, city, offer, checkout URL, or target area is missing and required for the selected pipeline.
- The user has not provided a budget ceiling for paid ads, paid APIs, generated media, or postcards.
- The selected trade has no visible demand signal in public data.

## Data Quality Stops

- Imagery is older than three years and no fresher source is available.
- The qualifier is borderline or cannot be verified from the selected source.
- Two sources disagree in a way that changes whether someone is a lead.
- Community/source activity cannot be verified.
- Contact data fails validation.

## Tool / Cost Stops

- A tool or API fails three times.
- A quota, rate limit, or budget threshold is reached.
- The agent cannot verify that a paid operation succeeded.

## Risk Stops

- Next action would contact a real person.
- Next action would spend money or change ad budget.
- Next action would publish externally.
- Next action would share personal/contact information.
- Next action would mark a lead sold, exclusive, or transferred.
- Creative contains unsupported claims, fake testimonials, or guaranteed outcomes.

## Escalation Format

Stopped because: <condition>
Goal affected: <pipeline goal>
Evidence: <source URLs, logs, table rows, cost, screenshots, or drafts>
Safe next options: <2-3 choices>
Recommended option: <one choice>
Approval/input needed: <specific approval or missing value>
