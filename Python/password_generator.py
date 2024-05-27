import random
import string

def get_user_choices():
    # Get user input for password length
    length = int(input("Enter the desired password length: "))

    # Prompt the user for character set preferences
    include_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
    include_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    include_special_chars = input("Include special characters? (y/n): ").strip().lower() == 'y'

    return length, include_lowercase, include_uppercase, include_numbers, include_special_chars

def build_character_set(include_lowercase, include_uppercase, include_numbers, include_special_chars):
    # Define character sets based on user input
    character_set = ''
    if include_lowercase:
        character_set += string.ascii_lowercase
    if include_uppercase:
        character_set += string.ascii_uppercase
    if include_numbers:
        character_set += string.digits
    if include_special_chars:
        character_set += string.punctuation

    return character_set

def generate_password(length, character_set):
    # Ensure the character set is not empty
    if not character_set:
        raise ValueError("At least one character type must be selected")

    # Generate password
    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

def main():
    try:
        length, include_lowercase, include_uppercase, include_numbers, include_special_chars = get_user_choices()
        character_set = build_character_set(include_lowercase, include_uppercase, include_numbers, include_special_chars)
        password = generate_password(length, character_set)
        print(f"Generated Password: {password}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
    