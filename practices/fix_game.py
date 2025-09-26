#JS, 1st, Fixing Game
import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    game_over = False
    while not game_over:
        guess = int(input("Enter your guess: ")) #Add int() so it can compare to number_to_guess
        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True 
        elif guess == number_to_guess: #Changed to elif to make sure you can't have both (attempts >= max_attempts) and (guess == number_to_guess) be true
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif guess > number_to_guess:
            print("Too high! Try again.")
        elif guess < number_to_guess:
            print("Too low! Try again.")  
        attempts += 1 #It won't increment attempts. Increment attempts after every guess
        #Removed continue, it's redundant
    print("Game Over. Thanks for playing!")
start_game()