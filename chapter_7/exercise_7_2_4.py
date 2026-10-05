"""Campus IL self.py — exercise 7.2.4."""

def seven_boom(end_number):
    """Replace multiples of seven and numbers containing 7 with BOOM."""
    result = []
    for number in range(end_number + 1):
        if number % 7 == 0 or "7" in str(number):
            result.append("BOOM")
        else:
            result.append(number)
    return result

def main():
    print(seven_boom(17))


if __name__ == "__main__":
    main()
