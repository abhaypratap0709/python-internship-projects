"""
Sysslan Internship - Level 4 - Task 3
Calculator

A menu-driven console calculator that performs basic
arithmetic operations.
"""


def add(num_a, num_b):
    """Return the sum of two numbers."""
    return num_a + num_b


def subtract(num_a, num_b):
    """Return the difference of two numbers."""
    return num_a - num_b


def multiply(num_a, num_b):
    """Return the product of two numbers."""
    return num_a * num_b


def divide(num_a, num_b):
    """Return the quotient of two numbers.

    Returns None if the divisor is zero.
    """
    if num_b == 0:
        return None
    return num_a / num_b


def display_menu():
    """Display the calculator menu."""
    print("\n===== Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("======================")


def get_two_numbers():
    """Prompt the user for two numbers and return them.

    Returns a tuple (num_a, num_b) or None if input is invalid.
    """
    try:
        num_a = float(input("Enter the first number : "))
        num_b = float(input("Enter the second number: "))
    except ValueError:
        print("Error: Please enter valid numbers.")
        return None
    return num_a, num_b


OPERATIONS = {
    "1": ("Addition", add),
    "2": ("Subtraction", subtract),
    "3": ("Multiplication", multiply),
    "4": ("Division", divide),
}


def main():
    """Run the Calculator application."""
    print("Welcome to Calculator!")

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "5":
            print("Goodbye!")
            break

        if choice not in OPERATIONS:
            print("Error: Invalid choice. Please enter a number from 1 to 5.")
            continue

        operation_name, operation_func = OPERATIONS[choice]
        numbers = get_two_numbers()
        if numbers is None:
            continue

        num_a, num_b = numbers
        result = operation_func(num_a, num_b)

        if result is None:
            print("Error: Cannot divide by zero.")
        else:
            print(f"Result: {num_a} {operation_name.lower()} {num_b} = {result}")


if __name__ == "__main__":
    main()
