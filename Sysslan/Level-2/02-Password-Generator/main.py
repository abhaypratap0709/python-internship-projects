"""Task 2: Generate a random password."""
import random
import string


def generate_password(length: int) -> str:
    """
    Generate a random password using uppercase, lowercase,
    numbers, and special characters.
    """
    if length < 4:
        raise ValueError("Password length must be at least 4 to include all character types.")

    # Guarantee at least one of each required character type
    lower = random.choice(string.ascii_lowercase)
    upper = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    special = random.choice(string.punctuation)

    # Fill the remaining length with a random selection of all character types
    all_chars = string.ascii_letters + string.digits + string.punctuation
    remaining = [random.choice(all_chars) for _ in range(length - 4)]

    # Combine all characters and shuffle to ensure randomness
    password_chars = [lower, upper, digit, special] + remaining
    random.shuffle(password_chars)

    return "".join(password_chars)


def main() -> None:
    print("--- Random Password Generator ---")
    
    while True:
        user_input = input("Enter desired password length (or 'q' to quit): ").strip()
        
        if user_input.lower() == 'q':
            break
            
        try:
            length = int(user_input)
            if length < 4:
                print("Error: Password length should be at least 4 for strong passwords.\n")
                continue
                
            password = generate_password(length)
            print(f"\nYour generated password ({length} chars):")
            print(f">>> {password} <<<\n")
            
        except ValueError:
            print("Invalid input! Please enter a valid integer.\n")


if __name__ == "__main__":
    main()
