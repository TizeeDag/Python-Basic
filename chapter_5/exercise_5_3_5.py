"""Campus IL self.py — exercise 5.3.5."""

def distance(num1, num2, num3):
    """Return whether one number is close to num1 and the other is far away."""
    return ((abs(num1 - num2) == 1 and abs(num1 - num3) >= 2
             and abs(num2 - num3) >= 2)
            or (abs(num1 - num3) == 1 and abs(num1 - num2) >= 2
                and abs(num2 - num3) >= 2))

def main():
    print(distance(1, 2, 10))


if __name__ == "__main__":
    main()
