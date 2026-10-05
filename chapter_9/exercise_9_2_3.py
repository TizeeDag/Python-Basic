"""Campus IL self.py — exercise 9.2.3."""

def who_is_missing(file_name):
    """Find the missing integer from 1..n and write it to found.txt."""
    with open(file_name, encoding="utf-8") as file:
        numbers = [int(number) for number in file.read().split(",")]
    n = len(numbers) + 1
    missing = n * (n + 1) // 2 - sum(numbers)
    with open("found.txt", "w", encoding="utf-8") as file:
        file.write(str(missing))
    return missing

def main():
    print(who_is_missing(input("Enter a file path: ")))


if __name__ == "__main__":
    main()
