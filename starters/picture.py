from turtle import *
def draw_branch(length):
    if length > 5:
        for _ in range(3):
            t.forward(length)
            draw_branch(length/3)
            t.backward(length)
            t.right(60)

t = Turtle()
t.speed(0)
t.color("light blue")
t.penup()
t.goto(0,0)
t.pendown()

for i in range(6):
    draw_branch(100)
    t.right(60)

t.hideturtle()