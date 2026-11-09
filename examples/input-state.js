// Illustrative pattern only. Verify current GameBay API signatures first.
// Keep event edges separate from held state so menus and continuous movement
// do not accidentally treat a repeated key-down as a new one-shot action.
const held = new Set();

const unsubscribe = gb.onInput(({ player, key, action }) => {
  const id = `${player}:${key}`;
  if (action === "down") {
    const wasHeld = held.has(id);
    held.add(id);
    if (!wasHeld && key === "ok") confirmFor(player);
  } else if (action === "up") {
    held.delete(id);
  }
});

function onGamePaused() {
  held.clear();
}

function confirmFor(player) {
  // Replace with a game action.
  console.info("confirm", player);
}

// Call unsubscribe when the game is permanently torn down, if applicable.
void unsubscribe;
