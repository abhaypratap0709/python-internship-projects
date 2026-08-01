"""
Sysslan Internship - Level 5 - Task 1
Basic Web Scraper

A menu-driven console application that fetches and displays
the title of a webpage using requests and BeautifulSoup.
"""

import requests
from bs4 import BeautifulSoup


def display_menu():
    """Display the main menu options."""
    print("\n===== Web Scraper =====")
    print("1. Scrape Website")
    print("2. Exit")
    print("=======================")


def is_valid_url(url):
    """Check whether the URL starts with http:// or https://."""
    return url.startswith("http://") or url.startswith("https://")


def fetch_page(url):
    """Download a webpage and return the Response object.

    Returns None if an error occurs.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the website.")
    except requests.exceptions.Timeout:
        print("Error: The request timed out.")
    except requests.exceptions.HTTPError as error:
        print(f"HTTP Error: {error}")
    except requests.exceptions.RequestException as error:
        print(f"Error: {error}")
    return None


def extract_title(html):
    """Parse the HTML and return the page title.

    Returns None if no <title> tag is found.
    """
    soup = BeautifulSoup(html, "html.parser")
    title_tag = soup.find("title")
    if title_tag and title_tag.string:
        return title_tag.string.strip()
    return None


def scrape_website():
    """Ask the user for a URL, fetch it, and display its title."""
    url = input("Enter the website URL: ").strip()

    if not url:
        print("Error: URL cannot be empty.")
        return

    if not is_valid_url(url):
        print("Error: Invalid URL. Please include http:// or https://.")
        return

    print(f"Fetching: {url} ...")
    response = fetch_page(url)
    if response is None:
        return

    print(f"Status Code : {response.status_code}")
    title = extract_title(response.text)
    if title:
        print(f"Page Title  : {title}")
    else:
        print("No <title> tag found on this page.")


def main():
    """Run the Web Scraper application."""
    print("Welcome to Web Scraper!")

    while True:
        display_menu()
        choice = input("Enter your choice (1-2): ").strip()

        if choice == "1":
            scrape_website()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
