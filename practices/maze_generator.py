# JS, 1st, Maze Generator
from turtle import *
import random
maze = {
    0: [],
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: [],
    10: [],
    11: [],
    12: [],
    13: [],
    14: [],
    15: [],
    16: [],
    17: [],
    18: [],
    19: [],
    20: [],
}
for i in range(10):
    maze[0].append("-")
    maze[20].append("-")
maze[0][random.randint(1,9)] = " "
maze[20][random.randint(1,9)] = " "
for row in maze:
    if row == 0 or row == 20:
        continue
    if isinstance(row/2, int):
        