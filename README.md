# GameBay Skills

Reusable AI-agent skills for developing games for [GameBay](https://github.com/weenas/gamebay), an Android TV game platform.

This repository uses the open Agent Skills directory format. The primary skill is `skills/gamebay-game-development/`; it guides compatible coding agents through GameBay's HTML/CSS/JavaScript game format, Android TV controls, Runtime API, GPK packaging, and device validation.

## Install

Copy `skills/gamebay-game-development/` into an Agent Skills directory supported by your coding tool, or add it to a project under that tool's skills directory. Examples:

| Tool | Common project location |
| --- | --- |
| Codex / Agent Skills-compatible tools | `.agents/skills/gamebay-game-development/` |
| Claude Code | `.claude/skills/gamebay-game-development/` |
| GitHub Copilot in VS Code | `.github/skills/gamebay-game-development/` |

Tool support and discovery paths can change; check your tool's current documentation. The skill itself is plain Markdown and does not require a particular model or vendor.

## What's included

- `skills/gamebay-game-development/SKILL.md`: the portable, task-oriented skill.
- `skills/gamebay-game-development/references/`: platform contract, TV checklist, design/feel guidance, and focused references.
- `skills/gamebay-game-development/examples/`: small patterns for safe input handling.

## Source of truth

The GameBay platform evolves. Before using the skill for a release, compare it with the current sources:

- [GameBay host and developer docs](https://github.com/weenas/gamebay)
- [GameBay game SDK and examples](https://github.com/weenas/gamebay-games)

If a skill note conflicts with the current SDK, host behavior, or developer docs, follow the current platform source and update this repository through a pull request.

## Contributing

Please include the affected GameBay API version, a reproducible example or device evidence when applicable, and any documentation/source links. Avoid copying private server configuration, credentials, user logs, or unreleased game assets into this public repository.

## License

MIT. See [LICENSE](LICENSE).
