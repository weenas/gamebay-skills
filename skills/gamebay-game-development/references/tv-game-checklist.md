# GameBay TV Game Checklist

## Before implementation

- [ ] Confirm game ID, genre, one/multiplayer mode, target device and Runtime API version.
- [ ] Decide D-pad/OK/controller actions and how the player discovers them.
- [ ] Decide whether progress is session-only, a save, or a resumable checkpoint.
- [ ] Confirm every asset is original or properly licensed.

## During implementation

- [ ] All required resources are bundled locally; no runtime network dependencies.
- [ ] TV-readable typography and contrast; selected/focused control is obvious from couch distance.
- [ ] D-pad and OK cover all menus and gameplay actions; controls do not depend on touch or mouse.
- [ ] Continuous movement, one-shot actions, and key repeat are handled separately.
- [ ] Held input is cleared on pause, resume edge cases, focus loss, restart, and disconnect.
- [ ] Simulation uses elapsed time; frame delta is clamped after long pauses.
- [ ] Entity/effect/audio counts are bounded.
- [ ] Audio begins after user interaction and behaves correctly during host lifecycle events.
- [ ] Save data is validated, versioned, bounded, and written at safe points.
- [ ] Only used capabilities are declared, with matching HTML metadata.

## Before release packaging

- [ ] Run the current repository packer and all relevant checks.
- [ ] Confirm the GPK includes the intended code and assets and respects current limits.
- [ ] Test local browser preview and keyboard mappings.
- [ ] Test an actual Android TV remote and representative controller.
- [ ] Verify pause/resume, restart, game-over, save/resume, and offline launch.
- [ ] Verify readable layout at real TV distance and resolution.
- [ ] Record exact tested device/OS/controller and results; do not generalize beyond evidence.
- [ ] Increment the game version when packaged content changes, per the current repository rules.
- [ ] Treat submission as an external action; only upload to review when explicitly requested.
