#JS, 1st, Idiot Proof Practice
name = input("What is your name?\n")
invalid_characters = "0123456789!@#$%^&*()-=_+[]{}|:;>.<,~`"
while any(char in invalid_characters for char in name):
    name = input("That is not a valid name. What is your name?\n")
while True:
    gpa_str = input("What is your gpa?\n")
    if gpa_str.replace('.', '', 1).isdigit() or (gpa_str.startswith('-') and gpa_str[1:].replace('.', '', 1).isdigit()):
        gpa = float(gpa_str)
        if 0.0 <= gpa <= 4.0:
            break
        else:
            print("Gpa must be between 0.0 and 4.0.")
    else:
        print("That was not a valid gpa. Please try again.")
phone = input("What is your phone number?\n").strip(" ").strip("-")
invalid_characters2 = "qwertyuiopasdfghjkllzxcvbnm,.;'!@#$%^&*()~`_-+={[]}|:><"
while len(phone) != 10 or any(char in invalid_characters2 for char in phone):
    phone = input("That's not a valid phone number. What is your phone number?\n").strip(" ").strip("-")
char_phone = list(phone)
char_phone.insert(3, ' ')
char_phone.insert(7, ' ')
phone_number = "".join(char_phone)
print(f"Hi {name.title()}, you have a gpa of {gpa} and your phone number is {phone_number}")