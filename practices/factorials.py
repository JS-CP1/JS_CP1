# JS, 1st, Factorials 

#welcome the user and give instructions
print("Welcome user! Use this program to calculate the factorial of any valid number. Soon you will be given the option to choose a number. Please make sure this input is a positive whole number.")

#define function with argument
def function(argument):
    # ADDITION BY CODER: define total
    total = 1
    #for i in range(1, argument) ADDITION BY CODER + 1
    for i in range(1, argument + 1):
        #make total times i ADDITION BY CODER: *=
        total *= i
    #return the total
    return total

#while True statement
while True:
    #get user input and store as a variable
    user = input("Please input a number: ")
    #Check if valid
    try:
        if "-" not in user:
            user = int(user)
            valid = True
        else:
            valid = False
    except:
        valid = False
    #if not valid
    if valid == False:
        #print try again
        print("Try again; that was not a valid number.")
        #continue
        continue
    #if valid
    if valid == True:
        #break
        break

#print the input and function output
print(f"Your input: {user}, Your output: {function(argument= user)}")