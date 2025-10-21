# JS, 1st, Fuction Notes
#Set Vars
health = 100
monster_health = 100
player_health = 100
#Def Functions
def damage(amount, turn):
    if turn == "player":
        return monster_health - amount, player_health
    else:
        return monster_health, player_health - amount
    

monster_health, player_health = damage(10, "player")
print("Monster Health:", monster_health)
print("Player Health:", player_health)

def add(x, y):
    return x + y

def initials(name):
    names = name.split(" ")
    initials = ""
    for name in names:
        initials += name[0]
    return initials

total = add(5,5)
print(total)
print(f"10 + 72 = {add(10,72)}")
x = 0
while x < add(3,9):
    print("Duck")
    x += 1
print("Goose!")
print(initials("Joseph Stratford"))