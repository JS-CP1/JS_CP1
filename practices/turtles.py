from turtle import *
import random
running = True
teleport(500,300)
right(90)
forward(600)
t1,t2,t3,t4,t5=Turtle(),Turtle(),Turtle(),Turtle(),Turtle()
t1.teleport(-500,250)
t1.color("red")
t2.teleport(-500,125)
t2.color("orange")
t3.teleport(-500,0)
t3.color("yellow")
t4.teleport(-500,-125)
t4.color("green")
t5.teleport(-500,-250)
t5.color("blue")
while running==True:
    t1.forward(random.randint(10,25))
    t2.forward(random.randint(10,25))
    t3.forward(random.randint(10,25))
    t4.forward(random.randint(10,25))
    t5.forward(random.randint(10,25))
    if t1.xcor() > 500:
        print("Red wins!")
        break
    elif t2.xcor() > 500:
        print("Orange wins!")
        break
    elif t3.xcor() > 500:
        print("Yellow wins!")
        break
    elif t4.xcor() > 500:
        print("Green wins!")
        break
    elif t5.xcor() > 500:
        print("Blue wins!")
        break
done()