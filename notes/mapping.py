# JS, 1st, Mapping Notes

numbers = [8432782435, 237549832654, 254376345, 2348593845]
"""
new_nums = []

for number in numbers:
    new_nums.append(number/3)

print(new_nums)

def divide(num):
    return num/3
"""
new_nums = map(lambda num: num/3, numbers)
for num in new_nums:
    print(num)