# JS, 1st, Multiplication Table
length = int(input("How big?\n ").strip())
list = []
for len in range(length):
    list.append(len+1)
for x in list:
    for y in list:
        print(x*y,end = " ")
    print()