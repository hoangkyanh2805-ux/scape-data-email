import importlib.util
import subprocess
import sys
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("run_youtube_retail_commenter_email.py")
spec = importlib.util.spec_from_file_location("runner", MODULE_PATH)
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)


class YoutubeRetailCommenterEmailTests(unittest.TestCase):
    def test_normalize_rows_maps_evidence_by_channel_order(self):
        items = [
            {
                "channelUrl": "https://www.youtube.com/channel/UC1/about",
                "channelHandle": "@fallback",
                "emails": ["lead@example.com"],
                "sources": [
                    {
                        "email": "lead@example.com",
                        "sourceUrl": "https://www.youtube.com/channel/UC1/about",
                        "sourceType": "channel_description",
                    }
                ],
            }
        ]
        qualified = [
            {
                "handle": "@customer",
                "evidence": "Brother can you be my mentor, am starting this forex journey",
                "offer_bucket": "coaching_mastermind",
            }
        ]

        accepted, rejected = runner.normalize_rows(
            items,
            qualified,
            ["https://www.youtube.com/channel/UC1"],
        )

        self.assertEqual(len(accepted), 1)
        self.assertEqual(rejected, [])
        self.assertEqual(accepted[0]["source_handle"], "@customer")
        self.assertTrue(accepted[0]["customer_intent_evidence"].startswith("Brother can you"))
        self.assertEqual(accepted[0]["email_source_field"], "channel_description")

    def test_normalize_rows_rejects_seller_language(self):
        items = [
            {
                "channelUrl": "https://www.youtube.com/channel/UC2/about",
                "channelHandle": "@seller",
                "channelDescription": "Join my VIP signal provider group",
                "emails": ["seller@example.com"],
                "sources": [
                    {
                        "email": "seller@example.com",
                        "sourceUrl": "https://www.youtube.com/channel/UC2/about",
                        "sourceType": "channel_description",
                    }
                ],
            }
        ]

        accepted, rejected = runner.normalize_rows(items, [], [])

        self.assertEqual(accepted, [])
        self.assertEqual(len(rejected), 1)
        self.assertEqual(rejected[0]["status"], "rejected_not_customer_lead")
        self.assertIn("seller", rejected[0]["review_reason"])

    def test_reject_signal_uses_word_boundaries(self):
        self.assertTrue(runner.has_reject_signal("I am an IB for this broker"))
        self.assertFalse(runner.has_reject_signal("New subscriber learning forex"))

    def test_prepare_packet_uses_requested_source_path(self):
        prep_path = Path(__file__).with_name("prepare_youtube_retail_commenter_email_input.py")
        prep_spec = importlib.util.spec_from_file_location("prep", prep_path)
        prep = importlib.util.module_from_spec(prep_spec)
        prep_spec.loader.exec_module(prep)

        packet = prep.build_packet([], 10, "custom/filtered_leads.csv")

        self.assertEqual(packet["source_run"], "custom/filtered_leads.csv")

    def test_runner_refuses_without_exact_approval(self):
        proc = subprocess.run(
            [sys.executable, str(MODULE_PATH)],
            cwd=MODULE_PATH.parents[1],
            text=True,
            capture_output=True,
        )

        self.assertNotEqual(proc.returncode, 0)
        self.assertTrue("Refusing to run" in proc.stderr or "Refusing to run" in proc.stdout)


if __name__ == "__main__":
    unittest.main()