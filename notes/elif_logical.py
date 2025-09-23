# JS, 1st, Elif and Logical Operators Notes

grade = 101

if grade > 100:
    print(f"You did {grade - 100}% of extra credit... Are you doing okay?")
elif grade == 100:
    print("Your grade is good.")
else:
    print(f"try harder you only have {grade}%")

username = "Joseph"
password = "1"

user = input("Enter you username\n")
pword = input("Enter you password\n")

if not user or not pword:
    print("Please enter a valid input")
elif user == username and pword == password:
    print("welcome")
elif user == username:
    print("password incorrect")
else:
    print("incorrect credentials")
