# Create a list with all the characters in the alphabet
chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# Ask the user whether they would like to encode or decode
choice = int(input("Would you like to encode (1) or decode (2)?\n "))
# Ask the user for their message
message = input("What is your message?\n ")
# Ask the user how many times they want to shift the characters
shift = int(input("How much would you like to shift by?\n "))
# Define a function that encode and decodes and takes in the previous variables as parameters
def encode_decode(chars, choice, message, shift):
    # Create a list for the letters of the new word
    new = []
    # Loop through every character in the message
    for i in message:
        # Check if the character is a space
        if i == " ":
            # Append a space into the new list
            new.append(" ")
        # Check if the character is capitilized
        elif i.isupper():
            # Loop through all the letters in the alpahabet
            for index, x in enumerate(chars):
                # Capitilize the letter
                x = x.upper()
                # Check if the letter in the alphabet is equal to the letter in the alphabet
                if i == x:
                    # Check if the user chose to encode
                    if choice == 1:
                        # Check if the shifted value is greater than 26
                        if index + shift > 26:
                            # Subtract 26 from index
                            index -= 26
                        # Append the new value to the new word list
                        new.append(chars[index+shift])
                    # Check if the user chose to decode
                    else:
                        # Check if the shifted value is less than 0
                        if index - shift < 0:
                            # Add 26 to index
                            index += 26
                        #Append the new value to the new word list
                        new.append(chars[index-shift])
        # For every character that is not capitilized
        else:
            # Loop through every value in the alphabet 
            for index, x in enumerate(chars):
                # Check if the letter from the alphabet and the letter from the message are the same
                if i == x:
                    # Check if the user chose to encode
                    if choice == 1:
                        # Check if the shifted value is greater than 26
                        if index + shift > 26:
                            # Subtract 26 from index
                            index -= 26
                        # Append the new value to the new word list
                        new.append(chars[index+shift])
                    # Check if the user chose to decode
                    else:
                        # Checck if the shifted value is less than 0
                        if index - shift < 0:
                            # Add 26 to index
                            index += 26
                        # Append the new value to the new word list
                        new.append(chars[index-shift])
    # Return the final word
    return new
# Call the function
new = encode_decode(chars, choice, message, shift)
#Print the final word
print(f"Your encoded message: ")
for i in new:
    print(i, end="")
