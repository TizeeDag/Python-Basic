"""Campus IL self.py — exercise 7.2.2."""

def numbers_letters_count(my_str):
    """Return digit and nondigit counts, including punctuation and spaces."""
    digits = 0
    for char in my_str:
        if char.isdigit():
            digits += 1
    return [digits, len(my_str) - digits]

def main():
    print(numbers_letters_count("Python 3.6.3"))


if __name__ == "__main__":
    main()
