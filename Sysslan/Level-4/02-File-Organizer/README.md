# File Organizer

## Description

Organizes files inside a folder by sorting them into category subfolders based on their extensions.

## Features

- Categorizes files into Images, PDFs, Documents, Audio, Videos, and Others
- Creates category folders automatically
- Skips files that already exist at the destination
- Displays an organization summary

## Concepts Used

- `os` and `shutil` modules
- File extension parsing
- Dictionary-based mapping
- Error handling for file operations

## How to Run

```bash
python main.py
```

## Expected Output

Prompts for a folder path and moves files into categorized subfolders.
