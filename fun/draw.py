from turtle import *

CELL_SIZE = 50
GRID_SIZE = 30
WINDOW_SIZE = CELL_SIZE * GRID_SIZE

screen = Screen()
screen.setup(WINDOW_SIZE, WINDOW_SIZE)
screen.tracer(0)

draw = Turtle()
draw.speed(0)
draw.penup()

drawn = [["" for _ in range(CELL_SIZE)] for _ in range(CELL_SIZE)]

def draw_square(row, col, fill):
    half_window = WINDOW_SIZE / 2
    x = -half_window + col * CELL_SIZE
    y = half_window - row * CELL_SIZE
    draw.goto(x, y)
    draw.setheading(0)

    if fill == True:
        color = "black"
    else:
        color = "white"
    draw.fillcolor(color)
    draw.pencolor(color)
    draw.begin_fill()
    draw.pendown()
    for _ in range(4):
        draw.forward(CELL_SIZE)
        draw.right(90)
    draw.penup()
    draw.end_fill()

def draw_base(x, y):
    half_window = WINDOW_SIZE / 2
    col = int((x + half_window) // CELL_SIZE)
    row = int((half_window - y) // CELL_SIZE)
    if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
        if drawn[row][col] == "X":
            drawn[row][col] = ""
            draw_square(row, col, False)
        else:
            drawn[row][col] = "X"
            draw_square(row, col, True)
    screen.update()

def drag(x, y):
    half_window = WINDOW_SIZE / 2
    col = int((x + half_window) // CELL_SIZE)
    row = int((half_window - y) // CELL_SIZE)
    if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
        if drawn[row][col] == "X":
            drawn[row][col] = ""
            draw_square(row, col, True)
        else:
            drawn[row][col] = "X"
            draw_square(row, col, True)
    screen.update()


screen.onclick(draw_base)
draw.ondrag(drag)
done()
