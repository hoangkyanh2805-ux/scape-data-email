# YouTube Comments Discovery Workflow

## Purpose

Find customer demand first, then enrich contacts. This workflow exists because keyword-to-email scraping produced seller, IB, affiliate, and creator emails instead of customer leads.

## Source Query Families

Use offer-fit customer language, not seller language.

### Free Signal / Broker / Prop-Firm

```text
need forex signal
which broker for forex
xauusd signal help
forex funded challenge failed
prop firm challenge help
how to pass funded challenge
```

### Beginner / Mini-Course / Edu Course

```text
how do I start forex
forex beginner need help
xauusd beginner strategy
ict trading beginner confused
forex risk management help
```

### VIP / Copytrading / Coaching

```text
need forex mentor
forex signals worth it
copy trading forex help
want someone to guide me trading
forex course review help
```

### AI Sales Agent / Operator Fit

Use only when searching for operators, not retail learners.

```text
telegram signal group leads
forex signal group automation
trading course telegram bot
automate trading community sales
```

## Discovery Flow

1. `source-finder` proposes 3-5 YouTube search queries mapped to offer buckets.
2. `approval-gate-reporter` prepares exact actor input and budget ceiling.
3. After approval, `post-collector` finds public videos/channels.
4. `engagement-collector` collects public comments only.
5. `buyer-intent-scorer` scores each comment with an evidence phrase.
6. `seller-spam-filter` marks seller/affiliate/creator rows as rejected or review, preserving operator rows only if AI Sales Agent fit is explicit.
7. `lead-normalizer` writes local tables.
8. `approval-gate-reporter` reports yield, cost, risks, and next approval.

## Do Not Do

- Do not run an email scraper directly from broad keywords.
- Do not collect video creator emails as customer leads.
- Do not enrich every commenter. Enrich only retained high/medium rows.
- Do not use channel emails unless the channel belongs to the retained commenter/source and source evidence is preserved.

## Required Review Labels

```text
qualified_customer_candidate
operator_ai_sales_agent_fit
seller_affiliate_creator_reject
spam_scam_reject
not_enough_evidence_review
```

## Email Enrichment Gate

Only rows with these labels can move to enrichment:

```text
qualified_customer_candidate
operator_ai_sales_agent_fit
not_enough_evidence_review
```

`not_enough_evidence_review` should be sampled sparingly, not bulk-enriched.
