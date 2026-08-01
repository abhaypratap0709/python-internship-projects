# CSV Data Handling

## Description

Reads and processes data from a CSV file with display, search, and statistics features.

## Features

- Display all records in a formatted table
- Case-insensitive keyword search across all columns
- Basic statistics (record count, column count, min/max/avg for numeric columns)
- Validates CSV structure (empty files, mismatched row lengths)

## Concepts Used

- `csv` module for file reading
- Dynamic table formatting
- Numeric column detection
- Exception handling

## How to Run

```bash
python main.py
```

A sample `data.csv` file is included for testing.

## Expected Output

Menu-driven interface to explore and analyze CSV data.
