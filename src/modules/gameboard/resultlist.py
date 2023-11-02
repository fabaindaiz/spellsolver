from typing import Any, Dict, Generator, List, Tuple

from src.modules.gameboard.resultword import ResultWord
from src.modules.gameboard.gametile import GameTile
from src.utils.timer import Timer
from src.config import GEMS_MULT, WORD_MULT


class ResultList:
    """Represents a result list"""

    def __init__(self, timer: Timer = None) -> None:
        self.data: Dict[Tuple[int, str], ResultWord] = {}
        self.timer: Timer = timer

    def update(self, results: Generator[ResultWord, None, None]) -> None:
        """Update result list"""
        for res in results:
            self.data[(res.points, res.word)] = res
    
    def print_timer(self) -> None:
        """Print elapsed time"""
        print(
            f"The following words have been found (elapsed time: {self.timer.elapsed_millis()} milliseconds)"
        )
    
    def sorted_words(self) -> List[ResultWord]:
        """Return sorted list with result words"""
        return sorted(self.data.values(), reverse=True, key=self.sort_tile)
    
    @staticmethod
    def words_to_text(sorted_words: List[ResultWord]) -> str:
        """Return result list sorted by points"""
        return ", ".join(word.text() for word in sorted_words[:10])

    @staticmethod
    def words_to_dict(sorted_words: List[ResultWord]) -> List[Dict[str, Any]]:
        """Return result list sorted by points"""
        return [word.dict() for word in sorted_words[:10]]
    
    @staticmethod
    def sort_tile(tile: GameTile) -> int:
        """Sort tiles by gems & points"""
        return tile.gems * GEMS_MULT + tile.points * WORD_MULT
