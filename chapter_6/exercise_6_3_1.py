"""Campus IL self.py — exercise 6.3.1."""

def are_lists_equal(list1, list2):
    """Compare numeric lists ignoring order while preserving multiplicities."""
    return sorted(list1) == sorted(list2)

def main():
    print(are_lists_equal([0.6, 1, 2, 3], [3, 2, 0.6, 1]))


if __name__ == "__main__":
    main()
