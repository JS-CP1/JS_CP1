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
    "Coke": 2.50,
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

action = input("Choose a main: ").capitalize().strip()
while action not in mains:
    action = input("That is not a valid menu item. Choose a main: ").capitalize().strip()
order.append(action)
print("Added.")
action = input("Choose a sides: ").capitalize().strip()
while action not in sides:
    action = input("That is not a valid menu item. Choose a side: ").capitalize().strip()
order.append(action)
print("Added.")
action = input("Choose a sides: ").capitalize().strip()
while action not in sides:
    action = input("That is not a valid menu item. Choose a side: ").capitalize().strip()
order.append(action)
print("Added.")
# Create an infinite loop that lets the user choose 
i = 0
while True:
    if i == 0:
        action = input("1: Add an item\n2: Remove an item\n3: Stop or exit\n4: Print order").strip()
    else:
        action = input("Please input your action.\n ").strip()
    i = 1
    if action == 3:
        print("See ya!")
        break
    elif action == 4:
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
    elif action == 1: 
        order.append(action)
        print("Added.")