# JS, 1st, Lists Notes

import random

sibs = ["Joseph", "Gale", "Linda", "Isaac", "Gray"] #Brackets, commas, and proper data types

print(sibs[0])
#print(random.choice(sibs, weights=(20,20,20,20,20), k=5))
print(len(sibs))
print(sibs)
sibs[0] = "Joseph"
sibs[3:-1] = ["Isaac", "Gray"]
sibs.append("")
sibs.pop(4)
sibs.append(" ")
sibs.remove(" ")
#sibs.clear()
sibs.insert(5, " ")
sibs.extend([" 1", " 2"])
sibs.pop(5)
sibs.pop(5)
sibs.pop(5)
sibs.pop(5)
print(sibs)

tuples = ("thingy1", "thingy2", "thingy3") # Ordered, not changeable

fruit = {"blueberry", "blackberry", "raspberry", "apple"} # Unordered, changeable
print(fruit)