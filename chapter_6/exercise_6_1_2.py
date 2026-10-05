"""Campus IL self.py — exercise 6.1.2."""

def shift_left(my_list):
    """Return a new list rotated one position to the left."""
    return my_list[1:] + my_list[:1]

def main():
    print(shift_left([0, 1, 2]))


if __name__ == "__main__":
    main()
