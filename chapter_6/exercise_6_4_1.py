"""Campus IL self.py — exercise 6.4.1."""

def check_valid_input(letter_guessed, old_letters_guessed):
    """Return whether the input is one English letter not already guessed."""
    letter = letter_guessed.lower()
    return len(letter) == 1 and "a" <= letter <= "z" and letter not in old_letters_guessed

def main():
    print(check_valid_input("C", ["a", "b", "c"]))


if __name__ == "__main__":
    main()
