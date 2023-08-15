import os
from typing import Generator, Set, TextIO
from src.config import SOURCES, WORDLIST
from src.utils.utils import valid_word


class WordList:
    """
    Represents a class that can generate and load a wordlist file for Spellsolver.

    Attributes:
        source_path (str): The path to the folder containing source files.
        dest_path (str): The path to the destination wordlist file.
    """

    def __init__(self):
        """
        Initialize a WordList object with source and destination paths.
        """
        self.source_path = SOURCES
        self.dest_path = WORDLIST

    def open_file(self) -> TextIO:
        """
        Load a wordlist file, generate it if it doesn't exist.

        Returns:
            TextIO: A file object representing the opened wordlist file.
        """
        if not os.path.isfile(self.dest_path):
            self.generate_wordlist()
            print("Wordlist file successfully generated from sources")
        return open(self.dest_path)

    def generate_wordlist(self) -> None:
        """
        Generate a wordlist file from multiple files in a source folder.
        """
        words = self.fetch_words_from_files()
        self.write_words_to_file(words, path=self.dest_path)

    def fetch_words_from_files(self) -> Set[str]:
        """
        Fetch valid words from a list of source files.

        Returns:
            Set[str]: A set containing valid words from source files.
        """
        words = set()
        for file in os.listdir(self.source_path):
            words.update(
                self.read_source_file(path=os.path.join(self.source_path, file))
            )
        return words

    @staticmethod
    def read_source_file(path: str) -> Generator[str, None, None]:
        """
        Read valid words from a source file.

        Args:
            path (str): The path to the source file.

        Yields:
            Generator[str, None, None]: A generator yielding valid words from the source file.
        """
        with open(path) as file:
            for line in file.readlines():
                word = line.strip().lower()
                if valid_word(word):
                    yield word

    @staticmethod
    def write_words_to_file(words: Set[str], path: str) -> None:
        """
        Sort valid words and write them to a destination file.

        Args:
            words (Set[str]): A set of valid words to be written to the file.
            path (str): The path to the destination file.
        """
        words = sorted(words)
        with open(path, "w") as f:
            for word in words:
                f.write("%s\n" % word)
