from turtle import *

screen = Screen()
screen.setup(500, 500)
screen.title("Fractals")

draw = Turtle()
draw.speed(0)
draw.penup()
draw.hideturtle()

drawn = [["" for _ in range(10)] for _ in range(10)]

for i in range(11):
    draw.penup()
    draw.goto(-250 + i * 50, 250)
    draw.setheading(270)
    draw.pendown()
    draw.forward(10 * 50)
for i in range(11):
    draw.penup()
    draw.goto(-250, 250 - i * 50)
    draw.setheading(0)
    draw.pendown()
    draw.forward(10 * 50)
draw.penup()

def draw_square(row, col, fill):
    x = -250 + col * 50
    y = 250 - row * 50
    draw.goto(x, y)
    draw.setheading(0)

    color = "black" if fill else "white"
    draw.fillcolor(color)
    draw.pencolor("black")

    draw.begin_fill()
    for _ in range(4):
        draw.forward(50)
        draw.right(90)
    draw.end_fill()

def draw_base(x, y):
    col = int((x + 250) // 50)
    row = int((250 - y) // 50)
    if 0 <= row < 10 and 0 <= col < 10:
        drawn[row][col] = "" if drawn[row][col] == "X" else "X"
        draw_square(row, col, fill=(drawn[row][col] == "X"))

screen.onclick(draw_base)
done()
