"""Task 4: Generate the Fibonacci sequence for a given number of terms."""


def generate_fibonacci(n_terms: int) -> list[int]:
    """Return a list containing the first n_terms of the Fibonacci sequence."""
    if n_terms <= 0:
        return []
    if n_terms == 1:
        return [0]
        
    sequence = [0, 1]
    while len(sequence) < n_terms:
        next_val = sequence[-1] + sequence[-2]
        sequence.append(next_val)
        
    return sequence


def main() -> None:
    print("--- Fibonacci Sequence Generator ---")
    
    while True:
        user_input = input("Enter the number of terms (or 'q' to quit): ").strip()
        
        if user_input.lower() == 'q':
            break
            
        try:
            terms = int(user_input)
            
            if terms <= 0:
                print("Please enter a positive integer greater than 0.\n")
                continue
                
            fib_sequence = generate_fibonacci(terms)
            
            print(f"\nFibonacci sequence ({terms} terms):")
            # Format the list elegantly by separating items with commas
            print(", ".join(str(num) for num in fib_sequence))
            print()
            
        except ValueError:
            print("Invalid input! Please enter a valid integer.\n")


if __name__ == "__main__":
    main()
