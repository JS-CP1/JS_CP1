# JS, 1st, Conditional Notes
import random

player = {
    "hp": 20,
    "attack": 5,
    "damage": 5,
    "defense": 5
}
monster = {
    "hp": 15,
    "attack": 3,
    "damage": 10,
    "defense": 2
}

hit_roll = random.randint(1,20)
    
if hit_roll == 20:
    print("you crit. you roll damage twice")
    damage_roll = random.randint(1,8) + random.randint(1,8) + player["damage"]
    print(f"You did {damage_roll-monster["defense"]}. ")
    monster["hp"] -= (damage_roll - monster["defense"])
elif hit_roll == 1:
    print("You rolled a cratical failure! Now the monster gets to attack you!")
    damage_roll = random.randint(1,12) + monster["damage"]
    print(f"You got hit for {damage_roll}.")
    player["hp"] -= (damage_roll - player["defense"])
    print(f"You have {player["hp"]} left.")
elif hit_roll + player["attack"] >= 12:
    print("You hit! Roll for damage!")
    damage_roll = random.randint(1,8) + player["damage"]
    if damage_roll > monster["defense"]:
        print(f"You did {damage_roll-monster["defense"]}. ")
        monster["hp"] -= (damage_roll - monster["defense"])
    else:
        print("You did no damage.")
else:
    print("You missed.")
print("you turn ova")

if monster["hp"] > 0:
    attack_roll = random.randint(1,20) + monster["attack"]
    