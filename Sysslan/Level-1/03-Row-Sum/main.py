"""Task 3: Calculate and display the sum of each row in a 3×3 grid."""

GRID = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]


def display_grid(grid):
    """Print the grid row by row."""
    for row in grid:
        print("  ".join(str(num) for num in row))


def row_sums(grid):
    """Return a list containing the sum of each row."""
    return [sum(row) for row in grid]


def main():
    print("3×3 Number Grid")
    print("-" * 10)
    display_grid(GRID)
    print()

    sums = row_sums(GRID)
    for i, total in enumerate(sums, start=1):
        print(f"Row {i} sum: {total}")


if __name__ == "__main__":
    main()
