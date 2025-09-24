# JS, 1st, Letter Grade Practice
while True:
    percent = int(input("What is your percent grade?\n").strip().strip("%"))
    if percent >= 93:
        grade = "A"
    elif percent >= 90:
        grade = "A-"
    elif percent >= 87:
        grade = "B+"
    elif percent >= 90:
        grade = "B"
    elif percent >= 83:
        grade = "B-"
    elif percent >= 80:
        grade = "C+"
    elif percent >= 77:
        grade = "C"
    elif percent >= 73:
        grade = "C-"
    elif percent >= 70:
        grade = "D+"
    elif percent >= 67:
        grade = "D"
    elif percent >= 65:
        grade = "D-"
    else:
        grade = "F"
    print(f'You have a(n) {grade}.')
    again = input("Would you like to check another?\n")
    if again != "yes": 
        break