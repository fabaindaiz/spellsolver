from typing import Tuple


def get_coordinate(aux_cord: int) -> Tuple[int]:
    """Get a coordinate from a aux_cord"""
    aux_cord = aux_cord % 25
    return (aux_cord % 5, aux_cord // 5)


chars = "abcdefghijklmnopqrstuvwxyz"

def valid_word(word: str) -> bool:
    """Verify if a word is a valid word"""
    for letter in word:
        if letter not in chars:
            return False
    return True


points = {'a': 1, 'b': 4, 'c': 5, 'd': 3, 'e': 1, 'f': 5, 'g': 3, 'h': 4, 'i': 1, 'j': 7, 'k': 6, 'l': 3, 'm': 4,
    'n': 2, 'o': 1, 'p': 4, 'q': 8, 'r': 2, 's': 2, 't': 2, 'u': 4, 'v': 5, 'w': 5, 'x': 7, 'y': 4, 'z': 8, '': 0}

def letter_points(letter: str) -> int:
    """Gets points value of a letter"""
    return points[letter]
