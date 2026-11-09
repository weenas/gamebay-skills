// Illustrative pattern only. Verify current GameBay API signatures first.
// Keep event edges separate from held state so menus and continuous movement
// do not accidentally treat a repeated key-down as a new one-shot action.
const held = new Set();

const unsubscribeInput = gb.onInput(({ player, key, action }) => {
  const id = `${player}:${key}`;
  if (action === "down") {
    const wasHeld = held.has(id);
    held.add(id);
    if (!wasHeld && key === "ok") confirmFor(player);
  } else if (action === "up") {
    held.delete(id);
  }
});

const unsubscribeLifecycle = gb.onLifecycle(({ type }) => {
  if (type === "pause" || type === "restart" || type === "exit") held.clear();
});

function confirmFor(player) {
  // Replace with a game action.
  console.info("confirm", player);
}

// Retain these for teardown if the game's lifecycle needs explicit cleanup.
void unsubscribeInput;
void unsubscribeLifecycle;
