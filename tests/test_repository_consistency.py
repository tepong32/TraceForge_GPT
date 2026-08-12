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

        self.assertIn(f"Current release: **v{version} - Applied Knowledge**", readme)
        self.assertIn("current stable baseline is **v0.6 Applied Knowledge**", index)
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

    def test_applied_knowledge_guides_are_discoverable(self):
        root_index = (ROOT / "knowledge" / "README.md").read_text(encoding="utf-8")
        category = ROOT / "knowledge" / "spreadsheets"
        category_index = (category / "README.md").read_text(encoding="utf-8")

        self.assertIn("spreadsheets/README.md", root_index)
        for guide in category.glob("*.md"):
            if guide.name == "README.md":
                continue
            encoded_name = guide.name.replace(" ", "%20")
            self.assertIn(encoded_name, category_index, f"Unindexed guide: {guide.name}")

    def test_excel_guide_keeps_project_rules_out_of_universal_guidance(self):
        guide = (
            ROOT / "knowledge" / "spreadsheets" / "Excel 365 Workbook Engineering.md"
        ).read_text(encoding="utf-8")
        project_only_terms = ["Item No.", "Scheduler → Monthly", "tranche progression"]
        for term in project_only_terms:
            self.assertNotIn(term, guide)

    def test_applied_knowledge_guides_state_evidence_and_revision_boundaries(self):
        guides = [
            path
            for path in (ROOT / "knowledge").rglob("*.md")
            if path.name != "README.md"
        ]
        self.assertGreater(len(guides), 0)
        for guide in guides:
            content = guide.read_text(encoding="utf-8")
            self.assertIn("## Evidence Posture", content, f"{guide} lacks evidence posture")
            self.assertIn("## Revisit Conditions", content, f"{guide} lacks revisit conditions")

    def test_assessment_guide_keeps_inference_visible(self):
        guide = (
            ROOT
            / "knowledge"
            / "spreadsheets"
            / "Spreadsheet Assessment and Business-Rule Discovery.md"
        ).read_text(encoding="utf-8")
        for required in [
            "Assumption Register",
            "Alternative explanation",
            "Cost if wrong",
            "Original-Design Review Standard",
        ]:
            self.assertIn(required, guide)

    def test_assessment_guide_handles_multilingual_excel_annotations(self):
        guide = (
            ROOT
            / "knowledge"
            / "spreadsheets"
            / "Spreadsheet Assessment and Business-Rule Discovery.md"
        ).read_text(encoding="utf-8")
        for required in [
            "Notes and Comments as Contextual Evidence",
            "Multilingual, Slang, and Keyword-Only Annotations",
            "original wording",
            "working interpretation",
            "project glossary",
            "Tool-Capability Gate",
            "threaded Comments",
        ]:
            self.assertIn(required, guide)


if __name__ == "__main__":
    unittest.main()
