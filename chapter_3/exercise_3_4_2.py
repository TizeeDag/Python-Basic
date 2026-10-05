"""Campus IL self.py — exercise 3.4.2."""

def main():
    text = input("Please enter a string: ")
    print(text[:1] + text[1:].replace(text[:1], "e"))


if __name__ == "__main__":
    main()
