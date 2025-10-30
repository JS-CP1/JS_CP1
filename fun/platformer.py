from turtle import *
import tkinter as tk  # for monitor size
import time

# --- Setup ---
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.destroy()

screen = Screen()
screen.tracer(0)
screen.setup(screen_width, screen_height)
screen.title("Turtle Platformer")

# --- Player setup ---
player = Turtle()
player.shape("square")
player.color("black")
player.shapesize(1, 1)  # normal 20x20
player.penup()
player.goto(0, -230)

# --- Physics ---
gravity = -1.75
yvel = 0
xvel = 0
keys_pressed = set()

# --- Platforms ---
platforms = []

def make_platform(x, y, width):
    p = Turtle()
    p.shape("square")
    p.color("black")
    p.shapesize(0.5, width / 20)
    p.penup()
    p.goto(x, y)
    platforms.append((x, y, width))
    return p

# Ground + Floating Platforms
make_platform(0, -screen_height // 2 + 100, screen_width - 200)
make_platform(-150, -100, 150)
make_platform(150, 0, 200)
make_platform(0, 150, 120)

# --- Input handling ---
def key_down(key):
    keys_pressed.add(key)

def key_up(key):
    keys_pressed.discard(key)

def quit_game():
    screen.bye()

# Bind keys
screen.listen()
for key in ["a", "d", "w"]:
    screen.onkeypress(lambda k=key: key_down(k), key)
    screen.onkeyrelease(lambda k=key: key_up(k), key)
screen.onkeypress(quit_game, "q")

# --- Collision detection ---
def check_platform_collision(old_y, new_y, px, vy):
    player_half_height = 10
    for (x, y, width) in platforms:
        half_width = width / 2
        if abs(px - x) < half_width:
            bottom_old = old_y - player_half_height
            bottom_new = new_y - player_half_height
            top_old = old_y + player_half_height
            top_new = new_y + player_half_height

            # Landing on top
            if vy < 0 and bottom_old >= y and bottom_new <= y + 5:
                return ("land", y + 5)

            # Hitting head (ceiling)
            if vy > 0 and top_old <= y and top_new >= y - 5:
                return ("head", y - 15)

    return (None, None)

# --- Game loop ---
def game_loop():
    global xvel, yvel

    old_y = player.ycor()

    # Handle input
    if "a" in keys_pressed:
        xvel = -10
    elif "d" in keys_pressed:
        xvel = 10
    else:
        xvel = 0

    if "w" in keys_pressed and yvel == 0:
        yvel = 35

    # Apply gravity
    yvel += gravity
    new_y = player.ycor() + yvel
    new_x = player.xcor() + xvel

    # Check platform collisions (top and bottom)
    collision_type, platform_y = check_platform_collision(old_y, new_y, new_x, yvel)
    if collision_type == "land":
        new_y = platform_y + 10
        yvel = 0
    elif collision_type == "head":
        new_y = platform_y - 10
        yvel = -2  # bounce slightly down after hitting head

    player.goto(new_x, new_y)
    screen.update()
    screen.ontimer(game_loop, 20)

# --- Start ---
game_loop()
screen.mainloop()
