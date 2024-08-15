import random

def display_hangman(tries):
    """Displays the hangman stage based on the number of tries remaining."""
    stages = [
        """
        --------
        |       |
        |       O
        |      /|\
        |       |
        |      / \
        |
        """,
        """
        --------
        |       |
        |       O
        |      /|\
        |       |
        |       /
        |
        """,
        """
        --------
        |       |
        |       O
        |      /|\
        |       |
        |
        |
        """,
        """
        --------
        |       |
        |       O
        |      /|
        |       |
        |
        |
        """,
        """
        --------
        |       |
        |       O
        |       |
        |       |
        |
        |
        """,
        """
        --------
        |       |
        |       O
        |
        |
        |
        |
        """,
        """
        --------
        |       |
        |
        |
        |
        |
        |
        """
    ]
    return stages[tries]

def get_word():
    """Returns a randomly chosen word from the word list."""
    words = ['python', 'java', 'kotlin', 'javascript']
    return random.choice(words).upper()

def play_hangman():
    """Main game loop for hangman."""
    word = get_word()
    guessed_word = "_" * len(word)
    guessed_letters = set()
    guessed_words = set()
    tries = 6

    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(guessed_word)
    print("\n")

    while not guessed_word == word and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed the letter {guess}")
            elif guess not in word:
                print(f"{guess} is not in the word.")
                tries -= 1
                guessed_letters.add(guess)
            else:
                print(f"Good job! {guess} is in the word!")
                guessed_letters.add(guess)
                guessed_word = ''.join(
                    guess if letter == guess else char
                    for letter, char in zip(word, guessed_word)
                )
                if '_' not in guessed_word:
                    guessed_word = word
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"You already guessed the word {guess}")
            elif guess != word:
                print(f"{guess} is not the word.")
                tries -= 1
                guessed_words.add(guess)
            else:
                guessed_word = word
        else:
            print("Not a valid guess.")

        print(display_hangman(tries))
        print(guessed_word)
        print("\n")

    if guessed_word == word:
        print("Congratulations, you guessed the word! You win!")
    else:
        print(f"Sorry, you ran out of tries. The word was {word}. Maybe next time!")

if __name__ == "__main__":
    play_hangman()
