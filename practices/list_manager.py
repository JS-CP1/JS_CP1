# JS, 1st, Shopping List Manager Practice
list = []
while True:
    action = input("Enter a item, Enter the same item again = remove from list, stop = stop program, print = print list.\n").title().strip()
    if action == "Stop": break
    elif action == "Print": print(*list)
    elif action + "," in list: list.pop(list.index(action + ","))
    else: list.append(action + ","), print("Added.")