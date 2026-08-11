import re
import unittest
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


class RepositoryConsistencyTests(unittest.TestCase):
    def test_local_markdown_links_resolve(self):
        missing = []
        for document in ROOT.rglob("*.md"):
            if ".git" in document.parts or "env" in document.parts:
                continue
            content = document.read_text(encoding="utf-8")
            for raw_target in MARKDOWN_LINK.findall(content):
                target = raw_target.strip().strip("<>")
                if target.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                path_text = unquote(target.split("#", 1)[0].split("?", 1)[0])
                if not path_text:
                    continue
                resolved = (document.parent / path_text).resolve()
                if not resolved.exists():
                    missing.append(f"{document.relative_to(ROOT)} -> {target}")
        self.assertEqual(missing, [], "Missing local Markdown links:\n" + "\n".join(missing))

    def test_release_references_match_version_file(self):
        version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        index = (ROOT / "methodology" / "README.md").read_text(encoding="utf-8")
        changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")

        self.assertIn(f"Current release: **v{version} - Collaborative Execution**", readme)
        self.assertIn("current stable baseline is **v0.5 Collaborative Execution**", index)
        self.assertIn(f"## [{version}] -", changelog)
        self.assertLess(changelog.index(f"## [{version}] -"), changelog.index("## [0.4.1] -"))

    def test_handoff_template_and_canonical_file_share_required_sections(self):
        required = [
            "Snapshot",
            "Current Objective",
            "Completed Work",
            "Work in Progress",
            "Decisions",
            "Risks and Blockers",
            "Validation",
            "Next Starting Point",
            "Open Questions",
        ]
        for relative_path in [
            Path("templates/Session Handoff Template.md"),
            Path("SESSION_HANDOFF.md"),
        ]:
            content = (ROOT / relative_path).read_text(encoding="utf-8")
            for section in required:
                self.assertIn(f"## {section}", content, f"{relative_path} lacks {section}")


if __name__ == "__main__":
    unittest.main()
