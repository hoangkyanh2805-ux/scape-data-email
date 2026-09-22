# Output Schemas

Use these schemas for markdown tables, CSV, spreadsheets, databases, or dashboard backing stores.

## Global Fields

Add these fields when practical: id, run_id, subreddit, source_url, permalink, source_timestamp, fetched_at, confidence, status, review_reason, human_action_required, created_at, updated_at, notes.

Status values: draft, queued, review, skipped, sent_by_human, stale, blocked, archived.

## Subreddit Source Map

Fields: subreddit, url, rss_url, member_count, activity_level, buyer_relevance, self_promo_tolerance, link_tolerance, moderation_strictness, access_status, skip_reason, notes.

## Reddit Feed History

Fields: item_id, item_type, subreddit, title, author, body_text, parent_post, permalink, source_timestamp, fetched_at, score_or_engagement_if_available, duplicate_of, raw_source_path.

Item type values: post, comment.

## Subreddit Profile Index

Fields: subreddit, profile_path, last_updated, evidence_window, major_changes, rule_risk, tone_summary, language_summary, next_review_date.

## Niche Candidate Table

Fields: niche_id, problem, who_has_it, urgency_reason, current_paid_alternatives, subreddits, reachability, credential_risk, harm_risk, paid_intent, rank, status.

## Repeated Problem Analysis

Fields: problem_id, subreddit, problem_in_user_words, normalized_problem, count, frustration_level, representative_quotes, source_links, tried_before, paid_alternatives, build_recommendation, confidence.

## Product File

Fields: product_name, price, product_url, delivery_method, problem_solved_in_buyer_words, for_whom, not_for_whom, covers, does_not_do, objections_and_answers, proof_quotes, allowed_claims, forbidden_claims, last_updated.

## Thread Match Queue

Fields: match_id, subreddit, permalink, author, excerpt, source_timestamp, directness_score, urgency, already_answered_well, spam_risk, recommended_action, status, skip_reason.

Directness score: 1 weak relevance, 5 direct solution-seeking fit.

## Reply Draft Queue

Fields: draft_id, match_id, subreddit, permalink, draft_text, tone_basis, product_mention, link_included, risk_notes, urgency_rank, human_action_required, status.

Default product_mention and link_included should be no.

## Post Draft Queue

Fields: post_id, subreddit, submit_url, draft_title, draft_body, tone_basis, best_posting_window, removal_risk, survival_edits, human_action_required, status.

## Sent Log

Fields: sent_id, draft_id, subreddit, permalink_or_submit_url, human_account, sent_at, result, removal_status, follow_up_needed, notes.

## Account Health Notes

Fields: account_label, subreddit, event_type, event_time, evidence, severity, recommended_change, status.

Event types: removal, warning, rule_change, low_response, duplicate_risk, posting_window_shift.

## Daily Summary

Fields: date, pull_count, queued_replies, queued_posts, profile_changes, skipped_items, stale_items, account_health_events, human_actions_needed, dashboard_url.
