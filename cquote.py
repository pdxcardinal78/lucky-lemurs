import random


def translate(s: str) -> str:
    """Exchanges alphabetic characters in string s and returns a copy"""
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cba = "".join(random.sample(abc, len(abc)))
##    bob = s.maketrans(abc, cba)
    return s.translate(s.maketrans(abc, cba))


def cquote() -> None:
    """Function cquote is a function."""
    f_name = "./data/quotes.txt"
    lines = open(f_name).read().splitlines()
    quote = random.choice(lines).upper()
##  Translate
    print(translate(quote))
    print(quote)


if __name__ == "__main__":
    cquote()
