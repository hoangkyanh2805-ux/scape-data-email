"""
Mock demonstration for the scape-data public social engagement loop.

Usage:
    python test_orchestrator.py
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from apify_integration import MockApifyClient
from orchestrator import SelfImprovingOrchestrator


def main():
    """Run a local mock improvement loop without API keys or live scraping."""

    print("\n" + "=" * 70)
    print("SCAPE-DATA MOCK SOCIAL ENGAGEMENT LOOP")
    print("=" * 70)
    print("\nMockApifyClient only. No live Apify run, outreach, or export.\n")

    mock_client = MockApifyClient(failure_rate=0.15)

    initial_config = {
        "platform": "tiktok",
        "query": "xauusd forex beginner",
        "search_query": "xauusd forex beginner public comments",
        "max_posts": 5,
        "max_comments_per_post": 25,
        "batch_size": 25,
        "public_data_only": True,
        "login_required": False,
        "include_private_sources": False,
        "outreach_enabled": False,
        "external_export_enabled": False,
    }

    print("Initial configuration:")
    print(json.dumps(initial_config, indent=2))
    print()

    orchestrator = SelfImprovingOrchestrator(
        apify_client=mock_client,
        initial_config=initial_config,
        actor_name="mock_public_social_engagement_actor",
        max_iterations=3,
        conversation_pointer="data/forex-social-intent/runs/mock-demo/batch_report.md",
    )

    print("\n" + "=" * 70)
    print("STARTING MOCK LOOP")
    print("=" * 70 + "\n")

    result = orchestrator.run_improvement_loop()

    print("\n" + "=" * 70)
    print("FINAL RESULTS")
    print("=" * 70)

    print(f"\nStatus: {result['status']}")
    print(f"Total iterations: {result['total_runs']}")
    print("\nFinal configuration:")
    print(json.dumps(result['final_config'], indent=2))

    print("\nFinal metrics:")
    for metric, value in result["final_metrics"].items():
        if isinstance(value, float):
            suffix = ".2%" if metric.endswith("rate") else ".2f"
            print(f"  {metric}: {value:{suffix}}")
        else:
            print(f"  {metric}: {value}")

    print(f"\nConvergence reason: {result['convergence_reason']}")

    print("\nRun history:")
    print(f"{'Iter':<5} {'Rows':<7} {'Dedup':<8} {'Valid':<8} {'Errors':<7} {'Status':<12}")
    print("-" * 57)

    for run in result["run_history"]:
        status = "Success" if not run.get("error") else f"Error: {run['error_type']}"
        print(
            f"{run['iteration']:<5} "
            f"{run['lead_count']:<7} "
            f"{run['deduplication_rate']:<7.1%} "
            f"{run['lead_validation_rate']:<7.1%} "
            f"{run['error_count']:<7} "
            f"{status:<12}"
        )

    print("\nNext safe steps:")
    print("1. Review the mock metrics and generated fix proposals.")
    print("2. Draft an approval packet for one tiny public-data Apify actor test.")
    print("3. Stop before paid scale-up, contact export, Telegram, CRM, or outreach.")
    print()


if __name__ == "__main__":
    main()


