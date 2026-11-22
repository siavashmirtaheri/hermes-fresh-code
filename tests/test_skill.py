"""Structural checks for the fresh-code skill (stdlib only).

Run: python -m unittest discover -s tests -v
"""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "fresh-code" / "SKILL.md"


class SkillTests(unittest.TestCase):
    def setUp(self):
        self.text = SKILL.read_text(encoding="utf-8")

    def test_frontmatter_required_fields(self):
        parts = self.text.split("---", 2)
        self.assertGreaterEqual(len(parts), 3, "frontmatter must be fenced by ---")
        fm = parts[1]
        for key in ("name:", "description:", "version:"):
            self.assertIn(key, fm)

    def test_description_length(self):
        match = re.search(r"^description:\s*(.+)$", self.text, re.MULTILINE)
        self.assertIsNotNone(match)
        self.assertLessEqual(len(match.group(1).strip()), 60)

    def test_standard_sections_in_order(self):
        headings = re.findall(r"^## (.+)$", self.text, re.MULTILINE)
        for required in ("When to Use", "Procedure", "Pitfalls", "Verification"):
            self.assertIn(required, headings)
        self.assertLess(headings.index("When to Use"), headings.index("Procedure"))
        self.assertLess(headings.index("Procedure"), headings.index("Pitfalls"))
        self.assertLess(headings.index("Pitfalls"), headings.index("Verification"))

    def test_referenced_support_files_exist(self):
        for rel in (
            "fresh-code/references/version-checks.md",
            "fresh-code/references/completeness-checklist.md",
            "fresh-code/templates/implementation-report.md",
        ):
            self.assertTrue((ROOT / rel).is_file(), f"missing {rel}")

    def test_no_placeholder_headings(self):
        # The skill may name these markers as things to avoid; it must not
        # contain them as actual section headings or standalone lines.
        for line in self.text.splitlines():
            self.assertFalse(line.strip().startswith(("TODO", "FIXME")))

    def test_skills_sh_grouping(self):
        import json

        data = json.loads((ROOT / "skills.sh.json").read_text(encoding="utf-8"))
        names = [s for group in data["groupings"] for s in group["skills"]]
        self.assertIn("fresh-code", names)


if __name__ == "__main__":
    unittest.main()
