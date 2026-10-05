"""Campus IL self.py — exercise 1.4.1."""

from random import randint


def main():
    print("Welcome to the game Hangman")
    print(r"""    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \
   | |  | | (_| | | | | (_| | | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/""")
    print(randint(5, 10))


if __name__ == "__main__":
    main()
