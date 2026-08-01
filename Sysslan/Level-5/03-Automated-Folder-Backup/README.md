# Automated Folder Backup

## Description

Creates timestamped backups of user-specified folders into a local Backups directory.

## Features

- Copies an entire folder as a backup
- Names backups with folder name + timestamp (e.g., `Documents_2026-08-01_143520`)
- Prevents overwriting existing backups
- Lists all backups with creation dates
- Handles path validation, permission errors, and copy failures

## Concepts Used

- `os` and `shutil` modules
- `datetime` for timestamps
- Directory operations (`copytree`, `makedirs`)
- Exception handling

## How to Run

```bash
python main.py
```

## Expected Output

Menu-driven interface to create folder backups and view backup history.
