"""Class to manage a Hangman word."""

from typing import List


class Word:
    """Word object"""

    def __init__(self, word: str):
        """Initialize the object with a word."""
        self.word = word.upper()
        self.guesses: List[str] = []  # Each item in list is a single character
        self.tries = 0

    def __str__(self) -> str:
        """Returns a printable string of word so far."""
        guesses = self._compute_guessed()
        characters = [x for x in guesses]
        replaced = ['_' if x.islower() else x for x in characters]
        return ' '.join(replaced)

    def _compute_guessed(self) -> str:
        """Private method to calculate how much of the word is guessed."""
        guessed = self.word.lower()
        for alphabet in self.guesses:
            guessed = guessed.replace(alphabet.lower(), alphabet.upper())
        return guessed

    def guess(self, alphabet: str) -> bool:
        """Guess a single alphabet, returning True if guess is good."""
        self.tries += 1
        if len(alphabet) == 1:
            alphabet = alphabet.upper()
            if alphabet in self.guesses:
                return False
            self.guesses.append(alphabet)
            if alphabet in self.word:
                return True
        return False

    def win(self) -> bool:
        """Compute whether the player won by guessing the whole word."""
        guessed = self._compute_guessed()
        if guessed == self.word:
            return True
        return False
