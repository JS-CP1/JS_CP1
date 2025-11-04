# JS, 1st, Maze Generator
from turtle import *
import random
from collections import deque

solver = Turtle()
solver.penup()
solver.speed(0)
screen = Screen()
screen.setup(500,500)
screen.title("Maze Generator")
screen.tracer(0)
keys_pressed = set()
weights1 = [30,30,10]
weights2 = [10,30]
top_exit = random.randint(1,9)
bottom_exit = random.randint(1,9)
attempts = 0

def is_solvable(maze, exit_col):
    height = len(maze)
    width = len(maze[0])
    visited = [[False] * width for _ in range(height)]
    queue = [(0, exit_col)]
    visited[0][exit_col] = True
    while queue:
        row, col = queue.pop(0)
        if row == height - 1:
            return True
        for row_change, col_change in [(-1,0),(1,0),(0,-1),(0,1)]:
            next_row = row + row_change
            next_col = col + col_change
            if 0 <= next_row < height and 0 <= next_col < width:
                if not visited[next_row][next_col] and maze[next_row][next_col] == " ":
                    visited[next_row][next_col] = True
                    queue.append((next_row, next_col))
    return False

while True:
    attempts += 1
    if attempts > 100:
        print("yo code aint workin cuh")
        break
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
    for x, row in enumerate(maze):
        for y, cell in enumerate(row):
            if cell == " ":
                maze[x][y] = random.choices(["_", "|", "|o"], weights=weights1, k=1)[0]
            if y == 0 and x > 0 and x < 20:
                maze[x][y] = random.choices(["|-", "|"], weights=weights2, k=1)[0]
    maze[0][top_exit] = " "
    maze[20][bottom_exit] = " "
    if is_solvable(maze, bottom_exit):
        break
solver.goto(bottom_exit * 20 - 190, 190)

walls = Turtle()
walls.color("black")
walls.penup()
walls.speed(0)
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
        elif cell == "|o":
            walls.setheading(0)
            walls.backward(20)
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
screen.update()
screen.mainloop()
done()