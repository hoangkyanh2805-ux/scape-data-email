# Pipeline 3: Lead Resale

Use after Pipeline 2 has captured local leads and the user wants to sell those leads to local service businesses.

## Goal

Package verified local leads for relevant businesses without overpromising, duplicating sold leads, or contacting owners without approval.

Flow: captured leads -> matching businesses -> sample PDF -> outreach draft -> owner reply -> pricing -> dashboard delivery.

## Steps

1. Business list: search an approved source for the trade and city. Prefer owner-led local companies. Filter for 15 to 200 reviews unless specified otherwise. Exclude obvious franchises and companies outside the service area.
2. Lead matching: match each company with the three closest unsold leads inside its coverage area. Skip companies with fewer than three nearby leads. Never sell the same exclusive lead to multiple companies.
3. Sample asset: build a one-page PDF or page showing three sample leads with street/area, render, requested quote time or response summary, and timestamp. Redact sensitive details unless approved.
4. Outreach draft: write a plain message that three people near them asked for a quote this week. Link to the sample asset or prepare QR/postcard. Draft at least one follow-up for one week later. Stop before sending.
5. Pricing recommendation: month 1 can be per-lead test pricing; month 2+ can be retainer for exclusive zip codes or territory. Keep pricing as draft until approved.
6. Delivery dashboard: track lead address, owner/contact where allowed, render, form fill, timestamp, buyer business, exclusivity status, sold date, price, and outcome.

## Checks

- Coverage area evidence supports the match.
- Lead is not already sold exclusively.
- Sample asset does not expose sensitive data without approval.
- Pricing and exclusivity terms are explicit.
- First owner conversation remains human-led unless explicitly approved.

## Outputs

- business-buyer-table
- lead-match-table
- sample-lead-pdf-draft
- business-outreach-draft
- pricing-recommendation
- delivery-dashboard

## Human Approval Gates

- Sending first outreach.
- Sharing full lead contact details.
- Setting price or exclusivity.
- Taking payment or changing sold status.
