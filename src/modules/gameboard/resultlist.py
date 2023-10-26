from typing import Any, Dict, Generator, List, Tuple

from src.modules.gameboard.resultword import ResultWord
from src.utils.timer import Timer


class ResultList:
    """Represents a result list"""

    def __init__(self, timer: Timer = None) -> None:
        self.data: Dict[Tuple[int, str], ResultWord] = {}
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
