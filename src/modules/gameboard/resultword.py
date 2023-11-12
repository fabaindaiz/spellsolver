from collections.abc import Generator
from typing import Any

from src import DEBUG, GEMS_MULT, WORD_MULT
from .gametile import GameTile


class ResultWord:
    def __init__(
        self,
        points: int,
        gems: int,
        word: str,
        path: tuple[GameTile, ...],
        swaps: tuple[int, ...],
    ) -> None:
        self.points: int = points
        self.gems: int = gems
        self.word: str = word
        self.path: tuple[GameTile, ...] = path
        self.swaps: tuple[int, ...] = swaps

    @property
    def order(self) -> int:
        return self.points * WORD_MULT + self.gems * GEMS_MULT

    def _str(self) -> Generator[str, None, None]:
        yield f"{self.points} {self.word} {self.path[0].coordinates}"
        yield from (
            f"{self.word[swap]} {self.path[swap].coordinates}" for swap in self.swaps
        )

        if DEBUG:
            yield str([tile.__str__() for tile in self.path])

    @property
    def label(self) -> str:
        return f"{self.word.ljust(12)} {self.points}★ {self.gems}💎"

    @property
    def text(self) -> str:
        return f"({' | '.join(self._str())})"

    def dict(self) -> dict[str, Any]:
        return {
            "points": self.points,
            "gems": self.gems,
            "word": self.word,
            "path": [node.coordinates for node in self.path],
            "swap": self.swaps,
        }
