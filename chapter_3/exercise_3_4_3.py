"""Campus IL self.py — exercise 3.4.3."""

def main():
    text = input("Please enter a string: ")
    middle = len(text) // 2
    print(text[:middle].lower() + text[middle:].upper())


if __name__ == "__main__":
    main()
