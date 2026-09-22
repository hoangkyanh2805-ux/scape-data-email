# Product Selling Mode

Use when the user already has a product and wants Reddit to surface helpful reply and post opportunities.

## Goal

Find threads where people describe the problem the product solves, draft useful replies and posts in the subreddit voice, and queue them for human posting.

Flow: product file -> subreddit profiles -> match detection -> reply queue -> post queue -> human posting -> sent log.

## Product File

Create and maintain a product file before drafting content. It must include:

- Product name, price, link, and delivery method.
- Exact problem solved in buyer language.
- Who it is for.
- Who it is not for.
- Specific things it covers.
- What it does not do.
- Honest answers to objections.
- Three real subreddit quotes describing the problem.
- Claims that are allowed and claims that are forbidden.

Read the product file and subreddit profile before writing any post, reply, or message draft.

## Finding Threads

Search collected history and fresh pulls for posts/comments where someone describes the solved problem, even if they use community-specific phrasing.

For each match, record: link, subreddit, author, text excerpt, timestamp, directness score 1 to 5, urgency, whether already answered well, spam risk, and recommended action.

Ignore anything older than one month, already answered well, obviously spammy to reply to, or outside the product boundaries.

## Reply Drafting

For each new match scoring 4 or above, draft a reply and queue it.

Reply rules:

- Match the target subreddit tone profile.
- Answer the actual question properly.
- Use the product file for substance, not for promotion.
- Do not mention the product.
- Do not include links unless explicitly approved and subreddit rules allow it.
- Match the length of other good replies in the thread.
- Avoid marketing language, hype, exclamation marks, and formulaic openings.
- Put the reply on the dashboard with direct permalink and copy-ready text.
- Sort by time sensitivity.
- Log skipped matches and why.

## Post Drafting

Every morning, draft up to five helpful posts across target subreddits.

Post rules:

- Read the subreddit profile first.
- Give away the method with nothing held back.
- Do not mention the product or link by default.
- End with an offer to answer questions.
- Include removal risk and survival edits based on subreddit rules.
- Include submit link and best posting window.

The operator chooses which posts to publish. The agent never posts.

## DM Boundary

The agent cannot read Reddit DMs from public feeds and should not automate DMs. The human handles DMs manually. Useful DM insights can be pasted back into the subreddit profile as source notes.

## Outputs

- product-file
- thread-match-queue
- reply-draft-queue
- post-draft-queue
- skipped-opportunity-log
- sent-log
- account-health-notes

## Human Approval Gates

- Any Reddit post, comment, or DM.
- Any product mention or link.
- Any claim with legal, health, finance, income, or guaranteed-outcome risk.
- Any subreddit where rules are unclear.
