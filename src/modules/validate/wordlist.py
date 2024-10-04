import os
from collections.abc import Generator
from typing import TextIO

from src import SOURCES, WORDLIST
from src.utils import resource_path
from .generate import WordGenerate


class WordList:
    def __init__(self):
        self.source = resource_path(SOURCES)
        self.destination = resource_path(WORDLIST)

    def open_file(self) -> TextIO:
        if not os.path.exists(self.destination):
            WordGenerate.generate_wordlist(
                source=self.source,
                destination=self.destination,
            )

        return open(self.destination, "r")

    def get_words(self) -> Generator[str, None, None]:
        with self.open_file() as file:
            for line in file:
                yield line.strip().lower()
