"""Campus IL self.py — exercise 9.2.2."""

def copy_file_content(source, destination):
    """Copy a text file's content to destination, replacing previous content."""
    with open(source, encoding="utf-8", newline="") as file:
        content = file.read()
    with open(destination, "w", encoding="utf-8", newline="") as file:
        file.write(content)

def main():
    copy_file_content(input("Source file: "), input("Destination file: "))


if __name__ == "__main__":
    main()
