from itertools import tee
from typing import Iterable


def pairwise(iterable: Iterable) -> Iterable:
    """pairwise('ABCDEFG') --> AB BC CD DE EF FG"""
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)