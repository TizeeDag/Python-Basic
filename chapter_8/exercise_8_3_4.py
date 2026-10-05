"""Campus IL self.py — exercise 8.3.4."""

def inverse_dict(my_dict):
    """Invert a mapping and collect each value's original keys in sorted lists."""
    result = {}
    for key, value in my_dict.items():
        result.setdefault(value, []).append(key)
    for keys in result.values():
        keys.sort()
    return result

def main():
    print(inverse_dict({"I": 3, "love": 3, "self.py!": 2}))


if __name__ == "__main__":
    main()
