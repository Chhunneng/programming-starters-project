# Number Guessing Game in Python

Welcome to the Number Guessing Game project for Python! 🐍

In this project, we'll create a simple number guessing game where the computer randomly selects a number, and the player tries to guess it. Let's get started!

## Project Overview

### Objective

Create a Python script that implements a number guessing game.

### Features

- The computer generates a random number.
- The player tries to guess the number.
- Provide feedback on whether the guess is too high, too low, or correct.
- Track the number of attempts.

## Project Structure

Create a new Python script named `number_guessing_game.py`.

## Instructions

1. **Generate a Random Number:**
   - Use the `random` module to generate a random number between a predefined range.

2. **Get Player Input:**
   - Prompt the player to enter a guess.

3. **Compare and Provide Feedback:**
   - Compare the player's guess with the randomly generated number.
   - If the guess is correct, print a congratulatory message.
   - If the guess is too high or too low, provide feedback.

4. **Track Attempts:**
   - Keep track of the number of attempts made by the player.

5. **Play Again (Optional):**
   - After the game ends, ask the player if they want to play again.

## Example Code

```python
import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    target_number = random.randint(1, 50)

    attempts = 0

    while True:
        # Get player input
        guess = int(input("Enter your guess: "))

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

# Run the game
number_guessing_game()
```

Feel free to enhance the game, add features, or modify the structure as you see fit. Contributors can use this document as a guide to implementing the number guessing game in Python.
