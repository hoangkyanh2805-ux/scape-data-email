"""Prepare exact YouTube commenter email-probe input from filtered leads.

This script does not call Apify. It reads a local filtered_leads.csv file,
keeps only retained retail customer commenters, rejects seller/operator rows,
and writes the approval input JSON consumed by run_youtube_retail_commenter_email.py.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any

DEFAULT_SOURCE = "data/forex-social-intent/runs/20260922-190136/filtered_leads.csv"
DEFAULT_OUTPUT = "docs/apify-youtube-retail-commenter-exact-email-input.json"
SELLER_STATUSES = {
    "seller_affiliate_creator_reject",
    "spam_scam_reject",
}


def truthy(value: str) -> bool:
    return str(value).strip().lower() in {"1", "true", "yes", "y"}


def row_is_retained_customer(row: dict[str, str]) -> bool:
    status = row.get("seller_filter_status", "").strip().lower()
    if status in SELLER_STATUSES:
        return False
    if not truthy(row.get("retained_for_enrichment", "")):
        return False
    if not row.get("channel_or_profile_url", "").startswith("https://www.youtube.com/"):
        return False
    evidence = row.get("evidence") or row.get("engagement_text") or ""
    return bool(evidence.strip())


def build_packet(rows: list[dict[str, str]], max_profiles: int, source_run: str = DEFAULT_SOURCE) -> dict[str, Any]:
    selected: list[dict[str, str]] = []
    seen_urls: set[str] = set()
    for row in rows:
        if not row_is_retained_customer(row):
            continue
        url = row["channel_or_profile_url"].strip()
        if url in seen_urls:
            continue
        seen_urls.add(url)
        selected.append(row)
        if len(selected) >= max_profiles:
            break

    return {
        "approval_id": "apify-youtube-retail-commenter-exact-email-002",
        "budget_ceiling_usd": 0.05,
        "source_run": source_run,
        "actor_candidate": "crawlerbros/youtube-email-scraper",
        "do_not_run_without_approval": True,
        "input": {
            "channelUrls": [row["channel_or_profile_url"].strip() for row in selected],
            "followExternalProfiles": True,
            "maxExternalPerChannel": 2,
            "autoProxyFallback": True,
        },
        "qualified_handles": [
            {
                "handle": row.get("user_handle", ""),
                "evidence": row.get("evidence") or row.get("engagement_text", ""),
                "offer_bucket": row.get("offer_bucket", ""),
            }
            for row in selected
        ],
        "rules": [
            "public data only",
            "no login/cookies/private contact panels",
            "no guessed/generated emails",
            "no validation at scale",
            "no outreach/export",
            "every retained email needs email_source_url and email_source_field",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default=DEFAULT_SOURCE)
    parser.add_argument("--output", default=DEFAULT_OUTPUT)
    parser.add_argument("--max-profiles", type=int, default=10)
    args = parser.parse_args()

    source = Path(args.source)
    with source.open(newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))

    packet = build_packet(rows, args.max_profiles, str(source))
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(packet, indent=2, ensure_ascii=False), encoding="utf-8")

    summary = {
        "source": str(source),
        "output": str(output),
        "selected_profiles": len(packet["input"]["channelUrls"]),
        "handles": [row["handle"] for row in packet["qualified_handles"]],
    }
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())