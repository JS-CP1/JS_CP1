# JS, 1st, Squared Numbers Practice

#ASSIGNMENT
#Ask the user for 20 numbers
print("Input 20 numbers:")
nums = [input(f"{i+1}: ") for i in range(20)]
#Calculate the squares and put them in a list
squares = list(map(lambda i: (int(i)*int(i)), nums))
#Print the numbers
for num in nums:
    print(f"Number: {num}, Squared: {squares[nums.index(num)]}")



#GOLFED VERSION
#print('\n'.join(f'{i},{int(i)*int(i)}'for i in [input()for _ in range(20)])) 76 characters
#c is set to the user's 20 numbers
#it then prints the number, ", ", and the squared of that number