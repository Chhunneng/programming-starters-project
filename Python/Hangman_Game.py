import random

def display_hangman(tries):
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stages[tries]

def get_word():
    words = ['python', 'hangman', 'programming', 'developer', 'computer', 
             'keyboard', 'algorithm', 'function', 'variable', 'database',
             'software', 'hardware', 'internet', 'network', 'security']
    return random.choice(words).upper()

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display.strip()

def play_hangman():
    print("=" * 40)
    print("Welcome to Hangman!")
    print("=" * 40)
    
    word = get_word()
    guessed_letters = set()
    tries = 6
    game_over = False
    
    while not game_over:
        print(display_hangman(tries))
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Tries remaining: {tries}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        
        # Get player input
        guess = input("\nGuess a letter: ").upper()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter!")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        
        guessed_letters.add(guess)
        
        # Check if guess is in word
        if guess in word:
            print(f"Good job! '{guess}' is in the word!")
            
            # Check if player won
            if all(letter in guessed_letters for letter in word):
                print(f"\n🎉 Congratulations! You won! The word was: {word}")
                game_over = True
        else:
            tries -= 1
            print(f"Sorry! '{guess}' is not in the word.")
            
            # Check if player lost
            if tries == 0:
                print(display_hangman(tries))
                print(f"\n💀 Game Over! The word was: {word}")
                game_over = True
        
        print("\n" + "-" * 40)
    
    # Ask to play again
    play_again = input("\nWould you like to play again? (yes/no): ").lower()
    if play_again == 'yes' or play_again == 'y':
        play_hangman()
    else:
        print("Thanks for playing! Goodbye!")

if __name__ == "__main__":
    play_hangman()