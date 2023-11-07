from typing import List, Tuple

from src.modules.gameboard.gameboard import GameTile


class Path:
    @staticmethod
    def word_points(path: Tuple[GameTile, ...]) -> int:
        """Get points value of actual word"""
        word_points = sum(node.points() for node in path)
        word_bonus = 10 if len(path) >= 6 else 0
        word_mult = 1

        for node in path:
            word_mult *= node.word_mult
        return word_points * word_mult + word_bonus

    @staticmethod
    def word_gems(path: Tuple[GameTile, ...]) -> int:
        """Get points value of actual word"""
        return sum(node.gems() for node in path)

    @staticmethod
    def get_path(
        path: Tuple[GameTile, ...], word: str, swaps: List[int]
    ) -> Tuple[GameTile, ...]:
        """Get a new path with swap nodes replaced"""
        if not swaps:
            return path

        return tuple(
            (node.copy(word[i]) if i in swaps else node) for i, node in enumerate(path)
        )
