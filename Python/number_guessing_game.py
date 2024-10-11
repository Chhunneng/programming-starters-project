import random


def number_guessing_game():
    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)

    attempts = 0

    while True:
        # Get player input
        guess = int(input("Enter your guess between 1 and 100: "))

        # Increment attempts
        attempts += 1

        # Compare and provide feedback
        if guess == target_number:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            break
        elif guess < target_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")


if __name__ == "__main__":
    # Run the game
    number_guessing_game()
