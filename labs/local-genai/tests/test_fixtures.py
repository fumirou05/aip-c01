from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


LAB_ROOT = Path(__file__).resolve().parents[1]
CHECK_SETUP_PATH = LAB_ROOT / "scripts/check_setup.py"
SPEC = importlib.util.spec_from_file_location("check_setup", CHECK_SETUP_PATH)
CHECK_SETUP = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(CHECK_SETUP)


class FixtureIntegrityTest(unittest.TestCase):
    def test_setup_is_valid(self) -> None:
        self.assertEqual([], CHECK_SETUP.validate())

    def test_no_realistic_email_domains_in_security_fixture(self) -> None:
        fixture = (LAB_ROOT / "data/security/adversarial.jsonl").read_text(encoding="utf-8")
        self.assertIn("example.invalid", fixture)

    def test_aws_lab_has_cost_and_cleanup_guardrails(self) -> None:
        lab_spec = (LAB_ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("5,000円", lab_spec)
        self.assertIn("4,000円", lab_spec)
        self.assertIn("Destroy", lab_spec)


if __name__ == "__main__":
    unittest.main()
