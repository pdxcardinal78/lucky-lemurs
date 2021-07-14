import random
import string
from blessed import Terminal


def quote_translate(s: str) -> str:
    """Function quote_translate returns an encoded version of it's input

    Input: s: str
    Returns: s encoded with a random function
    """
    abc = string.ascii_uppercase
    mix = "".join(random.sample(abc, len(abc)))
    return s.translate(s.maketrans(abc, mix))


def read_quote(f_name: str) -> str:
    """Function read_quote reads in a text file

    Input: f_name - location of quote file
    Returns random quote from file f_name
    """
    lines = open(f_name).read().splitlines()
    return random.choice(lines).upper()


if __name__ == "__main__":
    quote = read_quote("./data/quotes.txt")
    encrypted = quote_translate(quote)
    print(quote)
    print(encrypted)
    term = Terminal()
