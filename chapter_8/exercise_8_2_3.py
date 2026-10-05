"""Campus IL self.py — exercise 8.2.3."""

def mult_tuple(tuple1, tuple2):
    """Return every cross-product pair followed by the same pair reversed."""
    result = []
    for first in tuple1:
        for second in tuple2:
            result.append((first, second))
            result.append((second, first))
    return tuple(result)

def main():
    print(mult_tuple((1, 2), (4, 5)))


if __name__ == "__main__":
    main()
