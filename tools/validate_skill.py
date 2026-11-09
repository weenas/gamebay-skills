#!/usr/bin/env python3
"""Validate the repository's GameBay Agent Skill metadata and local links."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "gamebay-game-development"
SKILL_FILE = SKILL_DIR / "SKILL.md"


def fail(message: str) -> None:
    print(f"Skill validation failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    text = SKILL_FILE.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    _, frontmatter, _body = text.split("---", 2)
    fields = {}
    for line in frontmatter.splitlines():
        match = re.match(r"^([a-z][a-z0-9_-]*):\s*(.*)$", line)
        if match:
            fields[match.group(1)] = match.group(2).strip().strip("\"")

    name = fields.get("name", "")
    description = fields.get("description", "")
    if name != SKILL_DIR.name:
        fail(f"frontmatter name must match directory name {SKILL_DIR.name!r}")
    if not description:
        fail("frontmatter description is required")
    if len(description) > 1024:
        fail("frontmatter description must be at most 1024 characters")

    broken = []
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        if target.startswith(("https://", "http://", "mailto:", "#")):
            continue
        path = (SKILL_FILE.parent / target.split("#", 1)[0]).resolve()
        if not path.is_relative_to(SKILL_FILE.parent.resolve()) or not path.exists():
            broken.append(target)
    if broken:
        fail("broken or out-of-skill local references: " + ", ".join(broken))

    print(f"Validated {SKILL_FILE.relative_to(ROOT)} and its local references")


if __name__ == "__main__":
    main()
