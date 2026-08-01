"""Task 3: Accept text input and display total characters and words."""


def analyze_text(text: str) -> tuple[int, int]:
    """Return the total number of characters (including spaces) and words in the text."""
    total_chars = len(text)
    total_words = len(text.split())
    return total_chars, total_words


def main() -> None:
    print("--- Text Analyzer ---")
    
    while True:
        text = input("Enter some text to analyze (or 'q' to quit): ")
        
        # Check for exact string 'q' to quit (avoids quitting on random sentences starting with q)
        if text.strip() == 'q':
            break
            
        if not text.strip():
            print("Empty input. Please provide some text.\n")
            continue
            
        chars, words = analyze_text(text)
        
        print("\nAnalysis Results:")
        print("-" * 17)
        print(f"Total Characters: {chars}")
        print(f"Total Words.....: {words}\n")


if __name__ == "__main__":
    main()
