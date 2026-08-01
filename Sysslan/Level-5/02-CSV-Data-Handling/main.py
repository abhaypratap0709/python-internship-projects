"""
Sysslan Internship - Level 5 - Task 2
CSV Data Handling

A menu-driven console application that reads and processes data
from a CSV file using Python's built-in csv module.
"""

import csv
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(SCRIPT_DIR, "data.csv")


# ── Helper ───────────────────────────────────────────────────────────

def load_csv(filepath):
    """Read the CSV file and return (headers, rows).

    Raises FileNotFoundError, ValueError on empty/invalid files.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File '{filepath}' not found.")

    with open(filepath, newline="", encoding="utf-8") as fh:
        reader = csv.reader(fh)
        headers = next(reader, None)

        if headers is None:
            raise ValueError("CSV file is empty.")

        rows = [row for row in reader if row]

        if not rows:
            raise ValueError("CSV file has headers but no data rows.")

        # Verify every row matches header length
        for i, row in enumerate(rows, start=2):
            if len(row) != len(headers):
                raise ValueError(
                    f"Row {i} has {len(row)} fields; expected {len(headers)}."
                )

    return headers, rows


def print_table(headers, rows):
    """Print headers and rows as a neatly aligned table."""
    # Determine column widths
    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(cell))

    # Build format string
    fmt = " | ".join(f"{{:<{w}}}" for w in col_widths)
    separator = "-+-".join("-" * w for w in col_widths)

    print()
    print(fmt.format(*headers))
    print(separator)
    for row in rows:
        print(fmt.format(*row))
    print()


def find_numeric_columns(headers, rows):
    """Return a dict mapping column index → header for numeric columns."""
    numeric = {}
    for i in range(len(headers)):
        try:
            for row in rows:
                float(row[i])
            numeric[i] = headers[i]
        except ValueError:
            continue
    return numeric


# ── Menu actions ─────────────────────────────────────────────────────

def display_all_records(headers, rows):
    """Display every record in a formatted table."""
    print("\n--- All Records ---")
    print_table(headers, rows)


def search_record(headers, rows):
    """Prompt for a keyword and display matching rows."""
    keyword = input("\nEnter search keyword: ").strip()
    if not keyword:
        print("No keyword entered.")
        return

    matches = [
        row for row in rows
        if any(keyword.lower() in cell.lower() for cell in row)
    ]

    if matches:
        print(f"\n--- {len(matches)} matching record(s) ---")
        print_table(headers, matches)
    else:
        print(f"\nNo records matched '{keyword}'.")


def show_statistics(headers, rows):
    """Display total records, columns, and numeric-column stats."""
    print("\n--- Basic Statistics ---")
    print(f"  Total records : {len(rows)}")
    print(f"  Total columns : {len(headers)}")

    numeric_cols = find_numeric_columns(headers, rows)

    if numeric_cols:
        for idx, name in numeric_cols.items():
            values = [float(row[idx]) for row in rows]
            min_val = min(values)
            max_val = max(values)
            avg_val = sum(values) / len(values)
            print(f"\n  Column '{name}':")
            print(f"    Minimum : {min_val}")
            print(f"    Maximum : {max_val}")
            print(f"    Average : {avg_val:.2f}")
    else:
        print("  (No numeric columns found.)")
    print()


# ── Main loop ────────────────────────────────────────────────────────

def show_menu():
    """Print the main menu."""
    print("=============================")
    print("   CSV Data Handling Menu")
    print("=============================")
    print("  1. Display all records")
    print("  2. Search a record")
    print("  3. Show basic statistics")
    print("  4. Exit")
    print("=============================")


def main():
    """Entry point: load CSV once, then run the menu loop."""
    try:
        headers, rows = load_csv(CSV_FILE)
    except (FileNotFoundError, ValueError) as err:
        print(f"Error: {err}")
        return

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            display_all_records(headers, rows)
        elif choice == "2":
            search_record(headers, rows)
        elif choice == "3":
            show_statistics(headers, rows)
        elif choice == "4":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please enter 1, 2, 3, or 4.\n")


if __name__ == "__main__":
    main()
