from itertools import combinations
from typing import Generator, Iterable, Tuple


def _iter(word, num):
    for t in combinations(range(len(word)), num):
        yield "".join("0" if i in t else word[i] for i in range(len(word)))


def swap_iter(word: str, swap: int) -> Generator[str, None, None]:
    for num in range(swap + 1):
        for iword in _iter(word, num):
            yield iword


def word_iter(words: Generator[str, None, None], swap) -> Generator[str, None, None]:
    """Insert a chunk of words into the trie and return it"""
    for word in words:
        yield from swap_iter(word, swap)


def pair_iter(
    words: Iterable[str], swap
) -> Generator[Tuple[str, Tuple[int]], None, None]:
    """Insert a pair of words into the trie and return it"""
    for i, word in enumerate(words):
        for iword in swap_iter(word, swap):
            yield iword, (i,)
