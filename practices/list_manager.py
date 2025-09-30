# JS, 1st, Shopping List Manager Practice
list = []
i = 0
i = 0
while True:
    if i == 0:
        action = input("Enter a item\nEnter the same item again = remove from list\nstop/exit = stop program\nprint = print list.\ndone = mark something finished\n ").title().strip()
    else:
        action = input("Please input your action.\n ").title().strip()
    i = 1
    if action == "Stop" or action == "Exit":
        print("See ya!")
        break
    elif action == "Print": 
        print(*list)
    elif action + "," in list:
    elif action + "," in list:
        list.pop(list.index(action + ","))
        print("Item Removed.")
    elif action == "Done":
        mark = input("Which item would you like to check off?\n ").title().strip()
        while mark + "," not in list:
            mark = input("That was not a valid item, try again.\n ").title().strip()
        for index, item in enumerate(list):
            if item == mark + ",":
                list[index] = mark + " ✔,"
    else: 
        list.append(action + ",")
        print("Added.")