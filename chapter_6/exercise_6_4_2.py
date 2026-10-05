"""Campus IL self.py — exercise 6.4.2."""

def check_valid_input(letter_guessed, old_letters_guessed):
    """Return whether the input is one English letter not already guessed."""
    letter = letter_guessed.lower()
    return len(letter) == 1 and "a" <= letter <= "z" and letter not in old_letters_guessed


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """Record a valid lowercase guess, or print X and the sorted old guesses."""
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower())
        return True
    print("X")
    print(" -> ".join(sorted(old_letters_guessed)))
    return False

def main():
    old_letters = ["a", "p", "c", "f"]
    print(try_update_letter_guessed("A", old_letters))


if __name__ == "__main__":
    main()
