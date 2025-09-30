# JS, 1st, Shopping List Manager Practice
list = []
i = 0
while True:
    if i == 0:
        action = input("Enter a item\nEnter the same item again = remove from list\nstop/exit = stop program\nprint = print list.\n ").title().strip()
    else:
        action = input("Please input your action.\n ").title().strip()
    i = 1
    if action == "Stop" or action == "Exit":
        print("See ya!")
        break
    elif action == "Print": 
        print(*list)
    elif action + "," in list:
        list.pop(list.index(action + ","))
        print("Item Removed.")
    else: 
        list.append(action + ",")
        print("Added.")