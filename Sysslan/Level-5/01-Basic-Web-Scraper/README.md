# Basic Web Scraper

## Description

Fetches a webpage and displays its title using `requests` and `BeautifulSoup`.

## Features

- Accepts a URL from the user
- Validates URL format (http/https)
- Fetches the page and displays the status code
- Extracts and displays the page title
- Handles connection, timeout, and HTTP errors

## Concepts Used

- `requests` library for HTTP requests
- `BeautifulSoup` for HTML parsing
- Exception handling for network errors
- URL validation

## How to Run

```bash
pip install requests beautifulsoup4
python main.py
```

## Expected Output

Prompts for a URL and displays the webpage title and status code.
