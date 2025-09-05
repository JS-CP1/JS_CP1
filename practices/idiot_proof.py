#JS, 1st, Idiot Proof Practice
while True:
    name = input("What is your name?\n")
    try:
        name = str(name)
        if name == str:
            break
    except ValueError:
        print("That was not a valid name. Please try again.")
while True:
    gpa_str = input("What is your gpa?\n")
    try:
        gpa = float(gpa_str)
        if 0.0 <= gpa <= 4.0:
            break
        else:
            print("gpa must be between 0.0 and 4.0.")
    except ValueError:
        print("That was not a valid gpa. Please try again.")
gpa = round(float(gpa), 1)
phone = input("What is your phone number?\n").strip(" ").strip("-")
while len(phone) != 10:
    phone = input("That's not a valid phone number. What is your phone number?\n").strip(" ").strip("-")
phone1, phone2 = phone.split(phone[2])
phone2, phone3 = phone2.split(phone2[2])
phone_number = phone1 + "-" + phone2 + "-" + phone3
print(phone_number)