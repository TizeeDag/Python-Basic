"""Campus IL self.py — exercise 7.3.1."""

def show_hidden_word(secret_word, old_letters_guessed):
    """Return guessed letters and underscores separated by single spaces."""
    result = []
    for letter in secret_word:
        if letter in old_letters_guessed:
            result.append(letter)
        else:
            result.append("_")
    return " ".join(result)

def main():
    print(show_hidden_word("mammals", ["s", "p", "j", "i", "m", "k"]))


if __name__ == "__main__":
    main()
