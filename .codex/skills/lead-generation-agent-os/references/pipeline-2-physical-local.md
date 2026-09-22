# Pipeline 2: Physical / Local Leads

Use when buyer need is visible from public property, imagery, business listing, permit, or listing-photo data.

## Goal

Find people or businesses that already appear to need a local trade, show the fix on their own property, and prepare an approval-gated outreach batch.

Flow: trade + city -> visible signal -> one qualifier -> candidate table -> reference images -> render draft -> property page -> outreach batch -> response log.

## Suitable Trades

Prefer trades where demand can be detected visually or from public records: roofing, solar, landscaping, pools, awnings, fencing, driveways, signage, exterior painting, and window replacement. Reject or mark review if the need is not visible from public data.

## Steps

1. Trade signal definition: identify what the property or business looks like when it needs the trade. Choose one public source and one qualifier only. Define what the render must show.
2. Candidate list: pull addresses or businesses in the selected area from the chosen source. Check imagery/listing photo availability and age before paid pulls when possible. Drop imagery older than three years unless approved.
3. Reference image collection: pull the minimum reference frames needed for a faithful edit. Preserve source URLs, image dates, and cost.
4. Render preparation: create an image-edit prompt that changes only the trade-relevant feature. Do not invent property features outside the reference images.
5. Property page draft: create one page per property with render at top, address, source context, and a quote-request form. Keep pages unpublished unless approved.
6. Outreach batch draft: choose channel from available contact data. Address only means postcard, email means email draft, phone means SMS draft if compliant and approved. Validate every address, email, and number.
7. Response capture: log QR scans, page visits, form fills, replies, timestamps, address, owner/contact, channel, and render URL.

## Checks

- One qualifier only.
- Imagery age is recorded.
- Borderline candidates are not auto-included.
- Render changes only the intended fix.
- Contact data is validated before batch review.
- Costs are reported before paid API or postcard send.

## Outputs

- trade-signal-definition
- candidate-table
- reference-image-log
- render-review-batch
- property-page-drafts
- outreach-batch-draft
- response-log

## Human Approval Gates

- Pulling paid imagery beyond the approved budget.
- Approving renders.
- Publishing pages.
- Sending postcards, emails, or SMS.
- Follow-up sequences.
