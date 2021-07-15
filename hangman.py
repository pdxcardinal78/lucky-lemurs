"""Test out wordclass."""

from wordclass import Word

word = Word("Apple")
print(f"Try to guess the word '{word.word}'")

while not word.win():
    print(word)
    char = input("Type a single character: ")
    if word.guess(char):
        print("You guessed right.")
    else:
        print("Try again.")
    print(f"Tried {word.tries} times - Guesses so far: {word.guesses}")

print(f"We have a winner: {word}")
