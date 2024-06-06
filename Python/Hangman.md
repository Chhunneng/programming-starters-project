# Hangman in Python

Welcome to the Hangman project for Python! 🐍

## Project Overview

In this project, we'll create a simple word guessing game that chooses from a random list of words and let's the player guess what the word is. 

### Objective

Create a Python script that implements a simple word guessing game

### Features

- The computer chooses a random word from the word list
- The player tries to guess a letter to see if it is in the word
- The game shows if the letter was part of the word
- Tracks how many tries are left

## Project Structure

Create a new Python script named `hangman.py`.

## Instructions

1. **Make a list of possible words:**
   - Create a array/list of words

2. **Get a random word from the list:**
   - Use the function choice from the `random` module to get a random word from your word list

3. **Create a list of "_" to give hints to the player:**
   - You can create a list of the same element by multiplying it by a number, in this case the length of your secret word. e.g `["_"] * len(secret)`

4. **Prompt the player for a guess:**
   - Ask the player to guess a letter

5. **Check if the guess was correct:**
   - Check if the letter is in the word and replace the "_" with the letter the player got correct
   - If the letter is not in the word reduce the lives the player has

6. **Check if the game has ended:**
   - If the player lives reach 0 it should be a game over
   - If there are no more "_" in the word the player won the game
   - If one of these conditions are reached break the loop with a message

## Example Code

```python
import random


def hangman():
    
    word_list = ["apple", "banana", "grape", "mango", "lemon", "orange"]
    lives = 6
    # choose a random word from the list
    secret = random.choice(word_list)
    # create a list of letters that will show what letters the player has guessed correctly
    word = ["_"] * len(secret)

    print("Welcome to Hangman!")
    print(f"Try to guess the word, you have {lives} lives.")

    while True:
        # convert the list to a string
        print("Your word is: ", "".join(word))
        # takes a input from the player
        guess = input("Guess a letter: ")

        # if the guess was in the word replace the _ with the word
        if guess in secret:
            for i in range(len(secret)):
                if secret[i] == guess:
                    word[i] = guess
            print("Correct!")
        else:
            lives -= 1
            print("Incorrect! You have", lives, "lives left.")

        # ends the game if the player has no lives left or if the word has been guessed
        if lives == 0:
            print("You lost! The word was", secret)
            break
        if "_" not in word:
            print("You won! The word was", secret)
            break


hangman()
```

Feel free to enhance the game, add features, or modify the structure as you see fit. Contributors can use this document as a guide to implementing a word guessing game in Python.
