"""Campus IL self.py — exercise 4.2.2."""

def main():
    word = input("Enter a word: ").replace(" ", "").lower()
    if word == word[::-1]:
        print("OK")
    else:
        print("NOT")


if __name__ == "__main__":
    main()
