#JS, 1st, String Method Notes

subject = "computer programming 1"

print(subject.upper())
print(subject.center(100))

# Stupid/idiot Proofing inputs
#color = input("What is your favorite color?\n").lower().strip()
# lower() => lowercases all characters
# upper() => uppercases all characters
# capitalize() => capitilize first letter
# title() => capitilizes first letter of every word
#full_name = input("What is your full name?\n").strip().title()
#print(full_name + " fav colo is " + color)
#print("{full_name} fav colo is {color}".format(full_name = full_name, color = color))
#f-string
#print(f"{full_name} fav colo is {color}")

pi = "3.1414592653589793238462643832795028841971693993751058209749445923078164062862089986280348253421170"
#print(f"we all know pi is equal to {pi:.3f}")
#print(pi.isdecimal())

sentence = "The quick brown fox jumps over the lazy dog."
word = "jumps"
print(sentence.find(word))
start = sentence.index(word)
length = len(word)
print(sentence[start:start+length])
print(sentence.replace(word, "swims"))
print(sentence)