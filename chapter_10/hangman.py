"""Campus IL self.py final project: Hangman."""

HANGMAN_ASCII_ART = r"""Welcome to the game Hangman
    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \
   | |  | | (_| | | | | (_| | | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/"""
MAX_TRIES = 6


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


def check_valid_input(letter_guessed, old_letters_guessed):
    """Return whether the input is one English letter not already guessed."""
    letter = letter_guessed.lower()
    return len(letter) == 1 and "a" <= letter <= "z" and letter not in old_letters_guessed


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """Record a valid lowercase guess, or print X and the sorted old guesses."""
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower())
        return True
    print("X")
    print(" -> ".join(sorted(old_letters_guessed)))
    return False


def show_hidden_word(secret_word, old_letters_guessed):
    """Return guessed letters and underscores separated by single spaces."""
    result = []
    for letter in secret_word:
        if letter in old_letters_guessed:
            result.append(letter)
        else:
            result.append("_")
    return " ".join(result)


def check_win(secret_word, old_letters_guessed):
    """Return True when every letter in the secret word has been guessed."""
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True


def choose_word(file_path, index):
    """Return unique word count and the word at a circular, one-based index."""
    with open(file_path, encoding="utf-8") as file:
        words = file.read().split()
    return len(set(words)), words[(index - 1) % len(words)]


def hangman(secret_word):
    """Play Hangman until every letter is guessed or six wrong guesses occur."""
    secret_word = secret_word.lower()
    old_letters_guessed = []
    num_of_tries = 0
    print("Let's start!")
    print_hangman(num_of_tries)
    print(show_hidden_word(secret_word, old_letters_guessed))
    while num_of_tries < MAX_TRIES and not check_win(secret_word, old_letters_guessed):
        letter_guessed = input("Guess a letter: ")
        if not try_update_letter_guessed(letter_guessed, old_letters_guessed):
            continue
        if letter_guessed.lower() not in secret_word:
            num_of_tries += 1
            print(":(")
            print_hangman(num_of_tries)
        print(show_hidden_word(secret_word, old_letters_guessed))
    if check_win(secret_word, old_letters_guessed):
        print("WIN")
    else:
        print("LOSE")


def main():
    """Print the opening screen and select the secret word from a text file."""
    print(HANGMAN_ASCII_ART, MAX_TRIES, sep="\n")
    file_path = input("Enter file path: ")
    index = int(input("Enter index: "))
    secret_word = choose_word(file_path, index)[1]
    hangman(secret_word)


if __name__ == "__main__":
    main()
