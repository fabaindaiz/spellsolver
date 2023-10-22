from typing import List, Tuple
from src.modules.gameboard.gameboard import GameTile


class Path:
    """Represents a path of GameTiles forming a word"""

    def __init__(self, path: List[GameTile]) -> None:
        self.path: List[GameTile] = path
        self.reduced_path = self.path[1:]

    def path_tuple(self) -> Tuple[GameTile, ...]:
        """Get a tuple with the path nodes"""
        return tuple(self.reduced_path)

    def word_points(self) -> int:
        """Get points value of actual word"""
        word_points = sum(node.points() for node in self.reduced_path)
        word_bonus = 10 if len(self.reduced_path) >= 6 else 0
        word_mult = 1

        for node in self.reduced_path:
            word_mult *= node.word_mult
        return word_points * word_mult + word_bonus

    def swap_index(self, word: str, swaps: List[int]) -> "Path":
        """Get a new path with swap nodes replaced"""
        if not swaps:
            return self

        new_path = self.path.copy()
        for index in swaps:
            letter = word[index]
            node = self.path[index + 1]
            new_path[index + 1] = node.copy(letter)

        return Path(new_path)
