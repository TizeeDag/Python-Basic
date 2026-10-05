"""Campus IL self.py — exercise 7.1.4."""

def squared_numbers(start, stop):
    """Return squares from start through stop using a while loop."""
    squares = []
    while start <= stop:
        squares.append(start ** 2)
        start += 1
    return squares

def main():
    print(squared_numbers(-3, 3))


if __name__ == "__main__":
    main()
