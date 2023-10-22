from typing import Any, Dict, Generator, List, Tuple

from src.modules.gameboard.gameboard import GameTile
from src.utils.timer import Timer


class ResultList:
    """Represents a result list"""

    def __init__(self, timer: Timer = None) -> None:
        self.data: Dict[str, ResultWord] = {}
        self.timer: Timer = timer

    def update(self, results: Generator["ResultWord", None, None]) -> None:
        """Update result list"""
        for res in results:
            self.data[(res.points, res.word)] = res

    def sorted(self, console: bool = False) -> List["ResultWord"]:
        """Return result list sorted by points"""
        sorted_data = sorted(self.data.values(), reverse=True, key=lambda x: x.points)
        if console:
            sorted_list = ", ".join(
                word.text(console=console) for word in sorted_data[:10]
            )
            print(
                f"The following words have been found (elapsed time: {self.timer.elapsed_millis()} milliseconds)"
            )
            print(f"[{sorted_list}]")
        return sorted_data

    def sorted_dict(self) -> List[Dict[str, Any]]:
        sorted_data = sorted(self.data.values(), reverse=True, key=lambda x: x.points)
        return [word.dict() for word in sorted_data[:10]]


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
