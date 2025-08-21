#  JS, 1st, Inputs and Outputs Notes

#5. What is an input
# A way for the code to get information

#6. What is the purpose of inputs
# Code isn't helpful if it doesn't use new information

name = input("What is your name: ").strip().capitalize()
# ^      ^           ^
# Save the input where it can be accessed again
# Use keyword "input" to create an input
# Inside parenthesis give user instructions

print("What is your name?")
name = input().strip().capitalize()

#Both instruction methods are fine just make sure you stick with one for all your code
print("Hello, ", name)