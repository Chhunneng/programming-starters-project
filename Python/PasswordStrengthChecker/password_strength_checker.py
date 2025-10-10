import re

def check_password_strength(password):
    # Criteria checks
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[@$!%*?&]", password) is None

    # Count how many conditions failed
    errors = sum([length_error, digit_error, uppercase_error, lowercase_error, symbol_error])

    if errors == 0:
        return "Strong 💪"
    elif errors <= 2:
        return "Moderate 👍"
    else:
        return "Weak ⚠️"

if __name__ == "__main__":
    print("🔐 Password Strength Checker")
    print("Your password should include uppercase, lowercase, digits, and special symbols.\n")

    while True:
        pwd = input("Enter a password (or type 'exit' to quit): ")
        if pwd.lower() == 'exit':
            print("Goodbye! 👋")
            break
        print(f"Password strength: {check_password_strength(pwd)}\n")
