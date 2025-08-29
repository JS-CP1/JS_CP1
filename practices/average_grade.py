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
if average_grade <= 92: #2
    letter_grade = "A-"
if average_grade <= 89: #2
    letter_grade = "B+"
if average_grade <= 86: #3
    letter_grade = "B"
if average_grade <= 82: #2
    letter_grade = "B-"
if average_grade <= 79: #2
    letter_grade = "C+"
if average_grade <= 76: #3
    letter_grade = "C"
if average_grade <= 72: #2
    letter_grade = "C-"
if average_grade <= 69: #2
    letter_grade = "D+"
if average_grade <= 66: #3
    letter_grade = "D"
if average_grade <= 65: #1
    letter_grade = "F"
print(f"Your average grade is: {average_grade}, and your overall letter grade is a(n) {letter_grade}!!!!!!!")