import random

choices = ['rock', 'paper', 'scissors']


def get_user_input():
    while True:
        user_input = input("Enter your choice (rock, paper, or scissors): ").lower()

        if user_input in choices:
            return user_input
        else:
            print("Invalid choice. Please try again.")


def rock_paper_scissors(user_choice):
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


if __name__ == "__main__":
    # Run the rock-paper-scissors game
    rock_paper_scissors(get_user_input())
