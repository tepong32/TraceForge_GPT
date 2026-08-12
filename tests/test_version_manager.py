import io
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from datetime import date
from pathlib import Path
from unittest.mock import patch

import version_manager


class VersionManagerTests(unittest.TestCase):
    def test_bump_version(self):
        self.assertEqual(version_manager.bump_version("1.2.3", "patch"), "1.2.4")
        self.assertEqual(version_manager.bump_version("1.2.3", "minor"), "1.3.0")
        self.assertEqual(version_manager.bump_version("1.2.3", "major"), "2.0.0")

    def test_build_changelog_entry(self):
        entry = version_manager.build_changelog_entry(
            "0.5.0", "Collaborative execution", "feature", date(2026, 8, 12)
        )
        self.assertEqual(
            entry,
            "## [0.5.0] - 2026-08-12\n\n### Added\n\n- Collaborative execution\n",
        )

    def test_insert_changelog_entry_below_title(self):
        result = version_manager.insert_changelog_entry(
            "# Changelog\n\n## [0.4.1] - 2026-08-04\n",
            "## [0.5.0] - 2026-08-12\n\n### Added\n\n- New behavior\n",
        )
        self.assertLess(result.index("[0.5.0]"), result.index("[0.4.1]"))
        self.assertTrue(result.endswith("\n"))

    def test_secondary_version_uses_original_version(self):
        with tempfile.TemporaryDirectory() as directory:
            module = Path(directory) / "module.py"
            module.write_text('__version__ = "0.4.1"\n', encoding="utf-8")
            affected = version_manager.update_version_in_files(
                "0.4.1", "0.5.0", [module]
            )
            self.assertEqual(affected, [module])
            self.assertIn('"0.5.0"', module.read_text(encoding="utf-8"))

    def test_dry_run_does_not_write(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            version_file = root / "VERSION"
            changelog_file = root / "CHANGELOG.md"
            module = root / "module.py"
            version_file.write_text("0.4.1\n", encoding="utf-8")
            changelog_file.write_text("# Changelog\n", encoding="utf-8")
            module.write_text('version = "0.4.1"\n', encoding="utf-8")
            before = {
                path: path.read_bytes() for path in [version_file, changelog_file, module]
            }

            with redirect_stdout(io.StringIO()):
                version_manager.update_files(
                    "0.4.1",
                    "0.5.0",
                    "Preview",
                    "feature",
                    version_file=version_file,
                    changelog_file=changelog_file,
                    versioned_files=[module],
                    dry_run=True,
                )

            self.assertEqual(
                before,
                {path: path.read_bytes() for path in [version_file, changelog_file, module]},
            )

    def test_update_files_writes_version_changelog_and_secondary(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            version_file = root / "VERSION"
            changelog_file = root / "CHANGELOG.md"
            module = root / "module.py"
            version_file.write_text("0.4.1\n", encoding="utf-8")
            changelog_file.write_text("# Changelog\n", encoding="utf-8")
            module.write_text('version = "0.4.1"\n', encoding="utf-8")

            version_manager.update_files(
                "0.4.1",
                "0.5.0",
                "Prepared v0.5",
                "feature",
                version_file=version_file,
                changelog_file=changelog_file,
                versioned_files=[module],
            )

            self.assertEqual(version_file.read_text(encoding="utf-8"), "0.5.0\n")
            self.assertIn("[0.5.0]", changelog_file.read_text(encoding="utf-8"))
            self.assertIn('"0.5.0"', module.read_text(encoding="utf-8"))

    def test_git_flags_require_dependencies(self):
        with redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit):
                version_manager.parse_args(["message", "minor", "--tag"])
            with self.assertRaises(SystemExit):
                version_manager.parse_args(["message", "minor", "--push", "--commit"])

    @patch("version_manager.subprocess.run")
    def test_git_effects_only_run_when_requested(self, run):
        changed = [Path("VERSION"), Path("CHANGELOG.md")]
        version_manager.run_git_release(
            "0.5.0", "Release", changed, commit=False, tag=False, push=False
        )
        run.assert_not_called()

        version_manager.run_git_release(
            "0.5.0", "Release", changed, commit=True, tag=True, push=True
        )
        commands = [call.args[0] for call in run.call_args_list]
        self.assertEqual(commands[0], ["git", "add", "VERSION", "CHANGELOG.md"])
        self.assertIn(["git", "tag", "v0.5.0"], commands)
        self.assertEqual(commands[-2:], [["git", "push"], ["git", "push", "--tags"]])


if __name__ == "__main__":
    unittest.main()
