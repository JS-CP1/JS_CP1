import sys
import tty
import termios
import time
import select

# Map size
WIDTH = 80
HEIGHT = 24
TILE_CHAR = "="

# Player setup
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_char = "^"

# Key handling
MOVE_KEYS = {
    "w": (0, -1),
    "s": (0, 1),
    "a": (-1, 0),
    "d": (1, 0),
}

FACING = {
    "w": "^",
    "s": "v",
    "a": "<",
    "d": ">",
}

# Draw the full board once
for y in range(HEIGHT):
    print(TILE_CHAR * WIDTH)

# Move cursor to player start
print(f"\033[{player_y+1};{player_x+1}H{player_char}", end="", flush=True)

# Save original terminal settings
fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)

try:
    tty.setcbreak(fd)  # Set terminal to raw mode (no Enter required)

    print("\nUse WASD to move, q to quit")

    while True:
        # Non-blocking key check
        dr, _, _ = select.select([sys.stdin], [], [], 0)
        if dr:
            key = sys.stdin.read(1)
            if key == "q":
                break 
            if key in MOVE_KEYS:
                dx, dy = MOVE_KEYS[key]
                # Erase previous player
                print(f"\033[{player_y+1};{player_x+1}H{" "}", end="", flush=True)
                # Update player position
                player_x += dx
                player_y += dy
                player_char = FACING[key]
                # Draw player at new position
                print(f"\033[{player_y+1};{player_x+1}H{player_char}", end="", flush=True)

        time.sleep(0.01)  # small delay to control speed

finally:
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
