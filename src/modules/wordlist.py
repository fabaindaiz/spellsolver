import os
from typing import Generator, Set, TextIO
from src.config import SOURCES, WORDLIST
from src.utils.utils import is_valid_word


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
        write_words_to_file(words, path=self.dest_path)

    def fetch_words_from_files(self) -> Set[str]:
        """
        Fetch valid words from a list of source files.

        Returns:
            Set[str]: A set containing valid words from source files.
        """
        words = set()
        for file in os.listdir(self.source_path):
            full_path = os.path.join(self.source_path, file)
            words.update(read_source_file(path=full_path))
        return words


def write_words_to_file(words: set, path: str) -> None:
    """
    Sort and write a set of valid words to a destination file.
    Args:
        words (set): A set of valid words to be written to the file.
        path (str): The path to the destination file.
    """
    sorted_words = sorted(words)
    with open(path, "w") as file:
        file.writelines(f"{word}\n" for word in sorted_words)


def read_source_file(path: str) -> Generator[str, None, None]:
    """
    Read valid words from a source file.

    Args:
        path (str): The path to the source file.

    Yields:
        Generator[str, None, None]: A generator yielding valid words from the source file.
    """
    with open(path) as file:
        for line in file:
            word = line.strip().lower()
            if is_valid_word(word):
                yield word
