"""Campus IL self.py — exercise 5.5.1."""

def is_valid_input(letter_guessed):
    """Return True for exactly one English letter, of either case."""
    return len(letter_guessed) == 1 and "a" <= letter_guessed.lower() <= "z"

def main():
    print(is_valid_input(input("Guess a letter: ")))


if __name__ == "__main__":
    main()
