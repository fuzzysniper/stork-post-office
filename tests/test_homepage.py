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

    def test_featured_research_is_above_token_material(self):
        self.assertIn('id="scout"', HTML)
        self.assertIn('id="token"', HTML)
        self.assertIn('id="post-office"', HTML)
        self.assertLess(HTML.index('id="scout"'), HTML.index('id="token"'))
        self.assertLess(HTML.index('OPEN SCOUT INTELLIGENCE'), HTML.index('POST OFFICE ROUTING MAP'))
        self.assertIn('aria-label="Post Office"', HTML)
        self.assertIn('href="#scout"', HTML)
        self.assertIn('href="#token"', HTML)

    def test_no_unverified_economic_linkage(self):
        self.assertIn('Free to explore. No STORK ownership, wallet connection or payment required.', HTML)
        self.assertNotIn('SCOUT revenue flows to token holders', HTML)
        self.assertIn('Historical routing concepts', HTML)
