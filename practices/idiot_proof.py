#JS, 1st, Idiot Proof Practice
name = input("What is your name?\n")
try:
    while "1" in name or "2" in name or "3" in name or "4" in name or "5" in name or "6" in name or "7" in name or "8" in name or "9" in name or "0" in name:
        name = input("That is not a valid name. What is your name?\n")
except ValueError:
    pass
while True:
    gpa_str = input("What is your gpa?\n")
    try:
        gpa = float(gpa_str)
        if 0.0 <= gpa <= 4.0:
            break
        else:
            print("Gpa must be between 0.0 and 4.0.")
    except ValueError:
        print("That was not a valid gpa. Please try again.")
phone1 = []
gpa = round(float(gpa), 1)
phone = input("What is your phone number?\n").strip(" ").strip("-")
while len(phone) != 10:
    phone = input("That's not a valid phone number. What is your phone number?\n").strip(" ").strip("-")
phone1 = phone.split(:phone1[2])
print(phone1)
phone2 = phone1[0].split(phone1[0][0])

phone_number = phone1 + "-" + phone2 + "-"
print(phone_number)