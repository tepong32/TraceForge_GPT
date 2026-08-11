"""Prepare TraceForge version and changelog updates with explicit Git effects."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from datetime import date
from pathlib import Path
from typing import Iterable, Sequence


VERSION_FILE = Path("VERSION")
CHANGELOG_FILE = Path("CHANGELOG.md")
VERSIONED_FILES = [Path("setup.py"), Path("src/__init__.py")]
CHANGELOG_CATEGORIES = {
    "feature": "Added",
    "fix": "Fixed",
    "refactor": "Changed",
    "chore": "Changed",
    "docs": "Changed",
}
VERSION_PATTERN = re.compile(r"^\d+\.\d+\.\d+$")


def get_current_version(version_file: Path = VERSION_FILE) -> str:
    """Read and validate a semantic version without modifying the repository."""
    if not version_file.exists():
        raise FileNotFoundError(f"Version file not found: {version_file}")

    version = version_file.read_text(encoding="utf-8").strip()
    if not VERSION_PATTERN.fullmatch(version):
        raise ValueError(f"Invalid semantic version in {version_file}: {version!r}")
    return version


def bump_version(current_version: str, bump_type: str) -> str:
    """Return the requested major, minor, or patch increment."""
    if not VERSION_PATTERN.fullmatch(current_version):
        raise ValueError(f"Invalid semantic version: {current_version!r}")
    if bump_type not in {"major", "minor", "patch"}:
        raise ValueError(f"Unsupported bump type: {bump_type}")

    major, minor, patch = map(int, current_version.split("."))
    if bump_type == "major":
        return f"{major + 1}.0.0"
    if bump_type == "minor":
        return f"{major}.{minor + 1}.0"
    return f"{major}.{minor}.{patch + 1}"


def build_changelog_entry(
    new_version: str,
    message: str,
    category: str = "feature",
    release_date: date | None = None,
) -> str:
    """Build a concise Keep-a-Changelog-style release entry."""
    cleaned_message = message.strip()
    if not cleaned_message:
        raise ValueError("Release message cannot be empty")
    if category not in CHANGELOG_CATEGORIES:
        raise ValueError(f"Unsupported changelog category: {category}")

    heading = CHANGELOG_CATEGORIES[category]
    entry_body = cleaned_message if "\n" in cleaned_message else f"- {cleaned_message}"
    stamp = (release_date or date.today()).isoformat()
    return f"## [{new_version}] - {stamp}\n\n### {heading}\n\n{entry_body}\n"


def insert_changelog_entry(existing: str, entry: str) -> str:
    """Insert an entry immediately below the changelog title."""
    normalized = existing.strip()
    if not normalized:
        normalized = "# Changelog"
    if not normalized.startswith("# Changelog"):
        normalized = f"# Changelog\n\n{normalized}"

    remainder = normalized[len("# Changelog") :].lstrip()
    if remainder:
        return f"# Changelog\n\n{entry.strip()}\n\n{remainder.rstrip()}\n"
    return f"# Changelog\n\n{entry.strip()}\n"


def update_version_in_files(
    old_version: str,
    new_version: str,
    versioned_files: Iterable[Path] = VERSIONED_FILES,
    *,
    dry_run: bool = False,
) -> list[Path]:
    """Replace declared Python version assignments and return affected files."""
    assignment = re.compile(
        rf"(?P<prefix>(?:version|__version__)\s*=\s*['\"]){re.escape(old_version)}(?P<suffix>['\"])"
    )
    affected: list[Path] = []

    for file_path in versioned_files:
        if not file_path.exists():
            continue
        content = file_path.read_text(encoding="utf-8")
        updated, count = assignment.subn(
            lambda match: f"{match.group('prefix')}{new_version}{match.group('suffix')}",
            content,
        )
        if count:
            affected.append(file_path)
            if not dry_run:
                file_path.write_text(updated, encoding="utf-8")
    return affected


def update_files(
    old_version: str,
    new_version: str,
    message: str,
    category: str,
    *,
    version_file: Path = VERSION_FILE,
    changelog_file: Path = CHANGELOG_FILE,
    versioned_files: Iterable[Path] = VERSIONED_FILES,
    dry_run: bool = False,
) -> list[Path]:
    """Prepare the version and changelog files without invoking Git."""
    entry = build_changelog_entry(new_version, message, category)
    existing_changelog = (
        changelog_file.read_text(encoding="utf-8") if changelog_file.exists() else "# Changelog\n"
    )
    new_changelog = insert_changelog_entry(existing_changelog, entry)
    secondary = update_version_in_files(
        old_version, new_version, versioned_files, dry_run=dry_run
    )
    changed = [version_file, changelog_file, *secondary]

    if dry_run:
        print(f"VERSION would change: {old_version} -> {new_version}")
        print("\nChangelog entry:\n")
        print(entry.rstrip())
        print("\nNo files or Git state were changed.")
        return changed

    version_file.write_text(f"{new_version}\n", encoding="utf-8")
    changelog_file.write_text(new_changelog, encoding="utf-8")
    return changed


def working_tree_is_clean() -> bool:
    result = subprocess.run(
        ["git", "status", "--porcelain"], capture_output=True, text=True, check=True
    )
    return not result.stdout.strip()


def run_git_release(
    new_version: str,
    message: str,
    changed_files: Sequence[Path],
    *,
    commit: bool,
    tag: bool,
    push: bool,
) -> None:
    """Run only the Git effects explicitly requested by the caller."""
    if not commit:
        return

    subprocess.run(["git", "add", *map(str, changed_files)], check=True)
    subprocess.run(
        ["git", "commit", "-m", f"Release: {message} (v{new_version})"], check=True
    )
    if tag:
        subprocess.run(["git", "tag", f"v{new_version}"], check=True)
    if push:
        subprocess.run(["git", "push"], check=True)
        subprocess.run(["git", "push", "--tags"], check=True)


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Update TraceForge version metadata; Git effects require explicit flags."
    )
    parser.add_argument("message", help="Changelog and optional release-commit message")
    parser.add_argument(
        "bump", choices=["patch", "minor", "major"], nargs="?", default="patch"
    )
    parser.add_argument(
        "-c",
        "--category",
        choices=sorted(CHANGELOG_CATEGORIES),
        default="feature",
    )
    parser.add_argument("-d", "--dry-run", action="store_true")
    parser.add_argument("--commit", action="store_true", help="Commit updated release files")
    parser.add_argument("--tag", action="store_true", help="Tag the new commit; requires --commit")
    parser.add_argument("--push", action="store_true", help="Push commit and tags; requires --tag")
    args = parser.parse_args(argv)

    if args.tag and not args.commit:
        parser.error("--tag requires --commit")
    if args.push and not args.tag:
        parser.error("--push requires --tag")
    return args


def main(argv: Sequence[str] | None = None) -> int:
    try:
        args = parse_args(argv)
        old_version = get_current_version()
        new_version = bump_version(old_version, args.bump)

        if args.commit and not args.dry_run and not working_tree_is_clean():
            raise RuntimeError(
                "Git release actions require a clean working tree. Commit project changes first, "
                "or omit --commit to update release files locally."
            )

        changed_files = update_files(
            old_version,
            new_version,
            args.message,
            args.category,
            dry_run=args.dry_run,
        )

        if args.dry_run:
            if args.commit:
                print("Git commit/tag/push actions were skipped by --dry-run.")
            return 0

        run_git_release(
            new_version,
            args.message,
            changed_files,
            commit=args.commit,
            tag=args.tag,
            push=args.push,
        )
        print(f"Prepared TraceForge v{new_version}.")
        return 0
    except (FileNotFoundError, ValueError, RuntimeError, subprocess.CalledProcessError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
