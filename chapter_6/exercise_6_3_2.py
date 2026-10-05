"""Campus IL self.py — exercise 6.3.2."""

def longest(my_list):
    """Return the longest string in a nonempty list."""
    return max(my_list, key=len)

def main():
    print(longest(["111", "234", "2000", "goru", "birthday", "09"]))


if __name__ == "__main__":
    main()
