from itertools import tee
from typing import Iterable


def pairwise(iterable: Iterable) -> Iterable:
    """
    Generate pairs of consecutive elements from an iterable.

    This function takes an iterable and returns an iterator that generates
    pairs of consecutive elements from the input iterable. Each pair consists
    of two adjacent elements. The input iterable is consumed in a single pass.

    Args:
        iterable (Iterable): An iterable sequence of elements.

    Yields:
        Iterable: An iterator that yields pairs of consecutive elements.

    Example:
        >>> list(pairwise('ABCDEFG'))
        [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F'), ('F', 'G')]
    """
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)
