"""
Sysslan Internship - Level 4 - Task 2
File Organizer

A console application that organizes files inside a folder
based on their file extensions.
"""

import os
import shutil


# Mapping of extensions to category folder names.
EXTENSION_MAP = {
    # Images
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".bmp": "Images",
    ".svg": "Images",
    ".webp": "Images",
    # PDFs
    ".pdf": "PDFs",
    # Documents
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".odt": "Documents",
    ".rtf": "Documents",
    ".xlsx": "Documents",
    ".xls": "Documents",
    ".pptx": "Documents",
    ".csv": "Documents",
    # Audio
    ".mp3": "Audio",
    ".wav": "Audio",
    ".flac": "Audio",
    ".aac": "Audio",
    ".ogg": "Audio",
    # Videos
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",
    ".mov": "Videos",
    ".wmv": "Videos",
}


def get_category(extension):
    """Return the category folder name for a given file extension."""
    return EXTENSION_MAP.get(extension.lower(), "Others")


def get_folder_path():
    """Prompt the user for a valid folder path and return it."""
    folder_path = input("Enter the folder path to organize: ").strip()
    if not folder_path:
        print("Error: Path cannot be empty.")
        return None
    if not os.path.isdir(folder_path):
        print(f'Error: "{folder_path}" is not a valid directory.')
        return None
    return folder_path


def organize_files(folder_path):
    """Organize files in the given folder by extension.

    Returns a dict mapping category names to the count of files moved.
    """
    summary = {}
    skipped = 0

    for entry in os.listdir(folder_path):
        source = os.path.join(folder_path, entry)

        # Skip directories.
        if not os.path.isfile(source):
            continue

        _, extension = os.path.splitext(entry)

        # Skip files with no extension.
        if not extension:
            category = "Others"
        else:
            category = get_category(extension)

        destination_dir = os.path.join(folder_path, category)
        os.makedirs(destination_dir, exist_ok=True)

        destination = os.path.join(destination_dir, entry)

        if os.path.exists(destination):
            print(f'  Skipped: "{entry}" already exists in {category}/.')
            skipped += 1
            continue

        try:
            shutil.move(source, destination)
            summary[category] = summary.get(category, 0) + 1
        except (shutil.Error, OSError) as error:
            print(f'  Error moving "{entry}": {error}')

    return summary, skipped


def display_summary(summary, skipped):
    """Print how many files were moved into each category."""
    if not summary and skipped == 0:
        print("\nNo files found to organize.")
        return

    total_moved = sum(summary.values())
    print("\n===== Organization Summary =====")
    for category in sorted(summary):
        print(f"  {category}: {summary[category]} file(s)")
    print(f"\nTotal moved : {total_moved}")
    if skipped:
        print(f"Total skipped: {skipped}")
    print("================================")


def display_menu():
    """Display the main menu."""
    print("\n===== File Organizer =====")
    print("1. Organize a folder")
    print("2. Exit")
    print("==========================")


def main():
    """Run the File Organizer application."""
    print("Welcome to File Organizer!")

    while True:
        display_menu()
        choice = input("Enter your choice (1-2): ").strip()

        if choice == "1":
            folder_path = get_folder_path()
            if folder_path is None:
                continue
            print(f'\nOrganizing files in "{folder_path}"...')
            summary, skipped = organize_files(folder_path)
            display_summary(summary, skipped)

        elif choice == "2":
            print("Goodbye!")
            break

        else:
            print("Error: Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
