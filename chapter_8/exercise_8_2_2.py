"""Campus IL self.py — exercise 8.2.2."""

def sort_prices(list_of_tuples):
    """Return item/price tuples sorted by numeric price, highest first."""
    return sorted(list_of_tuples, key=lambda item: float(item[1]), reverse=True)

def main():
    print(sort_prices([("milk", "5.5"), ("candy", "2.5"), ("bread", "9.0")]))


if __name__ == "__main__":
    main()
