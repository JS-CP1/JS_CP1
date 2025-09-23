# JS, 1st, User Sign In Practice
info = []
output = False
for _ in range(int(input("How many accounts would you like to add?\n").strip())):
    info.append([input("Insert a username:\n").strip().lower(), input("Insert a password:\n").strip().lower()])
username, password = [input("What is your username?\n").strip().lower(), input("What is your password?\n").strip().lower()]
for inf in info:
    if inf[0] == username and inf[1] == password:
        output = True
if output == True:
    print("You logged in succesfully")
else:
    print("That was not correct")