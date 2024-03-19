import os
from collections.abc import Generator
from typing import Callable

from src.utils import is_valid_word

type WordGenerator = Generator[str, None, None]
type WordValidator = Callable[[str], bool]


class WordGenerate:
    @staticmethod
    def fetch_single_file(path: str, validator: WordValidator) -> WordGenerator:
        with open(path) as file:
            for line in file:
                word = line.strip().lower()

                if validator(word):
                    yield word

    @staticmethod
    def fetch_multiple_files(path: str) -> WordGenerator:
        words: set[str] = set()

        for file in os.listdir(path):
            full_path = os.path.join(path, file)
            fetched_file = WordGenerate.fetch_single_file(full_path, is_valid_word)

            words.update(fetched_file)

        yield from words

    @staticmethod
    def write_words_to_file(path: str, words: WordGenerator, sort=False) -> None:
        if sort:
            sorted_words = sorted(words)
        else:
            sorted_words = words

        with open(path, "w") as file:
            for word in sorted_words:
                file.write(f"{word}\n")

    @staticmethod
    def generate_wordlist(source: str, destination: str) -> None:
        words = WordGenerate.fetch_multiple_files(path=source)

        WordGenerate.write_words_to_file(path=destination, words=words, sort=True)
        print("Wordlist file successfully generated from sources")
