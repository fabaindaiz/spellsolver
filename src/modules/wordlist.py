import os
from io import TextIOWrapper
from typing import Generator, Set
from src.utils.utils import valid_word
from src.config import SOURCES, WORDLIST


class WordList:
    """Represents a class that can generate and load a wordlist file for Spellsolver"""

    def __init__(self) -> None:
        self.source_path: str = SOURCES
        self.dest_path: str = WORDLIST

    def open_file(self) -> TextIOWrapper:
        """Load a wordlist file, if it doesn't exist it is generated"""
        if not os.path.isfile(self.dest_path):
            self.generate_wordlist()
            print("Wordlist file successfully generated from sources")

        return open(self.dest_path)

    def generate_wordlist(self) -> None:
        """Generate a wordlist files from multiples files in a source folder"""
        files = (
            os.path.join(self.source_path, file)
            for file in os.listdir(self.source_path)
        )
        words = set()

        for file in files:
            words.update(self.read_source_file(path=file))

        self.write_dest_file(words=words, path=self.dest_path)

    def read_source_file(self, path: str) -> Generator[str, None, None]:
        """Read all valid words from a source file"""
        with open(path) as file:
            return (
                word
                for word in (line[:-1].lower() for line in file.readlines())
                if valid_word(word)
            )

    def write_dest_file(self, words: Set[str], path: str) -> None:
        """Sorts valid words and writes them to a destination file"""
        words = sorted(words)
        with open(path, "w") as f:
            for word in words:
                f.write("%s\n" % word)
