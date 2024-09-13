import random
# Number guessing function
def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("Try to guess the number between 1 and 100.")

    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    attempts = 0
    guessed = False

    while not guessed:
        try:
            # Get user's guess and convert to integer
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Compare the guess with the target number
            if guess < target_number:
                print("Too low!")
            elif guess > target_number:
                print("Too high!")
            else:
                guessed = True
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
        except ValueError:
            # Handle non-numeric inputs
            print("Invalid input. Please enter a valid integer.")

# Run the game
number_guessing_game()
