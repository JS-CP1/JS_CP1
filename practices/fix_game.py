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
        guess = int(input("Enter your guess: ")) #Add int() so it can compare to number_to_guess (TypeError)
        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True 
        elif guess == number_to_guess: #Changed to elif for correct syntax
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif guess > number_to_guess:
            print("Too high! Try again.")
        elif guess < number_to_guess:
            print("Too low! Try again.")  
        attempts += 1 #It won't increment attempts. increment attempts after every guess
        if attempts > max_attempts: #You can't ever lose. If you do too many attempts it will game over.
            break
        continue
    print("Game Over. Thanks for playing!")
start_game()