# JS, 1st, Combat Program
import random
def user_turn():
    action = input("What would you like to do?\n ")
    while action != "a" and action != "d":
        action = input("That was not a valid input. What would you like to do? (a, d)\n ")
    return action
def boss_turn():
    action = "a"
    return action
user_stats = {
    "melee":{
        "hp": 200,
        "def": 10,
        "at": 35,
        "hit": .8,
        "hurt": .8
    },
    "ranger":{
        "hp": 100,
        "def": 2,
        "at": 15,
        "hit": .5,
        "hurt": .1
    },
    "mage":{
        "hp": 150,
        "def": 5,
        "at": 25,
        "hit": .8,
        "hurt": .5
    },
    "summoner":{
        "hp": 20,
        "def": 0,
        "at": 20,
        "hit": 1,
        "hurt": .05
    }
}
user = {
    "hp": 0,
    "def": 0,
    "at": 0,
    "hit": 0,
    "hurt": 0
}
boss_stats = {
    "providence": {
        "hp": 250,
        "at": 15
    },
    "dog": {
        "hp": 500,
        "at": 30
    },
    "yharon": {
        "hp": 1000,
        "at": 50
    },
    "calamitas": {
        "hp": 2500,
        "at": 100
    }
}
boss = {
    "hp": 0,
    "at": 0
}
combat = True
type = input("What class would you like to play? (Melee, Ranger, Mage, Summoner)\n ").lower().strip()
while type != "melee" and type != "ranger" and type != "mage" and type != "summoner":
    type = input("That was not a valid class. What class would you like to play? (Melee, Ranger, Mage, Summoner)\n ")
for i in user:
    user[i] = user_stats[type][i]
boss_choice = input("What boss would you like to fight? (Providence, DOG, Yharon, Calamitas)\n ").lower().strip()
while boss_choice != "providence" and boss_choice != "dog" and boss_choice != "yharon" and boss_choice != "calamitas":
    boss_choice = input("That was not a valid boss. What boss would you like to fight? (Providence, DOG, Yharon, Calamitas)\n ")
for x in boss:
    boss[x] = boss_stats[boss_choice][x]
print(f"You have chosen the {type} class, and are fighting {boss}.\nWhen you are given the option, press (a) to attack and (d) to dodge")
if random.randint(0,1) == 1:
    turn = "user"
else:
    turn = "boss"
while combat == True:
    if turn == "user":
        action = user_turn()
    else:
        action = boss_turn()
    if action == "a":
        if turn == "user":
            if random.random() < user["hit"]:
                boss["hp"] = boss["hp"] - user["at"]
                print(f"You did {user["at"]} damage.")
            else:
                print("You missed...")
        else:
            if random.random() < user["hurt"]:
                user["hp"] = (user["hp"] + user["def"]) - boss["at"]
                print(f"You took {boss["at"] - user["def"]} damage.")
            else:
                print("The enemy attacks, but you dodged!")
    else:
        print("Nothing happens...")
        continue
    print(f"Your hp: {user["hp"]}\nBoss hp: {boss["hp"]}")
    if turn == "user":
        turn = "boss"
    else:
        turn = "user"
    if user["hp"] > 0 and boss["hp"] > 0:
        continue
    if user["hp"] > 0:
        print("You Won!")
        exit()
    else:
        print("You Lost...")
        exit()