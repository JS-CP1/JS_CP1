import random

player = {
    "wins": 0,
    "money": 500000,
    "car": ""
}
cars = {
    "ae86": {
        "name": "Toyota AE86 Trueno",
        "tires": 40000,
        "grip": 5,
        "hp": 130
    },
    "fd_rx7": {
        "name": "Mazda RX-7",
        "tires": 100000,
        "grip": 8,
        "hp": 200
    },
    "civic": {
        "name": "Toyota AE86 Trueno Hatchback",
        "tires": 150000,
        "grip": 7,
        "hp": 190
    },
    "nismo": {
        "name": "Toyota AE86 Trueno Hatchback",
        "tires": 500000,
        "grip": 25,
        "hp": 600
    }
}
enemies = {
    "takahashi": {
        "name": "Ryosuke Takahashi",
        "track": "Akagi"
    },
    "impact_blue": {
        "name": "Mako Sato and Sayuki",
        "track": "Usui Pass"
    },
    "bunta": {
        "name": "Bunta Fujiwara",
        "track": "Akina"
    }
}

def combat(turns, enemy, player, cars):
    order = 0 if random.choice(0, 1) == 0 else order = 1
    print(f"You have engaged in combat with {enemy["name"]}")
    while turns > 0:
        if order == 0:
            opt = input("You're approaching the turn... Would you like to review your options? (y/n) ")
            if opt == "yes" or opt == "y":
                print("Defend inside (di)\nDefend outside (do)\nGive position (g)\nFeint inside (fi)\nFeint outside (fo)\nFeint give (fg)")
            act = input("What would you like to do? ")
            while act != "di" and act != "do" and act != "g" and act != "fi" and act != "fo" and act != "fg":
                act = input("That was not a valid action. What would you like to do? ")
            # DOOOOO THE OUTCOME PLEAAASE I DONT WANT TO RIGHT NOW...
        else:
            opt = input("You're approaching the turn... Would you like to review your options? (y/n) ")
            if opt == "yes" or opt == "y":
                print("Take inside (ti)\nTake outside (to)\nStay (s)\nFeint inside (fi)\nFeint outside (fo)\nFeint stay (fs)")
            act = input("What would you like to do? ")
            while act != "ti" and act != "to" and act != "s" and act != "fi" and act != "fo" and act != "fs":
                act = input("That was not a valid action. What would you like to do? ")
            # DOOOOO THE OUTCOME PLEAAASE I DONT WANT TO RIGHT NOW...
        if cars[enemy["car"]]["hp"] > cars[player["car"]]["hp"] and order == 1:
            valid = True
        elif cars[enemy["car"]]["hp"] < cars[player["car"]]["hp"] and order == 0:
            valid = True
        else:
            valid = False
        if valid == True and order == 1 and input("Would you like to try and overtake in the straightaway (y/n) ") == "y" or valid == True and order == 0 and random.choice(0, 1) == 0:
            if order == 0:
                opt = input("You're approaching the straightaway with your opponent threatening an overtake... Would you like to review your options? (y/n) ")
                if opt == "yes" or opt == "y":
                    print("Defend left (l)\nDefend right (r)")
                act = input("What would you like to do? ")
                while act != "l" and act != "r":
                    act = input("That was not a valid action. What would you like to do? ")
                # DOOOOO THE OUTCOME PLEAAASE I DONT WANT TO RIGHT NOW...
            else:
                opt = input("You're approaching the straightaway... Would you like to review your options? (y/n) ")
                if opt == "yes" or opt == "y":
                    print("Take left (l)\nTake right (r)")
                act = input("What would you like to do? ")
                while act != "l" and act != "r":
                    act = input("That was not a valid action. What would you like to do? ")
                # DOOOOO THE OUTCOME PLEAAASE I DONT WANT TO RIGHT NOW...

def main():
    