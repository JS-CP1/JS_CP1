from turtle import *
import threading
import time
player = Turtle()
player.left(90)
yvel = 0
xvel = 0
inp = ""

def get_input():
    global inp
    while True:
        inp = input()

thread = threading.Thread(target=get_input, daemon=True)
thread.start()

while True:
    # XVEL AND YVEL CHANGES
    if inp == "q":
        exit()
    if player.ycor() <= -250:
        yvel = 0
    if inp == "w" and player.ycor() <= -250:
        yvel = 25
    if inp == "a":
        xvel = -25
    if inp == "d":
        xvel = 25

    # MOVING
    if yvel >= 0:
        player.forward(yvel)
    else:
        player.backward(-yvel)
    x = player.xcor()
    if xvel >= 0:
        player.setx(x + xvel)
    else:
        player.setx(x - xvel)

    # RESET VARS
    inp = ""
    yvel -= 2