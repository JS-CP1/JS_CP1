# JS, 1st, Order Up!
#Define each dictionary with their items and values
order = []
sides = {
    "French Fries": 3.99,
    "Side Salad": 4.50,
    "Garlic Bread": 3.50,
    "Mashed Potatoes": 4.25
}
mains = {
    "Grilled Salmon": 18.99,
    "Steak Frites": 24.50,
    "Vegetarian Pasta": 15.99,
    "Chicken Tikka Masala": 17.50
}
drinks = {
    "Coca-Cola": 2.50,
    "Iced Tea": 2.99,
    "Sparkling Water": 3.00,
    "Fresh Orange Juice": 4.50
}
#Print the menu
print("------- MENU -------\nSides:")
for side in sides:
    print(f" {side}: ${sides[side]:.2f}")
print("Mains:")
for main in mains:
    print(f" {main}: ${mains[main]:.2f}")
print("Drinks:")
for drink in drinks:
    print(f" {drink}: ${drinks[drink]:.2f}")

# Create an infinite loop that lets the user choose 
while True:
    if i == 0:
        action = input("1: Add an item\n2:").title().strip()
    else:
        action = input("Please input your action.\n ").title().strip()
    i = 1
    if action == "Stop" or action == "Exit":
        print("See ya!")
        break
    elif action == "Print":
        print("Your order:")
        for item in order:
            if item in sides:
                print(f" {item}: {sides[item]:.2f}")
            elif item in mains:
                print(f" {item}: {mains[item]:.2f}")
            elif item in drinks:
                print(f" {item}: {drinks[item]:.2f}")
    elif action + "," in order:
        order.pop(order.index(action + ","))
        print("Item Removed.")
    elif action == "Done":
        mark = input("Which item would you like to check off?\n ").title().strip()
        while mark + "," not in order:
            mark = input("That was not a valid item, try again.\n ").title().strip()
        for index, item in enumerate(order):
            if item == mark + ",":
                order[index] = mark + " ✔,"
    else: 
        order.append(action + ",")
        print("Added.")