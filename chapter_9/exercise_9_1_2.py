"""Campus IL self.py — exercise 9.1.2."""

def main():
    file_path = input("Enter a file path: ")
    task = input("Enter a task: ")
    with open(file_path, encoding="utf-8") as file:
        lines = file.read().splitlines()
    if task == "sort":
        print(sorted(set(" ".join(lines).split())))
    elif task == "rev":
        for line in lines:
            print(line[::-1])
    elif task == "last":
        number = int(input("Enter a number: "))
        for line in lines[-number:]:
            print(line)


if __name__ == "__main__":
    main()
