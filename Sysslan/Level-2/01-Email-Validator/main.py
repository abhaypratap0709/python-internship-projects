"""Task 1: Validate an email address using basic rules."""
import re


def is_valid_email(email: str) -> bool:
    """
    Return True if the email is valid based on basic rules, False otherwise.
    Uses a standard regex for email validation.
    """
    if not email:
        return False
        
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.fullmatch(pattern, email.strip()))


def main() -> None:
    print("--- Email Validator ---")
    while True:
        email = input("Enter an email address to validate (or 'q' to quit): ").strip()
        
        if email.lower() == 'q':
            break
            
        if not email:
            print("Please enter a valid string.\n")
            continue

        if is_valid_email(email):
            print(f"✅ '{email}' is a valid email address.\n")
        else:
            print(f"❌ '{email}' is NOT a valid email address.\n")


if __name__ == "__main__":
    main()
