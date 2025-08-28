# JS, 1st, Average Grades

classes = int(input("How many classes do you have?\n"))
class_grades = []
letter_grade = ""
average_grade = 0
while classes > 0:
    grade = float(input("What is the grade of one of your classes\n"))
    class_grades.append(grade)
    classes -= 1
for percent in class_grades:
    average_grade += percent
average_grade = round(average_grade/len(class_grades))
if average_grade >= 93:
    letter_grade = "A"
elif average_grade >= 90 and average_grade <= 92:
    letter_grade = "A-"
elif average_grade >= 87 and average_grade <= 89:
    letter_grade = "B+"
elif average_grade >= 83 and average_grade <= 86:
    letter_grade = "B"
elif average_grade >= 80 and average_grade <= 82:
    letter_grade = "B-"
elif average_grade >= 77 and average_grade <= 79:
    letter_grade = "C+"
elif average_grade >= 73 and average_grade <= 76:
    letter_grade = "C"
elif average_grade >= 70 and average_grade <= 72:
    letter_grade = "C-"
elif average_grade >= 67 and average_grade <= 69:
    letter_grade = "D+"
elif average_grade >= 65 and average_grade <= 66:
    letter_grade = "D"
elif average_grade <= 65:
    letter_grade = "F"
print(f"Your average grade is: {average_grade}, and your letter grade is a(n) {letter_grade}!")