# JS, 1st, For Loop Notes
import time

nums = [1,2,3,4,5,6,7,8,9]

for num in nums:
    num /= 2
    if num > 500:
        print(f"{num} is only half of {num*2}. It is a large number")
    else:
        print(num)
print("heeeelllooo woooooooorldd")
for num in range(10, 0, -1):
    print(num)
    time.sleep(1)
print("GO!!!!!")
