"""Record Management System - Sysslan Internship Level 3, Task 1.

A simple record management system where users can add and view records.
Each record contains a name and an age.
"""


def display_menu():
    """Display the main menu options."""
    print("\n===== Record Management System =====")
    print("1. Add Record")
    print("2. View All Records")
    print("3. Exit")
    print("====================================")


def add_record(records):
    """Prompt user for details and add a new record to the list."""
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

    record = {"name": name, "age": age}
    records.append(record)
    print(f"Record added: {name}, Age {age}")


def view_records(records):
    """Display all stored records in a formatted table."""
    if not records:
        print("No records found.")
        return

    print(f"\n{'No.':<5} {'Name':<20} {'Age':<5}")
    print("-" * 30)
    for index, record in enumerate(records, start=1):
        print(f"{index:<5} {record['name']:<20} {record['age']:<5}")
    print(f"\nTotal records: {len(records)}")


def main():
    """Run the record management system."""
    records = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            add_record(records)
        elif choice == "2":
            view_records(records)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
