"""Save and Retrieve Records - Sysslan Internship Level 3, Task 2.

Save records to a text file and retrieve them later.
Records are stored one per line in the format: name,age
"""

import os

RECORDS_FILE = "records.txt"


def display_menu():
    """Display the main menu options."""
    print("\n===== Save & Retrieve Records =====")
    print("1. Add Record")
    print("2. View All Records")
    print("3. Exit")
    print("====================================")


def add_record():
    """Prompt user for details and save a record to the text file."""
    name = input("Enter name: ").strip()
    if not name:
        print("Error: Name cannot be empty.")
        return

    age = input("Enter age: ").strip()
    try:
        age = int(age)
        if age < 0:
            print("Error: Age must be a positive number.")
            return
    except ValueError:
        print("Error: Age must be a valid integer.")
        return

    try:
        with open(RECORDS_FILE, "a", encoding="utf-8") as file:
            file.write(f"{name},{age}\n")
        print(f"Record saved: {name}, Age {age}")
    except IOError as error:
        print(f"Error saving record: {error}")


def view_records():
    """Read and display all records from the text file."""
    if not os.path.exists(RECORDS_FILE):
        print("No records file found. Add a record first.")
        return

    try:
        with open(RECORDS_FILE, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except IOError as error:
        print(f"Error reading records: {error}")
        return

    if not lines:
        print("No records found.")
        return

    print(f"\n{'No.':<5} {'Name':<20} {'Age':<5}")
    print("-" * 30)
    count = 0
    for index, line in enumerate(lines, start=1):
        line = line.strip()
        if not line:
            continue
        parts = line.split(",", 1)
        if len(parts) == 2:
            print(f"{index:<5} {parts[0]:<20} {parts[1]:<5}")
            count += 1
    print(f"\nTotal records: {count}")


def main():
    """Run the save and retrieve records system."""
    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            add_record()
        elif choice == "2":
            view_records()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
