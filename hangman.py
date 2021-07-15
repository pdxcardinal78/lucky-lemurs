"""Test out wordclass."""

import random

from wordclass import Word

WORD_FILE = "./data/words.txt"


def get_word_from_file() -> str:
    """Retrieve a random word longer than four characters from word file."""
    words = open(WORD_FILE, 'r').read().splitlines()
    word = ''
    while not word:
        word = random.choice(words)
        if len(word) <= 4:
            word = ''
    return word


word = Word(get_word_from_file())
# print(f"Try to guess the word '{word.word}'")

print("Let's play Hangman!")

while not word.win():
    print(word)
    char = input("Type a single character: ")
    if word.guess(char):
        print("You guessed right.")
    else:
        print("Try again.")
    print(f"Tried {word.tries} times - Guesses so far: {word.guesses}")
    print()

print(f"We have a winner: {word}")
