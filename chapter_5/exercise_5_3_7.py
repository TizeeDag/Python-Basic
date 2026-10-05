"""Campus IL self.py — exercise 5.3.7."""

def chocolate_maker(small, big, x):
    """Return whether 1 cm and 5 cm blocks can form exactly x centimeters."""
    used_big = min(big, x // 5)
    return x - used_big * 5 <= small

def main():
    print(chocolate_maker(3, 1, 8))


if __name__ == "__main__":
    main()
