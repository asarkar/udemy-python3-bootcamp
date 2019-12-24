from typing import Counter, Dict


def rev(s: str) -> str:
    return s[::-1]


# https://en.wikipedia.org/wiki/Pig_Latin
def pig_latin(s: str) -> str:
    if s[0] in "aeiou":
        return f"{s}ay"
    return f"{s[1:]}{s[0]}ay"


def count_vowels(s: str) -> Dict[str, int]:
    # https://www.datacamp.com/community/tutorials/python-dictionary-comprehension
    return {k: v for k, v in Counter[str](s).items() if k in "aeiou"}


def is_palindrome(s: str) -> bool:
    mid = len(s) // 2
    indices = zip(range(mid + 1), range(len(s) - 1, mid, -1))

    return all(s[i] == s[j] for i, j in indices)
