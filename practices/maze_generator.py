# JS, 1st, Maze Generator
#Import turtle and random
from turtle import *
import random

#Setup the screen
screen = Screen()
screen.setup(500,500)
screen.title("Maze Generator")
screen.tracer(0)

#Create weight for randomly generated blocks
weights = [10,30]

#Create exits
top_exit = random.randint(1,9)
bottom_exit = random.randint(1,9)

#Create a function that solves the maze
def is_solvable(maze, exit_col):
    #Find dimensions of the maze
    height = len(maze)
    width = len(maze[0])
    #Set a variable for all visited cells
    visited = [[False] * width for _ in range(height)]
    #Set a variable for the next cell
    queue = [(0, exit_col)]
    #Set visited 
    visited[0][exit_col] = True
    #Loop while the queue is not empty
    while queue:
        row, col = queue.pop(0)
        #If out end function and return True
        if row == height - 1:
            return True
        #Loop through all possible directions
        for row_change, col_change in [(-1,0),(1,0),(0,-1),(0,1)]:
            #Set two variables for direction
            next_row = row + row_change
            next_col = col + col_change
            #If next is in maze
            if 0 <= next_row < height and 0 <= next_col < width:
                #Check if it's not at the exit and set the next move
                if not visited[next_row][next_col] and maze[next_row][next_col] == " ":
                    visited[next_row][next_col] = True
                    queue.append((next_row, next_col))
    return False
#Loop until a valid maze is reached.
attempts = 0
while True:
    #Create a cap so it doesn't break
    attempts += 1
    if attempts > 9999:
        break
    #Define the blank maze
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
    #Go through every blank box in map and set it to a random wall
    for x, row in enumerate(maze):
        for y, cell in enumerate(row):
            if cell == " ":
                maze[x][y] = random.choice(["_", "|", "|o"])
            if y == 0 and x > 0 and x < 20:
                maze[x][y] = random.choices(["|-", "|"], weights = weights, k = 1)[0]
    #Set the exits
    maze[0][top_exit] = " "
    maze[20][bottom_exit] = " "
    #If the maze is solvable break out of the loop
    if is_solvable(maze, bottom_exit):
        break
#Create a walls turtle
walls = Turtle()
walls.color("black")
walls.penup()
walls.speed(0)
#Loop through every cell in the maze
for r, row in enumerate(maze):
    for col, cell in enumerate(row):
        walls.penup()
        #Go to each cell
        walls.goto(col * 20 - 200, r * 20 - 200)
        #Draw each specific wall depending on what cell is equal to
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
#Update screen and keep it open
walls.hideturtle()
screen.update()
screen.mainloop()