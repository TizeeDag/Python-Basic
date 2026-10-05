"""Campus IL self.py — exercise 7.2.7."""

def arrow(my_char, max_length):
    """Return a spaced character arrow with max_length characters at its center."""
    lines = []
    for length in range(1, max_length + 1):
        lines.append(" ".join([my_char] * length))
    for length in range(max_length - 1, 0, -1):
        lines.append(" ".join([my_char] * length))
    return "\n".join(lines)

def main():
    print(arrow("*", 5))


if __name__ == "__main__":
    main()
