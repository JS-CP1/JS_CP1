# JS, 1st, Letter Grade Practice
while True:
    percent = int(input("What is your percent grade?\n").strip().strip("$"))
    print(f'You have a(n) {"A" if percent >= 93 else "A-" if percent >= 90 else "B+" if percent >= 87 else "B" if percent >= 83 else "B-" if percent >= 80 else "C+" if percent >= 77 else "C" if percent >= 73 else "C-" if percent >= 70 else "D+" if percent >= 67 else "D" if percent >= 65 else "F"}.',)
    again = input("Would you like to check another?\n")
    if again == "yes": break