from turtle import *
import random
teleport(500,300)
right(90)
forward(600)
t = [Turtle() for i in range(5)]
t[0].teleport(-500,250)
t[0].color("red")
t[0].shape("turtle")
t[1].teleport(-500,125)
t[1].color("orange")
t[1].shape("turtle")
t[2].teleport(-500,0)
t[2].color("yellow")
t[2].shape("turtle")
t[3].teleport(-500,-125)
t[3].color("green")
t[3].shape("turtle")
t[4].teleport(-500,-250)
t[4].color("blue")
t[4].shape("turtle")
while True:
    for turtle in t:
        turtle.forward(random.randint(10,25))
        if turtle.xcor() > 500:
            print(f"{turtle.color()[1]} Turtle Wins!")
            exit()