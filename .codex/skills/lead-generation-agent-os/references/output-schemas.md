# Output Schemas

Use these schemas as spreadsheet, database, CSV, or markdown table fields. The fields are intentionally explicit so another agent can resume the run without reading the source article.

## Global Fields

Add these fields to every operational table when practical: id, pipeline, run_id, source_url, source_date, confidence, status, review_reason, approval_status, created_at, updated_at, notes.

Recommended status values: draft, review, approved, active, sent, responded, sold, rejected, paused, blocked.

Recommended approval_status values: not_required, needed, requested, approved, denied.

## Community Source Map

Fields: platform, community_name, url, buyer_quality, why_buyers_are_here, common_topics, activity_status, access_status, notes.

Use for Pipeline 1 buyer habitat discovery. Buyer quality should be high, medium, low, or review.

## Voice Of Customer Counts

Fields: phrase_type, exact_phrase, normalized_theme, count, source_urls, date_range, engagement_total, confidence, inference_notes.

Phrase type values: question, complaint, desire, paid_alternative, objection, identity_phrase, outcome_phrase.

## Buyer Profile

Fields: product, price, buyer_segment, demographic_notes, psychographic_notes, tried_before, fears, hidden_wants, excuses_or_beliefs, paid_alternatives, strongest_phrases, source_evidence, confidence.

## Creative Plan

Fields: angle_id, angle, source_theme, source_count, hook, exact_phrase_used, video_concept, still_concept, placement, format, destination_url, claim_risk, compliance_status, approval_status.

## Candidate Table

Fields: trade, city_area, address_or_business, owner_name, buyer_type, contact_data, source_url, imagery_date, qualifier, qualifier_status, reference_images, estimated_cost, review_reason, status.

Qualifier status values: clear, borderline, no, review. Borderline rows cannot enter approved outreach without human approval.

## Reference Image Log

Fields: candidate_id, image_url_or_path, source, captured_or_imagery_date, view_type, cost, usable_for_render, notes.

## Render Review Batch

Fields: candidate_id, render_prompt, input_images, render_url_or_path, changed_feature, render_status, failure_reason, human_review_status, approved_for_outreach.

Render status values: draft, pass, fail, review.

## Property Page Drafts

Fields: candidate_id, draft_page_url_or_path, address, render_url, form_fields, tracking_id, publish_status, approval_status.

## Outreach Batch

Fields: batch_id, candidate_id, channel, recipient, validation_status, render_url, page_url, message_version, sample_copy, approval_status, sent_at, response_status.

Recommended response values: none, open, scan, reply, form_fill, booked, invalid.

## Business Buyer Table

Fields: business_id, business_name, trade, city_area, website, phone, email, address, review_count, franchise_markers, coverage_area_evidence, buyer_quality, status.

## Lead Match Table

Fields: business_id, lead_id, distance_or_area_match, coverage_confidence, sample_asset_url, share_level, match_status, review_reason.

Share level values: redacted, partial, full_after_approval.

## Lead Dashboard

Fields: lead_id, source_batch, address_or_business, owner_contact, requested_time, render_url, captured_at, lead_status, buyer_business, exclusivity, revenue, sold_at, outcome.

Recommended lead status values: warm, qualified, sold, rejected, duplicate, exclusive_hold.

## Daily Report

Fields: date, pipeline, run_id, spend, leads, sales, revenue, cost_per_lead, cost_per_sale, winning_angle_or_channel, blocked_items, review_items, recommended_action, approval_needed.
