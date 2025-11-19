def enter_number():
    numbers = []
    print("Enter numbers (type 'done' when finished):")

    while True:
        number = input("Number: ")

        if number == "done":
            break

        try:
            number = float(number)
            numbers.append(number)
        except ValueError:
            print("That was not a number.")

    if len(numbers) == 0:
        print("Your list is empty.")
        return enter_number()

    return numbers

def calculate(op="sum", *numbers):
    result = 1
    if op == "sum":
        result = sum(numbers)
    elif op == "average":
        result = sum(numbers) / len(numbers)
    elif op == "max":
        result = max(numbers)
    elif op == "min":
        result = min(numbers)
    elif op == "product":
        for num in numbers:
            result *= num
    return result

def main():
    print("Avaialable Operations: sum, average, max, min, product")

    op = input("Which operation would you like to perform? ")

    numbers = enter_number()

    print(f"Calculating {op} of: ", end="")
    for num in numbers:
        print(num, end=", ")

    result = calculate(op, *numbers)
    print(f"\nResult: {result}")

    again = input("Would you like to perform another calculation? (yes/no) ")
    if again == "no":
        print("Thank you for using the Flexible Calculator!")
    else:
        main()

print("Welcome to the Flexible Calculator!")
main()
