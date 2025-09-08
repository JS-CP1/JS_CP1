# JS, 1st, Calculator Practice

eq_nums = ["first addend", "second addend", "subtahend", "minuend", "first multiplicand", "second multiplicand", "dividend", "divisor", "dividend", "divisor", "dividend", "modulo", "base", "exponent"]
eq = input("What form of equation do you want to preform?\n add for addition\n min for subtraction\n mult for multiplication\n div for division\n intdiv for integer division\n mod for modulo\n exp for exponent\n").strip().lower()
while eq != "add" and eq != "sub" and eq != "mult" and eq != "div" and eq != "intdiv" and eq != "mod" and eq != "exp":
    eq = input("That was not a valid equation. What form of equation do you want to preform?\n add for addition\n min for subtraction\n mult for multiplication\n div for division\n intdiv for integer division\n mod for modulo\n exp for exponent\n").strip().lower()
num1 = 0
num2 = 0

def find_num_type(num_type):
    if num_type == "add":
        num_num1 = 0
        num_num2 = 1
    elif num_type == "sub":
        num_num1 = 2
        num_num2 = 3
    elif num_type == "mult":
        num_num1 = 4
        num_num2 = 5
    elif num_type == "div":
        num_num1 = 6
        num_num2 = 7
    elif num_type == "intdiv":
        num_num1 = 8
        num_num2 = 9
    elif num_type == "mod":
        num_num1 = 10
        num_num2 = 11
    elif num_type == "exp":
        num_num1 = 12
        num_num2 = 13
    num1 = float(input(f"What is your {eq_nums[num_num1]}?\n"))
    num2 = float(input(f"What is your {eq_nums[num_num2]}?\n"))
    return num1, num2

if eq == "add":
    num1, num2 = find_num_type(eq)
    result = num1 + num2
elif eq == "sub":
    num1, num2 = find_num_type(eq)
    result = num1 - num2
elif eq == "mult":
    num1, num2 = find_num_type(eq)
    result = num1 * num2
elif eq == "div":
    num1, num2 = find_num_type(eq)
    result = num1 / num2
elif eq == "intdiv":
    num1, num2 = find_num_type(eq)
    result = num1 // num2
elif eq == "mod":
    num1, num2 = find_num_type(eq)
    result = num1 % num2
elif eq == "exp":
    num1, num2 = find_num_type(eq)
    result = num1 ** num2

print(f"Your two numbers are {num1} and {num2}, and the result is {result:.2f}")