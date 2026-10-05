"""Campus IL self.py — exercise 5.3.4."""

def last_early(my_str):
    """Return whether the last character also occurs earlier, ignoring case."""
    text = my_str.lower()
    return bool(text) and text[-1] in text[:-1]

def main():
    print(last_early("happy birthday"))


if __name__ == "__main__":
    main()
