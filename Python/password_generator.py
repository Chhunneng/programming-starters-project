import secrets
import string


def include(message) -> bool:
    return (input(f"Include {message}? (Y/n): ").lower() or 'y') == 'y'


def generate_password():
    # Get user input for password length
    length = int(input("Enter the desired password length: "))

    # Combine character sets based on user choices
    character_set = ""
    character_set += string.ascii_lowercase if include("lowercase letters") else ''
    character_set += string.ascii_uppercase if include("uppercase letters") else ''
    character_set += string.digits if include("numbers") else ''
    character_set += string.punctuation if include("special characters") else ''

    # Generate password
    password = ''.join(secrets.choice(character_set) for _ in range(length))

    # Display the generated password
    print(f"Generated Password: {password}")


if __name__ == "__main__":
    # Run the password generator
    generate_password()
