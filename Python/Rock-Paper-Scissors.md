# Rock, Paper, Scissors Game in Python

Welcome to the Rock, Paper, Scissors Game project for Python! ✊🏻✋🏻✌🏻

In this project, we'll create a simple rock-paper-scissors game using Python. This classic game is great for practicing conditional statements and user input handling. Let's get started!

## Project Overview

### Objective

Create a Python script that allows a user to play the rock-paper-scissors game against the computer.

### Features

- Accept user input for their choice (rock, paper, or scissors).
- Generate a random choice for the computer.
- Determine the winner based on the game rules.

## Project Structure

Create a new Python script named `rock_paper_scissors.py`.

## Instructions

1. **User Input:**
   - Prompt the user to enter their choice (rock, paper, or scissors).

2. **Computer's Choice:**
   - Generate a random choice for the computer (rock, paper, or scissors).

3. **Game Logic:**
   - Implement the game logic to determine the winner.
   - Rock beats scissors, scissors beats paper, and paper beats rock.

4. **Display Result:**
   - Print the user's choice, the computer's choice, and the result of the game.

5. **Run the Script:**
   - Execute the script and play the game against the computer.

## Example Code

```python
import random

def rock_paper_scissors(user_choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    print(f"Your choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        print("You win!")
    else:
        print("You lose!")

# Get user input for their choice
user_input = input("Enter your choice (rock, paper, or scissors): ").lower()

# Run the rock-paper-scissors game
rock_paper_scissors(user_input)
```

Feel free to customize the rock-paper-scissors game, add features, or modify the structure as you see fit. Contributors can use this document as a guide to implementing the rock-paper-scissors game in Python.
