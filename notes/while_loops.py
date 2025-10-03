# JS, 1st, While Loop Notes
import time
import random
# Infinite Loop
num = 1
while num <= 20:
    print(num)
    time.sleep(1/60)
    num += 1 #Prevents an infinite loop
else:
    print("The condition was met.")
goose = random.randint(1,20)
count = 0

while count != goose: #You must include a break in this:
    count += 1
    print("duck")
    """if count == goose;
        break
    else:"""
    if count == 6:
        break
else:
    print("Goose")


i = 0
while i < 20:
    if i == 10:
        print("i is 10")
        continue
    else:
        print(f"{i} iteration of the loop")
    i += 1

print("The code is done!")