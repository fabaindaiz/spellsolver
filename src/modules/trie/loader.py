from typing import List, Generator
from itertools import combinations
from src.config import SWAP

    
def _word_iter(word, num):
    for t in combinations(range(len(word)), num):
        yield "".join("0" if i in t else word[i] for i in range(len(word)))

def word_iter(word: str) -> Generator[str, None, None]:
        for num in range(SWAP + 1):
            for iword in _word_iter(word, num):
                yield iword

def chunk_iter(words: Generator[str, None, None]) -> Generator[str, None, None]:
    """Insert a chunk of words into the trie and return it"""
    for word in words:
        yield from word_iter(word)
