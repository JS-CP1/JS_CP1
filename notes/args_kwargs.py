# JS, 1st, *args and **kwargs notes
"""
def hello(name = "tia", age = 23):
    return f"hello {name}"
print(hello("treyson", 19))
hello()

def hello(*names, **kwargs):
    print(type(names))
    print(kwargs)
    for n in names:
        print(f"Hello {n} {kwargs['last_name']}")
hello("Alex", "Katie", "Andrew", "Vienna", "Tia", "Treyson", "Xavier", "Jake", last_name = "Stratford", dad = "ur mom", num_cats = 0)

def full_name(age, **names):
    if 'middle' in names.keys():
        return f"{names['first']} {names['middle']} {names['last']} is {age}"
    else:
        return f"{names['first']} {names['last']} is {age}"

print(full_name(age = "???", first="Koro", last="Sensei"))
"""

def summary(**story):
    sum = ""
    if "name" in story.keys():
        sum += f"{story['name']} is the main character of this story.\n"
    if "place" in story.keys():
        sum += f"The story take place in {story['place']}.\n"
    if "conflict" in story.keys():
        sum += f"The problem is {story['conflict']}.\n"
    return sum
print(summary(name = "dumpster", place = "kwarg", conflict = "brotherly feud"))