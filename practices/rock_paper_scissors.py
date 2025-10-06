# JS, 1st, Rock Paper Scissors
import random as rand
while True:
    computer_choice = rand.choice(["rock", "paper", "scissors"])
    action = input("What would you like to throw? (Rock, Paper, Scissors)\n").lower().strip()
    if action == "r":
        action = "rock"
    elif action == "p":
        action = "paper"
    elif action == "s":
        action = "scissors"
    while action != "rock" and action != "paper" and action != "scissors":
        action = input("That was not a valid option, try again.\n").lower().strip()
    print(f"You did: {action.capitalize()}, Computer did: {computer_choice.capitalize()}.")
    if action == computer_choice:
        print("You Tied.")
    elif action == "rock" and computer_choice == "paper" or action == "paper" and computer_choice == "scissors" or action == "scissors" and computer_choice == "rock":
        print("You Lost.")
    elif action == "rock" and computer_choice == "scissors" or action == "paper" and computer_choice == "rock" or action == "scissors" and computer_choice == "paper":
        print("You Won!")
    leave = input("Would you like to exit.\n").lower().strip()
    if leave == "yes" or leave == "y":
        break