from typing import Generator, Iterable, Tuple
from itertools import combinations

from src.config import SWAP

    
def _iter(word, num):
    for t in combinations(range(len(word)), num):
        yield "".join("0" if i in t else word[i] for i in range(len(word)))

def swap_iter(word: str) -> Generator[str, None, None]:
        for num in range(SWAP + 1):
            for iword in _iter(word, num):
                yield iword

def word_iter(words: Generator[str, None, None]) -> Generator[str, None, None]:
    """Insert a chunk of words into the trie and return it"""
    for word in words:
        yield from swap_iter(word)

def pair_iter(words: Iterable[str]) -> Generator[Tuple[str, Tuple[int]], None, None]:
    """Insert a pair of words into the trie and return it"""
    for i, word in enumerate(words):
        for iword in swap_iter(word):
            yield iword, (i,)
