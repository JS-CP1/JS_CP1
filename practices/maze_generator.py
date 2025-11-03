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
weights1 = [30,30,10,10]
weights2 = [10,30]
top_exit = random.randint(1,9)
bottom_exit = random.randint(1,9)

def is_solvable(maze, exit):
    size = len(maze[1]) - 1
    visited = set()
    stack = [(0,0)]
    while stack:
        x, y = stack.pop()
        if x == exit and y == size:
            return True
        if (x,y) in visited:
            continue
        visited.add((x,y))
        if x < size and maze[y][x+1] == "_":
            stack.append((x+1, y))
        if y < size and maze[y+1][x] == "|":
            stack.append((x, y+1))
        if x > 0 and maze[y][x-1] == "_":
            stack.append((x-1,y))
        if y > 0 and maze[y-1][x] == "|":
            stack.append((x,y-1))

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

while True:
    maze = [
        ["|-", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "-|"],
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
        ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
]
    maze[0][top_exit] = " "
    maze[20][bottom_exit] = " "
    for x, row in enumerate(maze):
        for y, cell in enumerate(row):
            if cell == " ":
                maze[x][y] = random.choices(["_", "|", "|-", "-|"], weights=weights1, k=1)[0]
            if y == 0 and x > 0 and x < 20:
                maze[x][y] = random.choices(["|-", "|"], weights=weights2, k=1)[0]
    if is_solvable(maze, bottom_exit):
        break
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
        if cell == "_":
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