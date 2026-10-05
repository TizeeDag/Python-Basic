"""Campus IL self.py — exercise 4.3.1."""

def main():
    letter_guessed = input("Guess a letter: ")
    is_english = letter_guessed.isascii() and letter_guessed.isalpha()
    if len(letter_guessed) > 1 and not is_english:
        print("E3")
    elif len(letter_guessed) > 1:
        print("E1")
    elif not is_english:
        print("E2")
    else:
        print(letter_guessed.lower())


if __name__ == "__main__":
    main()
