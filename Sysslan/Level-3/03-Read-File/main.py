"""Read File - Sysslan Internship Level 3, Task 3.

Read the contents of a text file and display them safely
with proper error handling if the file does not exist.
"""


def read_file(filepath):
    """Read and return the contents of a text file.

    Args:
        filepath: Path to the file to read.

    Returns:
        The file contents as a string, or None if an error occurred.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied to read '{filepath}'.")
    except IOError as error:
        print(f"Error reading file: {error}")
    return None


def display_file_contents(filepath):
    """Read a file and display its contents with formatting."""
    print(f"\n--- Reading: {filepath} ---")
    content = read_file(filepath)

    if content is not None:
        if content.strip():
            print(content)
        else:
            print("(File is empty.)")
    print("-" * 40)


def main():
    """Prompt user for a file path and display its contents."""
    while True:
        print("\n===== File Reader =====")
        print("1. Read a file")
        print("2. Exit")
        print("=======================")

        choice = input("Enter your choice (1-2): ").strip()

        if choice == "1":
            filepath = input("Enter the file path: ").strip().strip('"').strip("'")
            if not filepath:
                print("Error: File path cannot be empty.")
                continue
            display_file_contents(filepath)
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
