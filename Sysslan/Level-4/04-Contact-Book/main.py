"""
Sysslan Internship - Level 4 - Task 4
Contact Book

A menu-driven console application to manage contacts
(add, view, search, delete).
"""


def display_menu():
    """Display the main menu options."""
    print("\n===== Contact Book =====")
    print("1. Add a new contact")
    print("2. View all contacts")
    print("3. Search for a contact")
    print("4. Delete a contact")
    print("5. Exit")
    print("========================")


def find_contact(contacts, name):
    """Return the index of a contact by name (case-insensitive).

    Returns -1 if not found.
    """
    for index, contact in enumerate(contacts):
        if contact["name"].lower() == name.lower():
            return index
    return -1


def add_contact(contacts):
    """Prompt the user and add a new contact to the list."""
    name = input("Enter contact name  : ").strip()
    if not name:
        print("Error: Name cannot be empty.")
        return

    if find_contact(contacts, name) != -1:
        print(f'Error: A contact named "{name}" already exists.')
        return

    phone = input("Enter phone number  : ").strip()
    if not phone:
        print("Error: Phone number cannot be empty.")
        return

    contacts.append({"name": name, "phone": phone})
    print(f'Contact "{name}" added successfully.')


def view_contacts(contacts):
    """Display all contacts in a numbered format."""
    if not contacts:
        print("No contacts found.")
        return
    print("\n--- Your Contacts ---")
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. {contact['name']}")
        print(f"   Phone: {contact['phone']}")
    print("---------------------")


def search_contact(contacts):
    """Search for a contact by name and display the result."""
    if not contacts:
        print("No contacts to search.")
        return
    name = input("Enter name to search: ").strip()
    if not name:
        print("Error: Name cannot be empty.")
        return
    index = find_contact(contacts, name)
    if index == -1:
        print(f'Contact "{name}" not found.')
    else:
        contact = contacts[index]
        print(f"\n  Name : {contact['name']}")
        print(f"  Phone: {contact['phone']}")


def delete_contact(contacts):
    """Delete a contact by name after confirmation."""
    if not contacts:
        print("No contacts to delete.")
        return
    name = input("Enter name to delete: ").strip()
    if not name:
        print("Error: Name cannot be empty.")
        return
    index = find_contact(contacts, name)
    if index == -1:
        print(f'Contact "{name}" not found.')
        return
    confirm = input(f'Delete "{contacts[index]["name"]}"? (y/n): ').strip().lower()
    if confirm == "y":
        removed = contacts.pop(index)
        print(f'Contact "{removed["name"]}" deleted successfully.')
    else:
        print("Deletion cancelled.")


def main():
    """Run the Contact Book application."""
    contacts = []
    print("Welcome to Contact Book!")

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
