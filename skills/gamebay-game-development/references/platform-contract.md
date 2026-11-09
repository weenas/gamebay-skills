# GameBay Platform Contract (SDK v4)

This reference describes the current GameBay package and platform boundaries. The authoritative signatures are the pinned SDK bundle, the host validator, and the current developer documentation.

## Package and SDK

- A GPK contains the game entry page, game code, game-owned assets, and a manifest. It declares an exact `sdkVersion` and capabilities; it does not contain `runtime.js` or other SDK files.
- The matching immutable `.gbsdk` package contains `manifest.json`, the shared runtime, and platform-owned public resources. Its manifest records version, runtime contract, and per-file SHA-256 values. The server publishes an outer package SHA-256 and size.
- The APK downloads and validates the SDK bundle before first use, stores it in the app-private versioned cache, and serves files to the game WebView from a same-origin local path. Once cached, the game can start offline.
- Game source directories keep a local copy of `runtime.js` only for browser preview. It must match `sdk/runtime.js`; the packer excludes it from GPK output. Game HTML still references `runtime.js`, which the host or platform playtest service resolves from the declared SDK bundle.
- Public SDK assets use the reserved `__gamebay_sdk__/` URL namespace. Never place files under this path in a GPK.
- SDK versions are immutable. Build a new version for any shared runtime change; never replace package contents at an existing version.

## Declared capabilities

Declare only used APIs in a unique, alphabetically sorted `capabilities` list and mirror the comma-separated list in the HTML `gamebay-capabilities` meta tag.

| Capability | API family |
| --- | --- |
| `input` | `gb.onInput(...)`, `gb.input.state(player)` |
| `players` | `gb.players.list()`, `gb.players.onChange(...)` |
| `audio` | `gb.audio.create(localPath)`, `gb.audio.tone(...)` |
| `lifecycle` | `gb.onLifecycle(...)` |
| `storage` | Per-game local key-value storage with quotas |
| `save` | `gb.save.load()`, `write(data)`, `clear()` |
| `checkpoint`, `launch` | Resumable checkpoints and host continue/new decision |
| `haptics` | Player/controller vibration when available |
| `exit` | Host exit route when declared |
| `log` | `gb.log(...)` to local host diagnostics |

Read the exact method signatures, limits, lifecycle behavior, and capability dependencies from the SDK and validator before coding.

## Ownership boundaries

- The Android host owns TV controller discovery/mapping, player binding, global Back/Start pause menu, app navigation, SDK download/cache verification, and sandbox boundaries.
- The SDK exposes normalized input, lifecycle, audio, save/storage, player, and diagnostic APIs. It handles the common API envelope; it does not implement a game's rules or data schema.
- The GPK owns gameplay, game-specific UI, assets, input-to-action mapping, save data shape/migration, and its response to lifecycle events.
- Games must stop their own simulation/timers on `pause`, resume safely on `resume`, reset state on `restart`, and clear held-input state when focus or player state changes. The host's pause overlay does not replace game lifecycle handling.
- Use GameBay player state instead of identifying controllers. Treat optional hardware features such as vibration as unavailable unless the API confirms support.

## Save and security boundaries

- Validate save shapes, ranges, and schema versions before restoring.
- Use bounded checkpoints and write only at intentional safe points. Local saves are not cloud saves and may disappear if app data is cleared or the app is uninstalled.
- SDK and GPK files are client-delivered and extractable. SHA-256 detects corruption or mismatch; it is not DRM or copy protection.
- Keep credentials, private server settings, personal data, and administrative endpoints out of both packages and public game source.
