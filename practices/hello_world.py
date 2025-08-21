#JS, 1st, Hello World Practice

name = input("What is your name? (Make sure to capitilize!)\n")
print("Hello, ", name)
returning = ["Anthony", "Jack", "Jacob", "Therizzler9000"]
admins = ["Ms. LaRose", "Joseph", "The Rock", "Pastry"]
if name in admins:
    print("Hello, admin")
elif name in returning:
    print("Welcome back, ", name)
elif name == "bob":
    print("Will you please take this seriously.")
elif name == "chicken jockey":
    print("That was soooo 6 months ago.")
elif name == "i am an enderpearl":
    print("FOR THE LAST TIME CAPITLIZE YOUR NAME")
elif name == "Pi":
    print("I mean at least you capitlized this time")
elif name == "Max Verstappen":
    ragebait = input("Since when is the last time you actually won a race. Like 2 days ago?\n")
    while ragebait == "nuh uh":
        ragebait == input("yah uh\n")
else:
    print("So your a first user? Welcome.")