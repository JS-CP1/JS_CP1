# JS, 1st, Password Strength Checker
length = False
capital = False
lowercase = False
number = False
special = False
score = 0
password = input("Please enter a password.\n").strip()
while password == False:
    password = input("Please enter a valid password.\n").strip()
if len(password) >= 8:
    length = True
    score += 1
capitals = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
for letter in capitals:
    if letter in password:
        capital = True
        score += 1
    if letter.lower() in password:
        lowercase = True
        score += 1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
for num in numbers:
    if str(num) in password:
        number = True
        score += 1
specials = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "`", "~", "_", "-", "+", "=", "[", "]", "{", "}", "|", ":", ";", "<", ">", ",", ".", "?"]
for spec in specials:
    if spec in password:
        special = True
        score += 1
    