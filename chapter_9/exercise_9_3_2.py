"""Campus IL self.py — exercise 9.3.2."""

def my_mp4_playlist(file_path, new_song):
    """Replace the third line's song title, pad short files, and print content."""
    with open(file_path, encoding="utf-8") as file:
        lines = file.read().splitlines()
    while len(lines) < 3:
        lines.append("")
    fields = lines[2].split(";")
    fields[0] = new_song
    lines[2] = ";".join(fields)
    content = "\n".join(lines) + "\n"
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)
    print(content, end="")

def main():
    my_mp4_playlist(input("Enter a playlist path: "), input("Enter a new song: "))


if __name__ == "__main__":
    main()
