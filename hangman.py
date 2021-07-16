
import random
import string
from blessed import Terminal

term = Terminal()

def get_word(f_name: str) -> str:
    """Function get_word selects random word from file f_name"""
    words = open(f_name).read().splitlines()
    return random.choice(words)


def clear_screen() -> None:
    print(term.clear+term.home)


def print_line(x: int, y: int, line: str) -> None:
    print(term.move_xy(x,y) + line)


def deal_with_misses(misses: int) -> int:
    """Deal with misses"""
    miss = [
    ".....│.............." ,  
    ".....│....O.........",      
    ".....│....|.........", 
    ".....│....|.........", 
    ".....│.../..........", 
    ".....│.../|.........", 
    ".....│.../|\........", 
    ".....│.../.\........"
    ]
    if misses == 1:
        print_line(0,1,miss[misses])
    if misses == 2:
        print_line(0,2,miss[misses])
    if misses == 3:
        print_line(0,3,miss[misses])
    if misses == 4:
        print_line(0,4,""+miss[misses])
    if misses == 5:
        print_line(0,2,miss[misses])
    elif misses == 6:
        print_line(0,2,miss[misses])
    elif misses == 7:
        print_line(0,4,miss[misses])


def erect_gallows() -> int:
    """Erect gallows"""
    gallows = [
    ".....┌────┐.........",
    ".....│..............",
    ".....│..............",
    ".....│..............",
    ".....│..............",
    "...┌─┴─────────┐....",
    "...│...........└──┐.",
    "...└──────────────┘.",
    ]
    height = len(gallows)
    for i in range(height):
        print_line(0,i,gallows[i])
    return height


def main() -> None:
    """Hangman"""
    x,y = term.width, term.height
    valid_chars = string.ascii_lowercase
##  ┌ ─ ┬ ┐ │ ├ ┼ ┤ └ ┴ ┘
    word = get_word("./data/wordlist.txt")
    guessed_word =len(word)*'-'
    guesses = ""
    misses = 0
    clear_screen()
    board_length = erect_gallows()
    print_line(1,board_length, f"Word: {guessed_word}: {word}")
    print_line(x-40,0,f"Used:")
    while(True):
        with term.cbreak():
            while(True):
                print_line(0,board_length + 1,"Guess:")
                guess = term.inkey()
                if guess in valid_chars and guess not in guesses:
                    print_line(0,board_length + 2," "*18)
                    break
                if guess in guesses:
                    print_line(0,board_length + 2,f"Already guessed {guess}.")
        guesses += guess
        guesses = "".join(sorted(guesses))
        print_line(x-34,0,guesses)
        if guess not in word:            
            misses += 1
            deal_with_misses(misses)
        else:
            temp = ""
            for i in range(len(word)):
                if guess == word[i]:
                    temp += guess
                else:
                    temp += guessed_word[i]
            guessed_word = temp
            print_line(1,board_length, f"Word: {guessed_word}: {word}")
            if guessed_word == word:
                print_line(0,10,"Winner, Winner Chicken Dinner!")
                break
        if misses == 7:
            print_line(0,10,"Lose!")
            break

if __name__ == '__main__':
    main()
