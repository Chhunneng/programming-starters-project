"""
rock_paper_scissors.py
Simple Rock-Paper-Scissors game: user vs computer.

Usage:
    python rock_paper_scissors.py

Author: Komal (for Hacktoberfest)
"""

import random

CHOICES = ("rock", "paper", "scissors")
SHORT = {"r": "rock", "p": "paper", "s": "scissors"}

def decide_winner(user_choice: str, comp_choice: str) -> str:
    """Return 'win', 'lose', or 'draw' from user's perspective."""
    if user_choice == comp_choice:
        return "draw"
    # rock beats scissors, scissors beats paper, paper beats rock
    wins = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock",
    }
    return "win" if wins[user_choice] == comp_choice else "lose"

def normalize_input(raw: str) -> str | None:
    """Normalize user input to 'rock', 'paper', or 'scissors'. Returns None if invalid."""
    if not raw:
        return None
    s = raw.strip().lower()
    if s in CHOICES:
        return s
    if s in SHORT:
        return SHORT[s]
    return None

def play_round() -> tuple[str, str, str]:
    """Plays one round. Returns (user_choice, comp_choice, outcome)."""
    while True:
        raw = input("Enter rock, paper, or scissors (r/p/s). Or 'q' to quit: ")
        if raw.strip().lower() == "q":
            return ("quit", "", "quit")
        user = normalize_input(raw)
        if user:
            comp = random.choice(CHOICES)
            outcome = decide_winner(user, comp)
            return (user, comp, outcome)
        print("Invalid input. Try again (rock/paper/scissors or r/p/s).")

def main():
    print("=== Rock Paper Scissors ===")
    wins = losses = draws = 0
    rounds = 0

    while True:
        user, comp, outcome = play_round()
        if outcome == "quit":
            break

        rounds += 1
        if outcome == "win":
            wins += 1
            print(f"You chose {user}. Computer chose {comp}. You WIN! 🎉")
        elif outcome == "lose":
            losses += 1
            print(f"You chose {user}. Computer chose {comp}. You LOSE. 😢")
        else:
            draws += 1
            print(f"You chose {user}. Computer chose {comp}. It's a DRAW. 🤝")

        print(f"Score: {wins} wins, {losses} losses, {draws} draws (Rounds: {rounds})\n")

    print("\nThanks for playing!")
    print(f"Final Score: {wins}W - {losses}L - {draws}D in {rounds} rounds")

if __name__ == "__main__":
    main()
