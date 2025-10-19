# Hangman Game 🎮

A classic word-guessing game implemented in Python with a command-line interface.

## Description

Hangman is a word puzzle game where players try to guess a hidden word by suggesting letters within a limited number of attempts. Each incorrect guess adds a part to the hangman drawing. The game ends when the player either guesses the word correctly or runs out of attempts.

## Features

- 🎨 ASCII art hangman visualization
- 🎲 Random word selection from a tech-themed word list
- ✅ Input validation and error handling
- 📊 Real-time tracking of guessed letters
- 🔄 Play again option
- 💬 Clear win/loss feedback
- 🎯 6 attempts to guess the word

## Prerequisites

- Python 3.6 or higher

## Installation

1. Clone the repository or download the `hangman.py` file
2. No additional dependencies required - uses only Python standard library

## How to Run

```bash
python Hangman_Game.py
```

## How to Play

1. The game will display underscores representing each letter in the hidden word
2. Guess one letter at a time by typing it and pressing Enter
3. If your guess is correct, the letter will be revealed in its position(s)
4. If your guess is wrong, you lose one attempt and a body part is added to the hangman
5. You have 6 incorrect guesses before the game is over
6. Win by guessing all letters in the word before running out of attempts
7. After each game, you can choose to play again or exit

## Game Rules

- Only single alphabetic characters are accepted as input
- Letter guesses are case-insensitive
- You cannot guess the same letter twice
- Special characters and numbers are not valid inputs

## Example Gameplay

```
========================================
Welcome to Hangman!
========================================

   --------
   |      |
   |      
   |    
   |      
   |     
   -

Word: _ _ _ _ _ _
Tries remaining: 6
Guessed letters: None

Guess a letter: p

Good job! 'P' is in the word!
```

## Word List

The game includes a curated list of technology-related words including:
- python
- hangman
- programming
- developer
- computer
- And more!

Feel free to expand the word list by editing the `words` array in the `get_word()` function.

## Customization

You can customize the game by:
- **Adding more words**: Edit the `words` list in the `get_word()` function
- **Changing difficulty**: Modify the `tries` variable in `play_hangman()` function
- **Updating the hangman display**: Edit the `stages` list in `display_hangman()` function

## Code Structure

- `display_hangman(tries)`: Returns the ASCII art for the current game state
- `get_word()`: Randomly selects a word from the word list
- `display_word(word, guessed_letters)`: Shows the word with guessed letters revealed
- `play_hangman()`: Main game loop that handles gameplay logic

---

**Enjoy playing Hangman!** 🎉