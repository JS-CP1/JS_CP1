# JS, 1st, Flexible Calculator

def enter_number():
    numbers = []
    number = input("Enter numbers (type 'done' when finished):\nNumber: ")
    while number != "done":
        if isinstance(number, (int, float)):
            numbers.append(number)
        else:
            number = input("That was not a number")
        number = input("Number: ")
    if len(numbers) == 0:
        print("Your list is empty.")
        enter_number()
print("Welcome to the Flexible Calculator!\nAvaialable Operations: sum, average, max, min, product")