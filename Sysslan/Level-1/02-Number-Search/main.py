"""Task 2: Search for a number in a 3×3 grid."""

GRID = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]


def display_grid(grid):
    """Print the grid row by row."""
    for row in grid:
        print("  ".join(str(num) for num in row))


def search_number(grid, target):
    """Return True if target exists in the grid, False otherwise."""
    for row in grid:
        if target in row:
            return True
    return False


def main():
    print("3×3 Number Grid")
    print("-" * 10)
    display_grid(GRID)
    print()

    try:
        target = int(input("Enter a number to search: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    if search_number(GRID, target):
        print(f"{target} was found in the grid.")
    else:
        print(f"{target} was NOT found in the grid.")


if __name__ == "__main__":
    main()
