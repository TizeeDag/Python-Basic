"""Campus IL self.py — exercise 8.4.1."""

HANGMAN_PHOTOS = {0: 'x-------x',
 1: 'x-------x\n|\n|\n|\n|\n|',
 2: 'x-------x\n|       |\n|       0\n|\n|\n|',
 3: 'x-------x\n|       |\n|       0\n|       |\n|\n|',
 4: 'x-------x\n|       |\n|       0\n|      /|\\\n|\n|',
 5: 'x-------x\n|       |\n|       0\n|      /|\\\n|      /\n|',
 6: 'x-------x\n|       |\n|       0\n|      /|\\\n|      / \\\n|'}


def print_hangman(num_of_tries):
    """Print the Hangman picture for 0 through 6 failed guesses."""
    print(HANGMAN_PHOTOS[num_of_tries])

def main():
    print_hangman(6)


if __name__ == "__main__":
    main()
