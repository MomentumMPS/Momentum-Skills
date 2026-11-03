#!/usr/bin/env python3
"""Link this collection into user-level skill locations without replacing files."""

import argparse
from pathlib import Path
import sys


def install(repo: Path, user_home: Path, *, dry_run: bool = False) -> None:
    skills = sorted(path.parent.resolve() for path in (repo / "skills").glob("*/SKILL.md"))
    if not skills:
        raise ValueError("No skills found beside install.py.")

    # Codex and Cursor share .agents/skills; Claude Code uses .claude/skills.
    roots = [user_home / ".agents/skills", user_home / ".claude/skills"]
    links = [(source, root / source.name) for root in roots for source in skills]
    conflicts = []
    for root in roots:
        for parent in (root, *root.parents):
            if (parent.exists() or parent.is_symlink()) and not parent.is_dir():
                conflicts.append(str(parent))
                break
    for source, target in links:
        if target.is_symlink() and target.resolve() == source:
            continue
        if target.exists() or target.is_symlink():
            conflicts.append(str(target))
    if conflicts:
        raise FileExistsError(
            "Existing paths need review; nothing was changed:\n  "
            + "\n  ".join(sorted(set(conflicts)))
            + "\nCompare and back up these paths outside skill discovery folders, then retry."
        )

    for source, target in links:
        if target.is_symlink() and target.resolve() == source:
            print(f"Already linked: {target}")
            continue
        if dry_run:
            print(f"Would link: {target} -> {source}")
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        # No overwrite flag: even a path created after preflight is preserved.
        target.symlink_to(source, target_is_directory=True)
        print(f"Linked: {target} -> {source}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Check paths without writing")
    args = parser.parse_args()
    try:
        install(Path(__file__).resolve().parent, Path.home(), dry_run=args.dry_run)
    except (OSError, ValueError) as error:
        print(f"Installation stopped: {error}", file=sys.stderr)
        sys.exit(1)
