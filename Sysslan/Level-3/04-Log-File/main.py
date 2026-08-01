"""Log File - Sysslan Internship Level 3, Task 4.

Create a log file that records messages with the current date and time.
"""

from datetime import datetime

LOG_FILE = "app.log"


def write_log(message):
    """Write a timestamped message to the log file.

    Args:
        message: The log message to record.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}\n"

    try:
        with open(LOG_FILE, "a", encoding="utf-8") as file:
            file.write(log_entry)
        print(f"Logged: {log_entry.strip()}")
    except IOError as error:
        print(f"Error writing to log file: {error}")


def view_logs():
    """Read and display all entries from the log file."""
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        print("No log file found. Write a log message first.")
        return
    except IOError as error:
        print(f"Error reading log file: {error}")
        return

    if not content.strip():
        print("Log file is empty.")
        return

    print(f"\n--- Log Entries ({LOG_FILE}) ---")
    print(content)
    print("-" * 40)


def clear_logs():
    """Clear all entries from the log file."""
    try:
        with open(LOG_FILE, "w", encoding="utf-8") as file:
            file.write("")
        print("Log file cleared.")
    except IOError as error:
        print(f"Error clearing log file: {error}")


def main():
    """Run the log file system."""
    while True:
        print("\n===== Log File System =====")
        print("1. Write Log Message")
        print("2. View All Logs")
        print("3. Clear Logs")
        print("4. Exit")
        print("===========================")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            message = input("Enter log message: ").strip()
            if not message:
                print("Error: Message cannot be empty.")
                continue
            write_log(message)
        elif choice == "2":
            view_logs()
        elif choice == "3":
            confirm = input("Are you sure? (y/n): ").strip().lower()
            if confirm == "y":
                clear_logs()
            else:
                print("Clear cancelled.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
