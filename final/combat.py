import sys
import tty
import termios
import time
import select

WIDTH = 80
HEIGHT = 24
TILE_CHAR = "="

player_x = WIDTH // 2
player_y = HEIGHT // 2
player_char = "^"

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

for y in range(HEIGHT):
    print(TILE_CHAR * WIDTH)

print(f"\033[{player_y+1};{player_x+1}H{player_char}", end="", flush=True)

fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)

try:
    tty.setcbreak(fd)

    print("\nUse WASD to move, q to quit")

    while True:
        dr, _, _ = select.select([sys.stdin], [], [], 0)
        if dr:
            key = sys.stdin.read(1)
            if key == "q":
                break 
            if key in MOVE_KEYS:
                dx, dy = MOVE_KEYS[key]
                print(f"\033[{player_y+1};{player_x+1}H{" "}", end="", flush=True)
                player_x += dx
                player_y += dy
                player_char = FACING[key]
                print(f"\033[{player_y+1};{player_x+1}H{player_char}", end="", flush=True)

        time.sleep(0.01)

finally:
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
