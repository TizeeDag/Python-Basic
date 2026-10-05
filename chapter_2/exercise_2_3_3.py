"""Campus IL self.py — exercise 2.3.3."""

def main():
    number = int(input("Enter three digits (each digit for one pig): "))
    total = number // 100 + number // 10 % 10 + number % 10
    print(total)
    print(total // 3)
    print(total % 3)
    print(total % 3 == 0)


if __name__ == "__main__":
    main()
