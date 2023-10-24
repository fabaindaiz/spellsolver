from typing import Any, Dict, Generator, List, Tuple

from src.modules.gameboard.gameboard import GameTile
from src.config import DEBUG


class ResultWord:
    """Represents a spellsolver result"""

    def __init__(
        self, points: int, word: str, path: Tuple[GameTile, ...], swaps: List[int] = []
    ) -> None:
        self.points: int = points
        self.word: str = word
        self.path: Tuple[GameTile, ...] = path
        self.swaps: List[int] = swaps

    def _str(self) -> Generator[str, None, None]:
        yield f"{self.points} {self.word} {self.path[0].cord}"
        yield from (f"{self.word[swap]} {self.path[swap].cord}" for swap in self.swaps)

        if DEBUG:
            yield str([tile.__str__() for tile in self.path])

    def text(self, console: bool = False) -> str:
        """Get text representation of result"""
        if not console:
            return f"{self.points} {self.word}"

        # Console prints
        word = " | ".join(self._str())
        return f"({word})"

    def dict(self) -> Dict[str, Any]:
        return {
            "points": self.points,
            "word": self.word,
            "path": [node.cord for node in self.path],
            "swap": self.swaps,
        }
