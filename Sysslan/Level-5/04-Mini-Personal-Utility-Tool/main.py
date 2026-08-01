"""
Sysslan Internship - Level 5 - Task 4
Mini Personal Utility Tool

A menu-driven console application that combines multiple useful
utilities: BMI Calculator, Age Calculator, Password Generator,
and Unit Converter.
"""

import random
import string
from datetime import date, datetime


# ── 1. BMI Calculator ───────────────────────────────────────────────

def bmi_calculator():
    """Calculate BMI from weight and height, display category."""
    print("\n--- BMI Calculator ---")

    try:
        weight = float(input("  Enter weight (kg): "))
        height = float(input("  Enter height (m) : "))
    except ValueError:
        print("  Error: Please enter valid numbers.")
        return

    if weight <= 0 or height <= 0:
        print("  Error: Weight and height must be positive.")
        return

    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal Weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    print(f"\n  Your BMI     : {bmi:.2f}")
    print(f"  Category     : {category}")


# ── 2. Age Calculator ───────────────────────────────────────────────

def age_calculator():
    """Calculate current age from a birth date in YYYY-MM-DD format."""
    print("\n--- Age Calculator ---")

    date_str = input("  Enter birth date (YYYY-MM-DD): ").strip()

    try:
        birth_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("  Error: Invalid date. Use YYYY-MM-DD format.")
        return

    today = date.today()

    if birth_date > today:
        print("  Error: Birth date cannot be in the future.")
        return

    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    print(f"\n  Your age: {age} years")


# ── 3. Password Generator ───────────────────────────────────────────

def password_generator():
    """Generate a strong random password of user-specified length."""
    print("\n--- Password Generator ---")

    try:
        length = int(input("  Enter desired password length (min 4): "))
    except ValueError:
        print("  Error: Please enter a valid number.")
        return

    if length < 4:
        print("  Error: Password length must be at least 4.")
        return

    # Guarantee at least one character from each category
    password_chars = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]

    all_chars = string.ascii_letters + string.digits + string.punctuation
    password_chars += [random.choice(all_chars) for _ in range(length - 4)]

    random.shuffle(password_chars)
    password = "".join(password_chars)

    print(f"\n  Generated password: {password}")


# ── 4. Unit Converter ───────────────────────────────────────────────

def celsius_to_fahrenheit():
    """Convert Celsius to Fahrenheit."""
    try:
        c = float(input("  Enter temperature in Celsius: "))
    except ValueError:
        print("  Error: Please enter a valid number.")
        return
    f = (c * 9 / 5) + 32
    print(f"  {c} °C = {f:.2f} °F")


def fahrenheit_to_celsius():
    """Convert Fahrenheit to Celsius."""
    try:
        f = float(input("  Enter temperature in Fahrenheit: "))
    except ValueError:
        print("  Error: Please enter a valid number.")
        return
    c = (f - 32) * 5 / 9
    print(f"  {f} °F = {c:.2f} °C")


def km_to_miles():
    """Convert Kilometers to Miles."""
    try:
        km = float(input("  Enter distance in Kilometers: "))
    except ValueError:
        print("  Error: Please enter a valid number.")
        return
    miles = km * 0.621371
    print(f"  {km} km = {miles:.2f} miles")


def miles_to_km():
    """Convert Miles to Kilometers."""
    try:
        miles = float(input("  Enter distance in Miles: "))
    except ValueError:
        print("  Error: Please enter a valid number.")
        return
    km = miles * 1.60934
    print(f"  {miles} miles = {km:.2f} km")


def unit_converter():
    """Display sub-menu for unit conversions."""
    while True:
        print("\n--- Unit Converter ---")
        print("  1. Celsius → Fahrenheit")
        print("  2. Fahrenheit → Celsius")
        print("  3. Kilometers → Miles")
        print("  4. Miles → Kilometers")
        print("  5. Back")

        choice = input("  Enter your choice (1-5): ").strip()

        if choice == "1":
            celsius_to_fahrenheit()
        elif choice == "2":
            fahrenheit_to_celsius()
        elif choice == "3":
            km_to_miles()
        elif choice == "4":
            miles_to_km()
        elif choice == "5":
            break
        else:
            print("  Invalid choice. Please enter 1-5.")


# ── Main menu ────────────────────────────────────────────────────────

def show_menu():
    """Print the main menu."""
    print("\n================================")
    print("   Mini Personal Utility Tool")
    print("================================")
    print("  1. BMI Calculator")
    print("  2. Age Calculator")
    print("  3. Password Generator")
    print("  4. Unit Converter")
    print("  5. Exit")
    print("================================")


def main():
    """Entry point: run the menu loop."""
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()

        try:
            if choice == "1":
                bmi_calculator()
            elif choice == "2":
                age_calculator()
            elif choice == "3":
                password_generator()
            elif choice == "4":
                unit_converter()
            elif choice == "5":
                print("\nGoodbye!")
                break
            else:
                print("\nInvalid choice. Please enter 1, 2, 3, 4, or 5.")
        except Exception as err:
            print(f"\n  Unexpected error: {err}")


if __name__ == "__main__":
    main()
