"""Campus IL self.py — exercise 9.4.1."""

def choose_word(file_path, index):
    """Return unique word count and the word at a circular, one-based index."""
    with open(file_path, encoding="utf-8") as file:
        words = file.read().split()
    return len(set(words)), words[(index - 1) % len(words)]

def main():
    print(choose_word(input("Enter file path: "), int(input("Enter index: "))))


if __name__ == "__main__":
    main()
