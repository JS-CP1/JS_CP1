# JS, 1st, Maze Generator
from turtle import *
import random
from collections import deque

player = Turtle()
player.penup()
screen = Screen()
screen.setup(500,500)
screen.title("Maze Generator")
keys_pressed = set()

def key_down(key):
    keys_pressed.add(key)

def key_up(key):
    keys_pressed.discard(key)

def quit_game():
    screen.bye()

screen.listen()
for key in ["a", "d", "w", "s"]:
    screen.onkey(lambda k=key: key_down(k), key)
    screen.onkeyrelease(lambda k=key: key_up(k), key)
screen.onkeypress(quit_game, "q")

# ⏼︎ player with |
# ⊝︎ player with -
# ◯︎ player with 
# ◶︎ player with |-
# ◶︎ player with -|
maze = [
    ["|-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-|"],
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
    ["|", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "|"],
    ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
]
w1 = [30,30,10,10]
w2 = [10,30]
for r, row in enumerate(maze):
    for c, cell in enumerate(row):
        if cell == " ":
            maze[r][c] = random.choices(["-", "|", "|-", "-|"], weights=w1, k=1)[0]
        if c == 0 and r > 0 and r < 20:
            maze[r][c] = random.choices(["|-", "|"], weights=w2, k=1)[0]
for r, row in enumerate(maze):
    for c, cell in enumerate(row):
        if cell == "|-" and "-" in maze[r+1][c] and maze[r][c+1] == "|":
            maze[r][c] = "|"
top_exit = random.randint(1,9)
bottom_exit = random.randint(1,9)
maze[0][top_exit] = " "
maze[20][bottom_exit] = " "
start_row = 19
player.goto(bottom_exit * 20 - 190, 190)

#While on - you cannot go down.
#While on | you cannot go left.
#While on |- you cannot go left or down.
#While on -| you cannot go right or down.
#While under - you cannot go up.
#While under |- or -| you cannot go up

walls = Turtle()
walls.color("black")
walls.penup()
walls.speed(10)
for r, row in enumerate(maze):
    for col, cell in enumerate(row):
        walls.penup()
        walls.goto(col * 20 - 200, r * 20 - 200)
        if cell == "-":
            walls.setheading(0)
            walls.pendown()
            walls.forward(20)
            walls.penup()
        elif cell == "|":
            walls.setheading(90)
            walls.pendown()
            walls.forward(20)
            walls.penup()
        elif cell == "|-":
            walls.setheading(90)
            walls.pendown()
            walls.forward(20)
            walls.penup()
            walls.backward(20)
            walls.setheading(0)
            walls.pendown()
            walls.forward(20)
            walls.penup()
        elif cell == "-|":
            walls.setheading(0)
            walls.pendown()
            walls.forward(20)
            walls.setheading(90)
            walls.forward(20)
            walls.penup()
walls.hideturtle()

def neighbors(r, c, maze):
    rows, cols = len(maze), len(maze[0])
    # up
    if r > 0 and '-' not in maze[r][c]:
        yield r - 1, c
    # down
    if r + 1 < rows and '-' not in maze[r + 1][c]:
        yield r + 1, c
    # left
    if c > 0 and '|' not in maze[r][c]:
        yield r, c - 1
    # right
    if c + 1 < cols and '|' not in maze[r][c + 1]:
        yield r, c + 1

def reachable_from(start, maze):
    q = deque([start])
    seen = {start}
    while q:
        r, c = q.popleft()
        for nr, nc in neighbors(r, c, maze):
            if (nr, nc) not in seen:
                seen.add((nr, nc))
                q.append((nr, nc))
    return seen

# usage:
start = (start_row, bottom_exit)            # for your code
reachable = reachable_from(start, maze)
all_cells = {(r, c) for r in range(len(maze)) for c in range(len(maze[0]))}
unreachable = all_cells - reachable

print("reachable:", len(reachable))
print("unreachable components (count):", len(unreachable))
# optionally list or inspect unreachable cells:
if unreachable:
    print("some unreachable cells:", list(unreachable)[:20])

while True:
    if "a" in keys_pressed:
        player.setx(player.xcor() - 5)
    if "d" in keys_pressed:
        player.setx(player.xcor() + 5)
    if "w" in keys_pressed:
        player.sety(player.ycor() + 5)
    if "s" in keys_pressed:
        player.sety(player.ycor() - 5)
    screen.update()