"""Campus IL self.py — exercise 6.2.3."""

def format_list(my_list):
    """Format even-indexed items, then append the last item preceded by and."""
    return ", ".join(my_list[::2]) + ", and " + my_list[-1]

def main():
    print(format_list(["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]))


if __name__ == "__main__":
    main()
