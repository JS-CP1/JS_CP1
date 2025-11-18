# JS, 1st, Flexible Calculator

def enter_number():
    numbers = []
    print("Enter numbers (type 'done' when finished):")

    while True:
        number = input("Number: ")

        if number == "done":
            break

        try:
            int(number)
        except ValueError:
            try:
                float(number)
            except ValueError:
                print("That was not a number.")
                continue
        
        numbers.append(number)

    if len(numbers) == 0:
        print("Your list is empty.")
        return enter_number()

    return numbers

def calculate(op, numbers):
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
    while op != "sum" and op != "average" and op != "max" and op != "min" and op != "product":
        op = input("That was not a valid operation. Which operation would you like to perform? ")

    numbers = enter_number()

    print(f"Calculating {op} of: ", end = "")
    for num in numbers:
        print(num, end = ", ")

    result = calculate(op, numbers)
    print(f"Result: {result}")

    again = input("Would you like to perform another calculation? (yes/no) ")
    if again == "no":
        print("Thank you for using the Flexible Calculator!")
    else:
        main()

print("Welcome to the Flexible Calculator!")
main()
