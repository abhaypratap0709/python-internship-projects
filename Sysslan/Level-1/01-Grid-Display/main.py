"""Task 1: Display a simple 3×3 number grid."""

GRID = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]


def display_grid(grid):
    """Print the grid row by row."""
    for row in grid:
        print("  ".join(str(num) for num in row))


def main():
    print("3×3 Number Grid")
    print("-" * 10)
    display_grid(GRID)


if __name__ == "__main__":
    main()
