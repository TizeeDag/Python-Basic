"""Campus IL self.py — exercise 8.3.3."""

def count_chars(my_str):
    """Count each character except space, preserving first appearance order."""
    result = {}
    for char in my_str:
        if char != " ":
            result[char] = result.get(char, 0) + 1
    return result

def main():
    print(count_chars("abra cadabra"))


if __name__ == "__main__":
    main()
