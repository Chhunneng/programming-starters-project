import random

HANGMAN_PICS = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

WORDS = [
    "python", "computer", "programming", "hangman", "university", "graduate",
    "research", "engineering", "science", "developer", "education", "project"
]

def hangman():
    print("🔠 Welcome to Hangman!\n")

    word = random.choice(WORDS)
    guessed = set()
    wrong_guesses = 0
    max_wrong = len(HANGMAN_PICS) - 1

    display_word = ["_"] * len(word)

    while wrong_guesses < max_wrong and "_" in display_word:
        print(HANGMAN_PICS[wrong_guesses])
        print("Word:", " ".join(display_word))
        print(f"Guessed letters: {', '.join(sorted(guessed))}")
        print(f"Lives left: {max_wrong - wrong_guesses}")

        guess = input("\nEnter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("❌ Please enter a single letter.\n")
            continue

        if guess in guessed:
            print("⚠️ You already guessed that letter.\n")
            continue

        guessed.add(guess)

        if guess in word:
            print("✅ Correct guess!\n")
            for i, letter in enumerate(word):
                if letter == guess:
                    display_word[i] = guess
        else:
            print("❌ Wrong guess!\n")
            wrong_guesses += 1

    # Final game result
    print(HANGMAN_PICS[wrong_guesses])
    print("Final word:", word)

    if "_" not in display_word:
        print("🎉 CONGRATULATIONS! You won!")
    else:
        print("💀 GAME OVER! Better luck next time.")

    # Replay option
    again = input("\nPlay again? (y/n): ").lower()
    if again == "y":
        hangman()
    else:
        print("👋 Thanks for playing!")

if __name__ == "__main__":
    hangman()
