from typing import Any, Dict, Generator, Tuple

from src.config import DEBUG, GEMS_MULT, WORD_MULT
from src.modules.gameboard.gameboard import GameTile


class ResultWord:
    """Represents a spellsolver result"""

    def __init__(
        self,
        points: int,
        gems: int,
        word: str,
        path: Tuple[GameTile, ...],
        swaps: Tuple[int] = [],
    ) -> None:
        self.points: int = points
        self.gems: int = gems
        self.word: str = word
        self.path: Tuple[GameTile, ...] = path
        self.swaps: Tuple[int] = swaps

    def order(self) -> int:
        """Order result by points & gems"""
        return self.points * WORD_MULT + self.gems * GEMS_MULT

    def _str(self) -> Generator[str, None, None]:
        yield f"{self.points} {self.word} {self.path[0].cord}"
        yield from (f"{self.word[swap]} {self.path[swap].cord}" for swap in self.swaps)

        if DEBUG:
            yield str([tile.__str__() for tile in self.path])

    def label(self) -> str:
        """Get label representation of result"""
        return f"{self.word.ljust(12)} {self.points}★ {self.gems}💎"

    def text(self) -> str:
        """Get text representation of result"""
        return f"({' | '.join(self._str())})"

    def dict(self) -> Dict[str, Any]:
        return {
            "points": self.points,
            "gems": self.gems,
            "word": self.word,
            "path": [node.cord for node in self.path],
            "swap": self.swaps,
        }
