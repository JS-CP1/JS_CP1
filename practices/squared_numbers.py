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
#print('\n'.join(f'{i},{int(i)**2}'for i in [input()for _ in range(20)])) 72 characters