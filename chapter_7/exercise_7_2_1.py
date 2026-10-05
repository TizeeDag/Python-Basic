"""Campus IL self.py — exercise 7.2.1."""

def is_greater(my_list, n):
    """Return a new list of items greater than n, preserving order."""
    result = []
    for item in my_list:
        if item > n:
            result.append(item)
    return result

def main():
    print(is_greater([1, 30, 25, 60, 27, 28], 28))


if __name__ == "__main__":
    main()
