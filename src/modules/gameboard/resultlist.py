from collections.abc import Generator
from typing import Any

from src import CONSOLE
from src.utils import Timer
from .resultword import ResultWord


class ResultList:
    def __init__(self, timer: Timer = Timer()) -> None:
        self.timer: Timer = timer
        self.data: dict[tuple[int, str], ResultWord] = {}

    def update(self, results: Generator[ResultWord, None, None]) -> None:
        for result in results:
            self.data[(result.points, result.word)] = result

    def print_timer(self) -> None:
        elapsed_time = self.timer.elapsed_millis
        header = "The following words have been found"
        time_message = f"(elapsed time: {elapsed_time} milliseconds)"
        padding = " " * max(0, len(header) - len(time_message))

        print(f"{header} {padding} {time_message}")

    @property
    def sorted_words(self) -> list[ResultWord]:
        data_values = self.data.values()
        sorted_words = sorted(data_values, reverse=True, key=self.sort_tile)

        if CONSOLE:
            self.print_timer()
            top_words = sorted_words[:10]
            word_list = self.words_to_text(top_words)
            print(f"{word_list}")

        return sorted_words

    @staticmethod
    def sort_tile(tile: ResultWord) -> int:
        return tile.order

    @staticmethod
    def words_to_text(sorted_words: list[ResultWord]) -> str:
        words_text = []

        for word in sorted_words:
            words_text.append(word.text)

        return "\n".join(words_text)

    @staticmethod
    def words_to_dict(sorted_words: list[ResultWord]) -> list[dict[str, Any]]:
        word_dicts = []

        for word in sorted_words:
            word_dict = word.dict()
            word_dicts.append(word_dict)

        return word_dicts
