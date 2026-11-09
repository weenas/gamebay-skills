---
name: gamebay-game-development
description: Build, port, debug, optimize, package, or review games for the GameBay Android TV platform. Use when a task mentions GameBay, GPK, GameBay Runtime, or preparing an HTML/JavaScript game for GameBay. Covers TV-first controls, capability declarations, offline constraints, save data, validation, and submission packaging.
license: MIT
---

# GameBay Game Development

Use this skill to make games that work as GameBay GPK packages on Android TV. It is a platform-specific playbook, not a replacement for the GameBay SDK or current developer documentation.

## Start by inspecting the actual project

1. Find the game's `gamebay.json`, `index.html`, bundled `runtime.js`, game code, and packaging command.
2. Read the current platform contract in [platform-contract.md](references/platform-contract.md).
3. Inspect the project's own SDK and packaging validator. Do not assume examples in this skill match a newer API.
4. Before using an API, verify its signature and behavior in the current `weenas/gamebay-games` SDK and host implementation.
5. Preserve unrelated user changes. Do not edit generated GPKs or bump a published version unless the task requires a release package.

## GameBay design constraints

- Treat the TV as the primary device: landscape 16:9, readable at couch distance, large focus/selection states, and complete operation using a D-pad and OK. Support the host's declared controller inputs as appropriate.
- The game runs locally in the GameBay Android WebView sandbox. Bundle every required script, image, font, and audio asset. Do not depend on a server, CDN, external URL, remote script, or runtime network fetch.
- Use the GameBay Runtime APIs for platform integration. Declare every used capability in both `gamebay.json` and the matching HTML meta tag. Undeclared APIs may be rejected by the SDK or host.
- The host owns global Back/B behavior and pause/navigation. Do not add a redundant in-game “back to library” button. Handle lifecycle pause/resume cleanly.
- Keep simulation timing independent of display refresh. Use `requestAnimationFrame` for rendering, elapsed-time updates for simulation, and clamp unusually large frame deltas after pause/resume.
- Keep rendering and resource use appropriate for Android TV hardware. Bound particles, projectiles, audio voices, and other transient objects; pre-render repeated artwork where useful; profile before adding complexity.
- Save only intentionally resumable game state. Validate stored data and version it; do not assume WebView storage survives app-data clearing or uninstall.
- Use original or properly licensed code, art, fonts, music, and sound effects. Include attribution or license notes where required.

## Recommended workflow

### 1. Clarify and plan

Identify game genre, single/multiplayer needs, control scheme, expected session length, save/resume behavior, and target Android TV. For changes to an existing game, reproduce the issue or inspect logs before changing code.

### 2. Implement in small pieces

- Keep game state, update logic, rendering, input, audio, and UI separable when complexity warrants it.
- Build a predictable state machine for title, playing, paused (host-driven), game-over, and results states.
- Convert input into game actions in one place. Handle `down`/`up`, held input and repeats deliberately; avoid triggering a one-shot action on every repeated event.
- For continuous movement, use normalized analog values or a consistent directional state. Add stick dead zones and prevent impossible immediate reversals where the genre requires it.
- Start audio only after an accepted user action. Use local assets or the current `gb.audio` API and test lifecycle pause/resume.
- For multiplayer, use the current `gb.players` and `gb.input` contracts. Do not infer player ownership by independently polling physical controllers when the host provides bound player state.

### 3. Declare capabilities and package metadata

Use the smallest accurate capability set. Keep the `capabilities` array unique and sorted as required by the current packer, and ensure `index.html` has exactly the matching `gamebay-capabilities` meta value. Declare `players` only with the required player metadata; `resume: true` must meet the SDK's checkpoint/launch requirements. Verify these rules from the current packer before release.

### 4. Validate progressively

1. Run the repository's static checks and package validator.
2. Run the game in a local browser preview using the documented command.
3. Test keyboard preview mappings for D-pad, OK, and Back, while remembering the host may reserve Back.
4. Install on an Android TV and test the real remote, at least one representative controller, focus/selection, input hold/repeat, audio, lifecycle pause/resume, restart, and save/resume.
5. Test with network unavailable to confirm all runtime dependencies are local.
6. Review GPK contents, metadata, size limits, and asset licensing. Only create or submit a release package when asked.

Record device model, Android/WebView version, controller model, test steps, and observed result for compatibility claims. Do not describe an untested device as verified.

## Focused references

- [Platform contract](references/platform-contract.md): packaging, capabilities, input, lifecycle, storage, and security boundaries.
- [TV game checklist](references/tv-game-checklist.md): implementation and test checklist.
- [Reference games](references/reference-games.md): which current GameBay examples are useful for specific patterns.
- [Input example](../../examples/input-state.js): minimal event-state handling pattern; adapt to the verified SDK.

## Troubleshooting rules

- If a control fails, inspect the entire path: physical device event → Android host mapping → SDK dispatch/state → game action. Do not patch only the game until the failing layer is known.
- If input sticks, verify both press and release paths, focus/blur, pause/resume, and held-state cleanup.
- If analog movement jitters, inspect axis range, dead zone, normalization, and per-frame polling/event cadence.
- If sound is missing, verify local asset paths, a user gesture, the host media settings, and lifecycle behavior.
- If performance drops, measure frame time first; reduce unnecessary drawing, scaling, allocations, and unbounded entity counts.
- If packaging rejects a game, trust the current validator output and inspect the manifest, meta tag, paths, hashes, size limits, API version, and declared capabilities.
