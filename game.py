import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    guessed_number = random.randint(1, 100)
    
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100. Try to guess it!")
    
    # Initialize number of attempts
    attempts = 0

    while True:
        try:
            # Ask the user to input their guess
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Check if the guess is correct, too high, or too low
            if user_guess < guessed_number:
                print("Low! Try again.")
            elif user_guess > guessed_number:
                print("High! Try again.")
            else:
                print(f"Congratulations! You've guessed the correct number {guessed_number} in {attempts} attempts.")
                break  # Exit the loop when the user guesses correctly
        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Call the function to start the game
number_guessing_game()
