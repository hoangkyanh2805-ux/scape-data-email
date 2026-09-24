# Offer-Fit Lead Filter

This file captures the user-provided offer context from the attached offer ladder image. It is source context for filtering leads, not an instruction to send outreach, launch funnels, or change safety gates.

## Offer Context

Primary project goal:

```text
public social engagement -> offer-fit intent score -> seller/spam filter -> public email enrichment -> local candidate table
```

The target is not only people who want to "learn Forex". The target is any public social account showing demand that matches one of the offer ladder paths below.

## Offer Ladder Buckets

### 1. Free Attraction

- Free signal channel.
- Broker partnership / broker-funded or exchange/referral route.

Lead signals:

- asks for signal, entry, TP/SL, gold/XAUUSD direction, daily setup;
- asks which broker, funded account, prop firm, deposit, spread, withdrawal, account setup;
- wants a free community, watchlist, alerts, or basic guidance.

### 2. AI Sales Agent / Telegram Automation

- AI sales agent on Telegram.
- Follow-up automation, lead reply handling, objection handling, booking or routing.

Lead signals:

- owns or promotes a signal group, trading channel, paid community, course, or mentorship;
- complains about manual DM replies, low conversion, missed leads, follow-up, onboarding, support;
- asks how to automate Telegram/WhatsApp/DM sales, qualification, or customer handling.

### 3. Tripwire / Low-Ticket

- Mini-course around entry/checklist/beginner trading.
- Low-cost access for people unsure about VIP or full course.

Lead signals:

- "how do I start", "beginner", "teach me", "what app", "how much capital", "where to learn";
- confused by strategy, ICT/SMC/XAUUSD concepts, risk management, TradingView, prop rules;
- wants simple checklist, step-by-step, template, beginner roadmap.

### 4. Core Offers

- VIP signal / monthly continuity.
- Edu course / full price or downsell.

Lead signals:

- asks for paid signal, reliable entries, daily calls, mentorship, structured course;
- has repeated trading pain, losses, failed self-learning, failed signals, or wants accountability;
- asks for results, refund, guarantee, trial, proof, community, or support.

### 5. Cross-Sell / Ascension

- VIP signal customer to edu course.
- Course learner to VIP/copytrading.

Lead signals:

- already uses signals but does not understand why entries work;
- already studies trading but wants done-for-you execution, copytrading, or a managed path;
- asks for both learning and daily trade help.

### 6. Backend / High-Ticket

- Copytrading / done-for-you.
- Mastermind or coaching.
- Tools such as calculators, scanners, journals, simulators, dashboards.
- Limited higher tiers.

Lead signals:

- wants someone to trade for them, copy trades, account management, or hands-off execution;
- asks for one-on-one coaching, private mentorship, faster path, accountability, direct review;
- wants trading tools, calculators, scanners, journaling, backtesting, or risk dashboards;
- has capital, business, audience, or trading operation but lacks system/process.

## Negative / Review Signals

Reject or review before enrichment:

- obvious brokers, IB spam, fake managers, recovery scams, giveaway spam;
- accounts selling the same offer unless they fit the AI Sales Agent / automation bucket;
- comments that are only emoji, generic hype, or unrelated;
- emails not tied to a public source URL and field;
- inferred, generated, or guessed emails.

## Scoring Shape

High intent:

- clear request matching any offer bucket;
- pain plus willingness to act/pay;
- operator/seller with clear automation pain for the AI Sales Agent bucket.

Medium intent:

- relevant question or repeated interest, but no urgency/payment clue;
- profile context supports the offer bucket.

Low intent:

- generic praise, vague curiosity, no offer fit.

Reject:

- spam, scam, unrelated, seller pitch not relevant to automation offer.

## Required Output Fields

Add these fields where practical:

```text
offer_bucket
offer_fit_score
offer_fit_reason
evidence_phrase
seller_or_operator_status
public_email
email_source_url
email_source_field
approval_status
```

Do not mark any row approved for outreach automatically.
