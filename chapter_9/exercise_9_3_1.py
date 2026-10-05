"""Campus IL self.py — exercise 9.3.1."""

def my_mp3_playlist(file_path):
    """Return longest song title, song count, and the most frequent artist."""
    with open(file_path, encoding="utf-8") as file:
        songs = [line.strip().split(";") for line in file if line.strip()]
    longest_song = ""
    longest_duration = -1
    artists = {}
    for title, artist, duration, *unused in songs:
        minutes, seconds = duration.split(":")
        duration_seconds = int(minutes) * 60 + int(seconds)
        if duration_seconds > longest_duration:
            longest_song, longest_duration = title, duration_seconds
        artists[artist] = artists.get(artist, 0) + 1
    return longest_song, len(songs), max(artists, key=artists.get)

def main():
    print(my_mp3_playlist(input("Enter a playlist path: ")))


if __name__ == "__main__":
    main()
