from collections.abc import Generator
from typing import Any

from src import CONSOLE
from src.utils import Timer
from .resultword import ResultWord


class ResultList:
    def __init__(self, timer: Timer = None) -> None:
        self.data: dict[tuple[int, str], ResultWord] = {}
        self.timer: Timer = timer

    def update(self, results: Generator[ResultWord, None, None]) -> None:
        for result in results:
            self.data[(result.points, result.word)] = result

    def print_timer(self) -> None:
        elapsed_time = self.timer.elapsed_millis()

        print(
            f"The following words have been found (elapsed time: {elapsed_time} milliseconds)"
        )

    @property
    def sorted_words(self) -> list[ResultWord]:
        sorted_words = sorted(self.data.values(), reverse=True, key=self.sort_tile)

        if CONSOLE:
            self.print_timer()
            words = sorted_words[:10]
            word_list = self.words_to_text(words)
            print(f"[{word_list}]")

        return sorted_words

    @staticmethod
    def words_to_text(sorted_words: list[ResultWord]) -> str:
        return ", ".join(word.text for word in sorted_words)

    @staticmethod
    def words_to_dict(sorted_words: list[ResultWord]) -> list[dict[str, Any]]:
        return [word.dict() for word in sorted_words]

    @staticmethod
    def sort_tile(tile: ResultWord) -> int:
        return tile.order
