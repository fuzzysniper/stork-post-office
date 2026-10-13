"""Static, dependency-free STORK homepage regression checks. Run: python3 -m unittest discover -s tests."""
from pathlib import Path
import unittest

HTML = (Path(__file__).resolve().parents[1] / "index.html").read_text(encoding="utf-8")

class HomepageTests(unittest.TestCase):
    def test_canonical_scout_entry_points(self):
        for url in ["https://scout.storkcoin.xyz", "https://scout.storkcoin.xyz/radar",
                    "https://scout.storkcoin.xyz/brief", "https://scout.storkcoin.xyz/status",
                    "https://scout.storkcoin.xyz/research"]:
            self.assertIn('href="' + url + '"', HTML)
        self.assertNotIn("scout-stonk-intel.vercel.app", HTML)

    def test_clear_relationship_and_open_access(self):
        for phrase in ["FLAGSHIP RESEARCH", "independent, read-only research",
                       "No STORK ownership, wallet connection or payment is required"]:
            self.assertIn(phrase, HTML)

    def test_historical_material_not_presented_as_live(self):
        self.assertIn("Archived September 15, 2026", HTML)
        self.assertIn("ARCHIVED · NOT LIVE", HTML)
        self.assertIn("NOT AN ACTIVE INPUT", HTML)
        self.assertNotIn("DESK OPEN</div>", HTML)

    def test_preserved_ledger_references(self):
        self.assertIn("FKmx3J7b4S3Y6imZLxCTS1KRPQmoZLvJVYYap3FMcjBD", HTML)
        self.assertIn("6VGA2f3Ya9SVPrbcpBpjrgBRMqkQyEgZbmpx5mFNFTyT", HTML)
        self.assertIn("TTs6XeLpe5huUb1HTR9nQVShUpxDEFJJAiSMC5t2cpAytwBByyM9VFcsGY8bdkRy8NWe6TAMVyt85NGMCXZZbk4", HTML)
