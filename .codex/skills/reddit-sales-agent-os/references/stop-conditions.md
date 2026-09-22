# Stop Conditions

Stop and report using the run output template whenever one of these conditions appears.

## Input Stops

- No subreddit list and no audience/product description to infer subreddits from.
- Product boundaries are unclear but the user asks for selling-mode replies.
- Price, product URL, or delivery method is needed for a landing page or product file and missing.
- Dashboard or storage destination is required and missing.

## Reddit And Rate-Limit Stops

- RSS source returns repeated 429 or rate-limit signals.
- Feed format changes and fields cannot be verified.
- A subreddit becomes inaccessible or private.
- Pull cadence would exceed the configured rate limit.

## Moderation And Account Stops

- Subreddit rules are unclear and the draft may be promotional.
- Similar content was removed and the profile has not been updated.
- Account health notes show warning/removal risk for the target subreddit.
- The next step requires logging in, posting, commenting, voting, or DMing.

## Quality Stops

- Subreddit profile evidence is too thin to match tone.
- Match score is below 4 but the next step would queue a reply as if it were high intent.
- Thread is older than one month, already answered well, or replying would obviously be spam.
- Product file lacks what the product does not do or forbidden claims.

## Risk Stops

- Niche appears medical, legal, financial, safety-critical, or credential-required.
- Draft includes unsupported claims, fake proof, or guaranteed outcomes.
- Next action would publish a page, enable checkout, spend money, or send a notification to an unapproved channel.

## Escalation Format

Stopped because: <condition>
Goal affected: <mode goal>
Evidence: <links, feed logs, profile notes, draft, or table rows>
Safe next options: <2-3 choices>
Recommended option: <one choice>
Approval/input needed: <specific request>
