"""Campus IL self.py — exercise 9.1.1."""

def are_files_equal(file1, file2):
    """Return whether the two text files have identical content."""
    with open(file1, encoding="utf-8", newline="") as first:
        with open(file2, encoding="utf-8", newline="") as second:
            return first.read() == second.read()

def main():
    print(are_files_equal(input("First file: "), input("Second file: ")))


if __name__ == "__main__":
    main()
