# JS, 1st, Order Up!

#Define variables
order = []
total = 0
#Define dictionaries with each menu item
sides = {
    "French Fries": 3.99,
    "Salad": 4.50,
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
print("Mains:")
for main in mains:
    print(f" {main}: ${mains[main]:.2f}")
print("Sides:")
for side in sides:
    print(f" {side}: ${sides[side]:.2f}")
print("Drinks:")
for drink in drinks:
    print(f" {drink}: ${drinks[drink]:.2f}")
#Allow user to choose 1 main 2 sides and 1 drink
print("\n------- INPUTS -------")
action = input("Choose a main: ").title().strip()
while action not in mains:
    action = input("That is not a valid menu item. Choose a main: ").title()
order.append(action)
print("Added.")
for _ in range(2):
    action = input("Choose a side: ").title().strip()
    while action not in sides:
        action = input("That is not a valid menu item. Choose a side: ").title().strip()
    order.append(action)
    print("Added.")
action = input("Choose a drink: ").title().strip()
while action not in drinks:
    action = input("That is not a valid menu item. Choose a drink: ").title().strip()
order.append(action)
print("Added.")
#Print the final order
print("\n------- OUTPUT -------")
for item in order:
    if item in drinks:
        print(f" Your Drink: {item}")
for item in order:
    if item in mains:
        print(f" Your Main Course: {item}")
print(" Your Side Dishes:")
for item in order:
    if item in sides:
        print(f" {item}")
for item in order:
    if item in drinks:
        total += drinks[item]
    elif item in mains:
        total += mains[item]
    elif item in sides:
        total += sides[item]
print(f"Your Total Cost: ${total:.2f}")