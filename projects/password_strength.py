#set strength to 0
strength = 0
#define a list with all lowercase letters (lowercases)
lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
#define a list with all uppercase letters (uppercases)
uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
#define a list with all special characters (specials)
specials = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "`", "~", "_", "-", "+", "=", "[", "]", "{", "}", "|", ":", ";", "<", ">", ",", ".", "?"]
#define a list with all numbers (numbers)
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
#define a list with all true or falses (truefalse)
truefalse = [False, False, False, False, False]
#ask user for a password
password = input("What is your chosen password?\n ").strip()
#if length of the password is greater than or equal to 8
if len(password) >= 8:
#    set first truefalse to True
    truefalse[0] = True
#check each item in lowercases for a lowercase letter
for char in lowercase:
#    check if char is in password
    if char in password:
#    set second truefalse to True
        truefalse[1] = True
#check each item in uppercases for an uppercase letter
for char in uppercase:
#    check if char is in password
    if char in password:
#    set third truefalse to True
        truefalse[2] = True
#check each item in specials for a special character
for char in specials:
#    check if char is in password
    if char in password:
#    set fourth truefalse to True
        truefalse[3] = True
#check each item in numbers for a number
for char in numbers:
#    check if char is in password
    if char in password:
#    set fifth truefalse to True
        truefalse[4] = True
#check for items in truefalse list
for item in truefalse:
#    check if item is True
    if item == True:
#    add 1 to strength
        strength += 1
#print all the things
print(f"Length (8+ characters): {truefalse[0]} \nContains uppercase: {truefalse[1]} \nContains lowercase: {truefalse[2]} \nContains numbers: {truefalse[3]} \nContains special characters: {truefalse[4]}\n Password Strength: {strength}!")