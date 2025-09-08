# JS, 1st, Calculator Practice

eq = input("What form of equation do you want to preform?\n add for addition\n min for subtraction\n mult for multiplication\n div for division\n intdiv for integer division\n mod for modulo\n exp for exponent\n").strip().lower()
while eq != "add" and eq != "sub" and eq != "mult" and eq != "div" and eq != "intdiv" and eq != "mod" and eq != "exp":
    eq = input("That was not a valid equation. What form of equation do you want to preform?\n add for addition\n min for subtraction\n mult for multiplication\n div for division\n intdiv for integer division\n mod for modulo\n exp for exponent\n").strip().lower()

if eq == "add":
    num1 = input("What is your first addend?\n")
    while num1 != int and num1 != float:
        num1 = input("That was not a valid number. What is your first addend?\n")
    num2 = input("What is your second addend?\n")
    while num2 != int and num2 != float:
        num2 = input("That was not a valid number. What is your second addend?\n")
    result = num1 + num2
elif eq == "sub":
    num1 = input("What is your subtahend?\n")
    while num1 != int and num1 != float:
        num1 = input("That was not a valid number. What is your subtahend?\n")
    num2 = input("What is your minuend?\n")
    result = num1 - num2
elif eq == "mult":
    num1 = input("What is your first multiplicand?\n")
    while num1 != int and num1 != float:
        num1 = input("That was not a valid number. What is your first multiplicand?\n")
    num2 = input("What is your second multiplicand?\n")
    result = num1 * num2
elif eq == "div":
    num1 = input("What is your dividend?\n")
    while num1 != int and num1 != float:
        num1 = input("That was not a valid number. What is your dividend?\n")
    num2 = input("What is your divisor?\n")
    result = num1 / num2
elif eq == "intdiv":
    num1 = input("What is your dividend?\n")
    while num1 != int and num1 != float:
        num1 = input("That was not a valid number. What is your dividend?\n")
    num2 = input("What is your divisor?\n")
    result = num1 // num2
elif eq == "mod":
    num1 = input("What is your dividend?\n")
    while num1 != int and num1 != float:
        num1 = input("That was not a valid number. What is your dividend?\n")
    num2 = input("What is your modulus?\n")
    result = num1 % num2
elif eq == "exp":
    num1 = input("What is your base?\n")
    while num1 != int and num1 != float:
        num1 = input("That was not a valid number. What is your base?\n")
    num2 = input("What is your exponent?\n")
    result = num1 ** num2

print(f"Your two numbers are {num1} and {num2}, and the result is {result:.2f}")