# GameBay Reference Games

The examples below are useful starting points in the public `weenas/gamebay-games` repository. Their current code may evolve; inspect the latest source rather than copying from an old package.

| Need | Reference | Why |
| --- | --- | --- |
| Smallest Canvas game / basic controls | `games/star-dodger/` | Minimal movement and menu actions |
| Save/load and simple game loop | `games/snake/` | Local save data, lifecycle and input |
| Modular larger game, rendering and TV performance | `games/sky-strike/` | Separate modules, input adaptation, bounded effects and checkpoints |
| Tank movement and two-player actions | `games/battle-tank/` | Tile-based movement, collision and player controls |
| Runtime API v3 multiplayer | `games/crystal-haul/` | Player list, per-player state and cooperative play |
| Multiplayer versus / AI fill | `games/boom-squad/` | Player slots and local opponent behavior |

When the example and the current SDK disagree, follow the SDK and host contract, then raise a documentation update for the stale example.
