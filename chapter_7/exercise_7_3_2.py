"""Campus IL self.py — exercise 7.3.2."""

def check_win(secret_word, old_letters_guessed):
    """Return True when every letter in the secret word has been guessed."""
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True

def main():
    print(check_win("yes", ["d", "g", "e", "i", "s", "k", "y"]))


if __name__ == "__main__":
    main()
