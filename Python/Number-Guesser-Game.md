# Number Guesser Game in Python

Welcome to the Number Guesser Game project for Python! 🎮

In this project, we'll create a simple game where the computer randomly selects a number, and the player guesses it. This project is great for learning about random number generation, loops, and conditional logic. Let's get started!

## Project Overview

### Objective

Create a Python script that generates a random number between 1 and 100, then allows the user to guess the number with feedback on whether their guess is too high or too low.

### Features

- Randomly generate a number between 1 and 100 each time the game starts.

- Prompt the user to guess the number.

- Provide "Higher" or "Lower" feedback for incorrect guesses.

- Notify the user when they guess correctly.

## Project Structure

Create a new Python script named `number_guesser.py`.

## Instructions

1. Generate a Random Number:

- Use Python's random module to generate a number between 1 and 100.

2. User Input Loop:

- Continuously prompt the user to guess the number.

- Compare the user's guess to the generated number.

3. Provide Feedback:

- If the guess is incorrect, print "Higher!" or "Lower!" to guide the user.

- Continue prompting until the user guesses correctly.

4. Win Notification:

- Congratulate the user and display the number of attempts when they guess the correct number.

5. Run the Script:

- Execute the script and play the game!

## Example Code

```py
import random

def number_guesser():
    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guesser Game!")
    print("I've picked a number between 1 and 100. Can you guess it?")

    while True:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess < target_number:
            print("Higher!")
        elif user_guess - target_number:
            print("Lower!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")
            break

# Start the game
number_guesser()
```

## Notes

- This code uses random.randint(1, 100) to generate a new number each game.

- The loop continues indefinitely until the correct guess is made.

- Error handling for non-integer inputs is not included here but can be added as an enhancement.
