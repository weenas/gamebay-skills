# GameBay Design and Feel Guidance

Use these principles to make games understandable and satisfying on a television. They supplement the GameBay SDK and host contract; they do not replace platform validation or player testing.

## Design for the living room

- Treat the television as the primary screen and the remote or controller as the primary input. Do not make progress depend on a pointer, touch gesture, hover, or keyboard-only action.
- At a glance, a player should be able to tell what is happening, what they can do next, and which item currently has focus. Keep focus order predictable and focus styling visible at couch distance.
- Keep essential information inside comfortable screen margins. Check layouts at the actual TV resolution and viewing distance; do not rely on desktop preview as proof of readability.
- Use contrast, shape, text, and motion together to communicate state. Color alone must not distinguish a required action, warning, or success.
- Keep menus and gameplay prompts consistent with the controls the host actually delivers. Label remote and gamepad actions accurately, and account for host-reserved Back/B behavior.
- Keep transitions short and purposeful. Never let a menu animation, modal, or decorative effect make a held action feel delayed or lost.

## Make feedback support the action

1. Confirm the mechanic and input path work before adding polish. A weak or missing response may be an input, timing, or state bug rather than a presentation problem.
2. Attach feedback to clear game events such as hit, pickup, landing, firing, damage, or completion. Avoid triggering one-shot feedback every frame of a held input.
3. Start with one or two channels, such as a sound plus a brief animation. Add particles, a flash, or a subtle camera/visual effect only if they improve clarity or impact on the target hardware.
4. Match intensity to importance. Routine navigation should stay quiet; major events can be more pronounced. Effects should ease or decay back to the normal state.
5. Keep feedback separate from authoritative simulation and collision state. Visual shake must not move collision bodies or change aim calculations.
6. Keep input usable during and after feedback. Buffer a deliberate action when appropriate, clear held state on lifecycle/input loss, and avoid long freezes or un-cancelable animations.
7. When using flashing, shake, or strong motion, provide a reduced-motion option or a restrained default, and verify that feedback remains understandable when reduced.

These are design constraints, not fixed recipes: there is no universal correct shake amount, pause duration, animation curve, text size, or sample count. Tune on the device and for the game event.

## Turn design claims into a small test

For a significant or uncertain change, make a short design note before building a large system:

- **Decision:** What concrete design choice is being made?
- **Observation:** What did a player, device test, issue report, or log actually show? Record device, input method, and build where relevant.
- **Assumption:** What explanation is not yet established?
- **Causal chain:** `mechanic or UI change -> player/system interaction -> observable behavior -> intended experience`.
- **Counterevidence:** What result would make the team revise or reject the explanation?
- **Small comparison:** Compare the current version with one reversible variant while keeping other factors as similar as practical.
- **Evidence boundary:** State which devices and players were tested, limitations, and unresolved questions. Preserve conflicting feedback rather than flattening it into one average.

Choose a lens only when it helps answer the decision. For example, trace mechanics to moment-to-moment behavior, inspect whether a choice has visible tradeoffs, or inspect how learning and mastery develop. Treat motivation models and player categories as context-specific hypotheses, not permanent labels for players.

Do not use session length, retention, score, or spending alone as proof of fun or benefit. Pair measurements with player observations and check for accessibility barriers. Prefer a small prototype or configuration variant over an irreversible production change.

## GameBay validation pass

Test the same action through the whole path:

`remote/controller -> Android host mapping -> GameBay input event/state -> game action -> visual/audio response`

On a real target TV, verify:

- the initial screen explains the basic controls and shows focus clearly;
- D-pad, OK, analog movement, held input/repeat, and one-shot actions behave as intended for each supported device;
- Back/B follows the GameBay host contract;
- feedback is prompt, proportionate, and returns to rest without blocking further input;
- pause/resume, focus loss, disconnect/reconnect, restart, and save/resume do not leave stale input or effects;
- text, safe margins, motion, and effects remain comfortable and legible at normal viewing distance;
- performance remains stable on the actual Android TV hardware.

Record tested model, Android/WebView version, controller, build, steps, and observed result. Distinguish measured behavior from interpretation; do not claim broad compatibility based on a single setup.

## Inspiration and adaptation

This guidance distills general ideas from:

- [game-ui-design](https://github.com/omer-metin/skills-for-antigravity/blob/main/skills/game-ui-design/SKILL.md): controller-first navigation, readable TV layouts, safe areas, accessibility, and target-device testing.
- [game-feel](https://github.com/gamedev-skills/awesome-gamedev-agent-skills/blob/main/skills/disciplines/game-feel/SKILL.md): event-based layered feedback, proportional intensity, return-to-rest behavior, and input-safe effects.
- [game-design-theory](https://github.com/akillness/jeo-skills/blob/main/.agent-skills/game-design-theory/SKILL.md): separating observation from assumption, causal hypotheses, falsifiers, and small controlled prototypes.

The examples in those projects target other toolchains or broader platforms. Use GameBay's current Runtime API, SDK, packer, Android host, and developer documentation for all implementation details.
