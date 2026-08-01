"""
Sysslan Internship - Level 5 - Task 3
Automated Folder Backup

A menu-driven console application that creates backups of a folder
using Python standard libraries (os, shutil, datetime).
"""

import os
import shutil
from datetime import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BACKUPS_DIR = os.path.join(SCRIPT_DIR, "Backups")


# ── Helper ───────────────────────────────────────────────────────────

def ensure_backups_folder():
    """Create the Backups folder if it does not exist."""
    if not os.path.exists(BACKUPS_DIR):
        os.makedirs(BACKUPS_DIR)
        print(f"  Created Backups folder: {BACKUPS_DIR}")


def generate_backup_name(source_path):
    """Return a backup folder name like FolderName_2026-08-01_143520."""
    folder_name = os.path.basename(os.path.normpath(source_path))
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    return f"{folder_name}_{timestamp}"


# ── Menu actions ─────────────────────────────────────────────────────

def create_backup():
    """Copy the user-specified folder into the Backups directory."""
    source = input("\nEnter the source folder path: ").strip().strip("'\"")

    if not source:
        print("  Error: No path entered.")
        return

    # Validate source
    if not os.path.exists(source):
        print(f"  Error: The path '{source}' does not exist.")
        return

    if not os.path.isdir(source):
        print(f"  Error: '{source}' is not a folder.")
        return

    # Prepare destination
    ensure_backups_folder()
    backup_name = generate_backup_name(source)
    destination = os.path.join(BACKUPS_DIR, backup_name)

    if os.path.exists(destination):
        print(f"  A backup named '{backup_name}' already exists.")
        print("  Please wait a moment and try again.")
        return

    # Copy folder
    try:
        shutil.copytree(source, destination)
        print(f"\n  Backup created successfully!")
        print(f"  Name : {backup_name}")
        print(f"  Path : {destination}")
    except PermissionError:
        print("  Error: Permission denied. Cannot access some files.")
    except shutil.Error as err:
        print(f"  Error during file copy: {err}")


def view_backup_info():
    """Display information about all existing backups."""
    if not os.path.exists(BACKUPS_DIR):
        print("\n  No Backups folder found. No backups have been created yet.")
        return

    entries = [
        e for e in os.listdir(BACKUPS_DIR)
        if os.path.isdir(os.path.join(BACKUPS_DIR, e))
    ]

    if not entries:
        print("\n  The Backups folder is empty. No backups found.")
        return

    entries.sort()

    print(f"\n--- Backup Information ---")
    print(f"  Total backups: {len(entries)}\n")

    # Column widths
    num_w = len(str(len(entries)))
    name_w = max(len(e) for e in entries)
    header_fmt = f"  {'#':>{num_w}}  {'Backup Name':<{name_w}}  {'Created On'}"
    row_fmt = f"  {{:>{num_w}}}  {{:<{name_w}}}  {{}}"

    print(header_fmt)
    print("  " + "-" * (num_w + name_w + 25))

    for idx, name in enumerate(entries, start=1):
        full_path = os.path.join(BACKUPS_DIR, name)
        created = os.path.getctime(full_path)
        created_str = datetime.fromtimestamp(created).strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        print(row_fmt.format(idx, name, created_str))

    print()


# ── Main loop ────────────────────────────────────────────────────────

def show_menu():
    """Print the main menu."""
    print("================================")
    print("   Automated Folder Backup")
    print("================================")
    print("  1. Create Backup")
    print("  2. View Backup Information")
    print("  3. Exit")
    print("================================")


def main():
    """Entry point: run the menu loop."""
    while True:
        show_menu()
        choice = input("Enter your choice (1-3): ").strip()

        try:
            if choice == "1":
                create_backup()
            elif choice == "2":
                view_backup_info()
            elif choice == "3":
                print("\nGoodbye!")
                break
            else:
                print("\nInvalid choice. Please enter 1, 2, or 3.\n")
        except Exception as err:
            print(f"\n  Unexpected error: {err}\n")

    print()


if __name__ == "__main__":
    main()
