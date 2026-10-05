"""Campus IL self.py — exercise 6.2.4."""

def extend_list_x(list_x, list_y):
    """Prepend list_y to list_x in place and return list_x."""
    list_x[:0] = list_y
    return list_x

def main():
    print(extend_list_x([4, 5, 6], [1, 2, 3]))


if __name__ == "__main__":
    main()
