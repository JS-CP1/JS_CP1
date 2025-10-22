chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
choice = int(input("Would you like to encode (1) or decode (2)?\n "))
message = input("What is your message?\n ")
shift = int(input("How much would you like to shift by?\n "))

def encode_decode(chars, choice, message, shift):
    new = []
    for i in message:
        if i == " ":
            new.append(" ")
        elif i.isupper():
            for index, x in enumerate(chars):
                x = x.upper()
                if i == x:
                    if choice == 1:
                        if index + shift > 26:
                            index -= 26
                        new.append(chars[index+shift])
                        if index - shift < 0:
                            index += 26
                    else:
                        new.append(chars[index-shift])
        else:
            for index, x in enumerate(chars):
                if i == x:
                    if choice == 1:
                        if index + shift > 26:
                            index -= 26
                        new.append(chars[index+shift])
                    else:
                        if index - shift < 0:
                            index += 26
                        new.append(chars[index-shift])
    return new
    
new = encode_decode(chars, choice, message, shift)

print(f"Your encoded message: ")
for i in new:
    print(i, end="")
