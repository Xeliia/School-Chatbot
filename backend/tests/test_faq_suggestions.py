import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from fastapi.testclient import TestClient

from config import get_settings
from faq_suggestions import FAQ_POOL, select_suggestions
import main as backend_main


class SuggestionSelectorTests(unittest.TestCase):
    def test_returns_limited_unique_items(self):
        result = select_suggestions(exclude_ids=None, limit=4, rng_seed=1)
        self.assertLessEqual(len(result), 4)
        self.assertGreaterEqual(len(result), 3)
        ids = [item["id"] for item in result]
        self.assertEqual(len(ids), len(set(ids)))

    def test_excludes_immediate_ids(self):
        excluded = ["general-location", "academic-strands"]
        result = select_suggestions(exclude_ids=excluded, limit=4, rng_seed=2)
        ids = {item["id"] for item in result}
        self.assertFalse(ids.intersection(excluded))

    def test_previously_excluded_can_reappear_next_turn(self):
        first = select_suggestions(exclude_ids=["general-location"], limit=4, rng_seed=3)
        first_ids = {item["id"] for item in first}
        self.assertNotIn("general-location", first_ids)

        seen_in_follow_up = False
        for seed in range(1, 30):
            second = select_suggestions(exclude_ids=[], limit=4, rng_seed=seed)
            second_ids = {item["id"] for item in second}
            if "general-location" in second_ids:
                seen_in_follow_up = True
                break

        self.assertTrue(seen_in_follow_up)

    def test_pool_size_matches_expectation(self):
        self.assertGreaterEqual(len(FAQ_POOL), 15)
        self.assertLessEqual(len(FAQ_POOL), 20)


class SuggestionEndpointTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(backend_main.app)
        cls.api_key = get_settings().api_key

    def test_requires_authorization(self):
        response = self.client.get("/suggestions")
        self.assertEqual(response.status_code, 401)

    def test_returns_schema_with_auth(self):
        response = self.client.get(
            "/suggestions",
            headers={"Authorization": f"Bearer {self.api_key}"},
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("suggestions", data)
        suggestions = data["suggestions"]
        self.assertGreaterEqual(len(suggestions), 3)
        self.assertLessEqual(len(suggestions), 4)
        for item in suggestions:
            self.assertIn("id", item)
            self.assertIn("question", item)
            self.assertIn("category", item)

    def test_exclusion_ids_are_not_returned(self):
        excluded = "general-location,academic-strands"
        response = self.client.get(
            f"/suggestions?exclude_ids={excluded}&limit=4",
            headers={"Authorization": f"Bearer {self.api_key}"},
        )
        self.assertEqual(response.status_code, 200)
        ids = {item["id"] for item in response.json()["suggestions"]}
        self.assertNotIn("general-location", ids)
        self.assertNotIn("academic-strands", ids)


if __name__ == "__main__":
    unittest.main()
