#Import turtle and random
from turtle import *
import random
#Create finish line
goto(500,300)
right(90)
forward(600)
#Create 5 turtles
t = [Turtle() for i in range(5)]
#Set turtle stats (position, color, shape)
t[0].goto(-500,250)
t[0].color("red")
t[0].shape("turtle")
t[1].goto(-500,125)
t[1].color("orange")
t[1].shape("turtle")
t[2].goto(-500,0)
t[2].color("yellow")
t[2].shape("turtle")
t[3].goto(-500,-125)
t[3].color("green")
t[3].shape("turtle")
t[4].goto(-500,-250)
t[4].color("blue")
t[4].shape("turtle")
#Loop until someone wins
while True:
    for turtle in t:
        #Move every turtle a random amount of steps
        turtle.forward(random.randint(10,25))
        #Check if x coordinant is greater than finish line
        if turtle.xcor() > 500:
            #Print the turtle that won
            print(f"{(turtle.color()[1]).title()} Turtle Wins!")
            #Quit
            exit()