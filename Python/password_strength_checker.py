"""
password_strength_checker.py

Description:
This program evaluates the strength of a given password based on:
- Length
- Presence of uppercase letters
- Presence of lowercase letters
- Presence of numbers
- Presence of special characters

It provides a strength rating (Weak, Moderate, Strong) and suggestions to improve weak passwords.
"""

import re

def check_password_strength(password):
    """Evaluates the strength of the password."""
    strength_points = 0
    suggestions = []

    # Length check
    if len(password) >= 8:
        strength_points += 1
    else:
        suggestions.append("Use at least 8 characters.")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        strength_points += 1
    else:
        suggestions.append("Include at least one uppercase letter.")

    # Lowercase check
    if re.search(r"[a-z]", password):
        strength_points += 1
    else:
        suggestions.append("Include at least one lowercase letter.")

    # Digit check
    if re.search(r"[0-9]", password):
        strength_points += 1
    else:
        suggestions.append("Include at least one number.")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength_points += 1
    else:
        suggestions.append("Include at least one special character (!@#$%^&* etc.).")

    # Determine strength level
    if strength_points <= 2:
        strength = "Weak"
    elif strength_points == 3 or strength_points == 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, suggestions

def main():
    print("🔐 Password Strength Checker")
    password = input("Enter your password: ")

    strength, suggestions = check_password_strength(password)
    print(f"\nPassword Strength: {strength}")

    if suggestions:
        print("Suggestions to improve your password:")
        for s in suggestions:
            print(f"- {s}")

if __name__ == "__main__":
    main()
