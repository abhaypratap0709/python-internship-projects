"""Task 4: Verify whether every number in a 3×3 grid is unique."""

GRID = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]


def display_grid(grid):
    """Print the grid row by row."""
    for row in grid:
        print("  ".join(str(num) for num in row))


def all_unique(grid):
    """Return True if every number in the grid is unique."""
    numbers = [num for row in grid for num in row]
    return len(numbers) == len(set(numbers))


def main():
    print("3×3 Number Grid")
    print("-" * 10)
    display_grid(GRID)
    print()

    if all_unique(GRID):
        print("All numbers in the grid are unique.")
    else:
        print("There are duplicate numbers in the grid.")


if __name__ == "__main__":
    main()
