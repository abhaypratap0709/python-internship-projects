"""
Sysslan Internship - Level 4 - Task 1
Task Manager

A menu-driven console application to add, view, complete,
and delete tasks.
"""


def display_menu():
    """Display the main menu options."""
    print("\n===== Task Manager =====")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Exit")
    print("========================")


def add_task(tasks):
    """Prompt the user for a task description and add it to the list."""
    description = input("Enter task description: ").strip()
    if not description:
        print("Error: Task description cannot be empty.")
        return
    task = {"description": description, "completed": False}
    tasks.append(task)
    print(f'Task "{description}" added successfully.')


def view_tasks(tasks):
    """Display all tasks with their status."""
    if not tasks:
        print("No tasks found.")
        return
    print("\n--- Your Tasks ---")
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else "✗"
        print(f"{index}. [{status}] {task['description']}")
    print("------------------")


def mark_task_completed(tasks):
    """Mark a specific task as completed by its number."""
    if not tasks:
        print("No tasks to mark.")
        return
    view_tasks(tasks)
    try:
        choice = int(input("Enter task number to mark as completed: "))
    except ValueError:
        print("Error: Please enter a valid number.")
        return
    if choice < 1 or choice > len(tasks):
        print("Error: Invalid task number.")
        return
    task = tasks[choice - 1]
    if task["completed"]:
        print(f'Task "{task["description"]}" is already completed.')
    else:
        task["completed"] = True
        print(f'Task "{task["description"]}" marked as completed.')


def delete_task(tasks):
    """Delete a specific task by its number."""
    if not tasks:
        print("No tasks to delete.")
        return
    view_tasks(tasks)
    try:
        choice = int(input("Enter task number to delete: "))
    except ValueError:
        print("Error: Please enter a valid number.")
        return
    if choice < 1 or choice > len(tasks):
        print("Error: Invalid task number.")
        return
    confirm = input("Are you sure? (y/n): ").strip().lower()
    if confirm == "y":
        removed_task = tasks.pop(choice - 1)
        print(f'Task "{removed_task["description"]}" deleted successfully.')
    else:
        print("Deletion cancelled.")


def main():
    """Run the Task Manager application."""
    tasks = []
    print("Welcome to Task Manager!")

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
