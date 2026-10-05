"""Campus IL self.py — exercise 7.2.5."""

def sequence_del(my_str):
    """Collapse each run of identical characters into one character."""
    result = ""
    for char in my_str:
        if not result or result[-1] != char:
            result += char
    return result

def main():
    print(sequence_del("ppyyyyythhhhhooonnnnn"))


if __name__ == "__main__":
    main()
