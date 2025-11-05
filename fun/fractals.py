from turtle import *

screen = Screen()
screen.setup(500, 500)
screen.title("Fractals")
screen.tracer(0)

draw = Turtle()
draw.speed(0)
draw.penup()
draw.hideturtle()

drawn = [["" for _ in range(10)] for _ in range(10)]

def draw_square(row, col, fill):
    x = -250 + col * 50
    y = 250 - row * 50
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
        draw.forward(50)
        draw.right(90)
    draw.penup()
    draw.end_fill()

def draw_base(x, y):
    col = int((x + 250) // 50)
    row = int((250 - y) // 50)
    if 0 <= row < 10 and 0 <= col < 10:
        if drawn[row][col] == "X":
            drawn[row][col] = ""
            draw_square(row, col, False)
        else:
            drawn[row][col] = "X"
            draw_square(row, col, True)
    screen.update()

screen.onclick(draw_base)
done()
