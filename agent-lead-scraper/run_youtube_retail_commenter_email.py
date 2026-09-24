"""
Run an approval-gated YouTube retail commenter public email probe.

This script is intentionally narrow:
- exact channel URLs only;
- public data only;
- no outreach/export;
- no guessed emails;
- budget guard before and during polling.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import time
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path
from typing import Any


ACTOR_ID = "crawlerbros/youtube-email-scraper"
APPROVAL_TEXT = "approve run youtube retail commenter exact email budget 0.05"
REJECT_PATTERNS = (
    r"\bib\b",
    r"\baffiliate\b",
    r"\bbroker\s+partner\b",
    r"\bsignal\s+provider\b",
    r"\bvip\s+signals?\b",
    r"\bmanaged\s+account\b",
    r"\baccount\s+management\b",
    r"\bcopy\s+my\s+trades\b",
    r"\bdm\s+me\b",
    r"\bwhatsapp\s+me\b",
    r"\bguaranteed\s+profit\b",
    r"\bcourse\s+seller\b",
    r"\bmentor\s+slots?\b",
)


def has_reject_signal(text: str) -> bool:
    return any(re.search(pattern, text, flags=re.IGNORECASE) for pattern in REJECT_PATTERNS)


def api_request(method: str, url: str, token: str, body: Any | None = None) -> Any:
    data = None
    headers = {"Authorization": f"Bearer {token}"}
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Apify API error {exc.code}: {detail}") from exc


def write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False), encoding="utf-8")


def canonical_url(url: str) -> str:
    return url.rstrip("/").removesuffix("/about")


def normalize_rows(
    items: list[dict[str, Any]],
    qualified: list[dict[str, Any]],
    channel_urls: list[str],
) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    evidence_by_url: dict[str, dict[str, Any]] = {}
    for idx, channel_url in enumerate(channel_urls):
        if idx < len(qualified):
            evidence_by_url[canonical_url(channel_url)] = qualified[idx]
    for q in qualified:
        for url in q.get("channel_urls", []):
            evidence_by_url[canonical_url(str(url))] = q
    accepted: list[dict[str, str]] = []
    rejected: list[dict[str, str]] = []

    for item in items:
        channel_url = str(item.get("channelUrl") or item.get("inputChannelUrl") or "")
        evidence = evidence_by_url.get(canonical_url(channel_url), {})
        emails = item.get("emails") or []
        sources = item.get("sources") or []
        if not emails:
            rejected.append(
                {
                    "email": "",
                    "email_source_url": channel_url,
                    "email_source_field": "none",
                    "source_handle": str(evidence.get("handle", item.get("channelHandle", ""))),
                    "source_platform": "youtube",
                    "customer_intent_evidence": str(evidence.get("evidence", "")),
                    "offer_bucket": str(evidence.get("offer_bucket", "")),
                    "seller_or_operator_status": "retail_customer_candidate",
                    "status": "rejected_no_public_email",
                    "review_reason": "no email in public profile/about/external public bio",
                }
            )
            continue

        for email in emails:
            source = next((s for s in sources if s.get("email") == email), {})
            source_url = str(source.get("sourceUrl") or channel_url)
            source_type = str(source.get("sourceType") or "unknown")
            blob = " ".join(
                str(item.get(k, "")) for k in ("channelName", "channelDescription", "channelHandle")
            ).lower()
            reason = ""
            if has_reject_signal(blob):
                reason = "seller_ib_affiliate_or_creator_signal"
            if not source_url or source_type == "unknown":
                reason = (reason + "; " if reason else "") + "missing_source_attribution"

            row = {
                "email": str(email),
                "email_source_url": source_url,
                "email_source_field": source_type,
                "source_handle": str(evidence.get("handle", item.get("channelHandle", ""))),
                "source_platform": "youtube",
                "customer_intent_evidence": str(evidence.get("evidence", "")),
                "offer_bucket": str(evidence.get("offer_bucket", "")),
                "seller_or_operator_status": "retail_customer_candidate",
                "status": "review_candidate" if not reason else "rejected_not_customer_lead",
                "review_reason": reason,
            }
            (accepted if not reason else rejected).append(row)

    return accepted, rejected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="docs/apify-youtube-retail-commenter-exact-email-input.json")
    parser.add_argument("--budget", type=float, default=0.05)
    parser.add_argument("--approval", default="")
    parser.add_argument("--approved", action="store_true")
    parser.add_argument("--out-dir", default="")
    args = parser.parse_args()

    if not args.approved or args.approval != APPROVAL_TEXT:
        raise SystemExit(f"Refusing to run. Pass --approved --approval \"{APPROVAL_TEXT}\"")

    token = os.getenv("APIFY_TOKEN") or os.getenv("APIFY_API_TOKEN")
    if not token:
        raise SystemExit("Missing APIFY_TOKEN or APIFY_API_TOKEN")

    input_path = Path(args.input)
    packet = json.loads(input_path.read_text(encoding="utf-8"))
    run_input = packet["input"]
    qualified = packet.get("qualified_handles", [])

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    out_dir = Path(args.out_dir or f"data/forex-social-intent/runs/{timestamp}-retail-commenter-email-exact")
    out_dir.mkdir(parents=True, exist_ok=True)
    write_json(out_dir / "actor_input.json", run_input)

    run_url = f"https://api.apify.com/v2/acts/{ACTOR_ID}/runs?timeout=120&memory=4096"
    run = api_request("POST", run_url, token, run_input)["data"]
    write_json(out_dir / "run_started.json", run)
    run_id = run["id"]

    final = run
    for _ in range(60):
        time.sleep(5)
        final = api_request("GET", f"https://api.apify.com/v2/actor-runs/{run_id}", token)["data"]
        write_json(out_dir / "run_status.json", final)
        cost = float(final.get("usageTotalUsd") or 0)
        status = final.get("status")
        if cost >= args.budget and status in {"READY", "RUNNING"}:
            api_request("POST", f"https://api.apify.com/v2/actor-runs/{run_id}/abort", token)
            break
        if status in {"SUCCEEDED", "FAILED", "ABORTED", "TIMED-OUT"}:
            break

    final = api_request("GET", f"https://api.apify.com/v2/actor-runs/{run_id}", token)["data"]
    write_json(out_dir / "run_final.json", final)

    dataset_id = final.get("defaultDatasetId")
    items: list[dict[str, Any]] = []
    if dataset_id:
        items = api_request(
            "GET",
            f"https://api.apify.com/v2/datasets/{dataset_id}/items?clean=true&format=json",
            token,
        )
    write_json(out_dir / "raw_items.json", items)

    accepted, rejected = normalize_rows(items, qualified, run_input.get("channelUrls", []))
    fieldnames = [
        "email",
        "email_source_url",
        "email_source_field",
        "source_handle",
        "source_platform",
        "customer_intent_evidence",
        "offer_bucket",
        "seller_or_operator_status",
        "status",
        "review_reason",
    ]
    for filename, rows in (("lead_candidates.csv", accepted), ("rejected_candidates.csv", rejected)):
        with (out_dir / filename).open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(rows)

    summary = {
        "actor": ACTOR_ID,
        "run_id": run_id,
        "status": final.get("status"),
        "cost_usd": final.get("usageTotalUsd"),
        "dataset_id": dataset_id,
        "accepted_customer_emails": len(accepted),
        "rejected_or_no_email": len(rejected),
        "output_dir": str(out_dir),
    }
    write_json(out_dir / "summary.json", summary)
    (out_dir / "batch_report.md").write_text(
        "\n".join(
            [
                "# YouTube Retail Commenter Exact Email Report",
                "",
                f"- Actor: `{ACTOR_ID}`",
                f"- Run ID: `{run_id}`",
                f"- Status: `{summary['status']}`",
                f"- Cost USD: `{summary['cost_usd']}`",
                f"- Accepted customer emails: `{len(accepted)}`",
                f"- Rejected/no-public-email rows: `{len(rejected)}`",
                "",
                "No outreach or external export was performed.",
            ]
        ),
        encoding="utf-8",
    )
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())