# JS, 1st, Random Numbers Notes=
import random

name = input("What is your character name?\n").strip()

#Generate Stat Options
stat_one = random.randint(1, 10) + random.randint(1, 10)
stat_two = random.randint(1, 10) + random.randint(1, 10)
stat_three = random.randint(1, 10) + random.randint(1, 10)
stat_four = random.randint(1, 10) + random.randint(1, 10)
stat_five = random.randint(1, 10) + random.randint(1, 10)
stat_six = random.randint(1, 10) + random.randint(1, 10)
stat_seven = random.randint(1, 10) + random.randint(1, 10)

#Telling user the stat choices
print(f"Your stat options are: {stat_one}, {stat_two}, {stat_three}, {stat_four}, {stat_five}, {stat_six}, {stat_seven}")

#Set Stats
strength = int(input("Which stat do you want as your strength: \n"))


print(f"{random.random()} is a random number 0 - 1.")
print(f"{random.randint(1,20)} is a random number 1 - 20.")