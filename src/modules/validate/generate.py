import os
from typing import Callable, Generator

from src.utils.utils import is_valid_word


def fetch_single_file(path: str, validate: Callable[[str], bool]) -> Generator[str, None, None]:
    """
    Fetch valid words from a source file.

    Args:
        source (str): The path to the source file.

    Yields:
        Generator[str, None, None]: A generator yielding valid words from the source file.
    """
    with open(path) as file:
        for line in file:
            word = line.strip().lower()
            if validate(word):
                yield word

def fetch_multiple_files(path: str) -> Generator[str, None, None]:
    """
    Fetch valid words from a list of source files.

    Args:
        source (str): The path to the source folder.

    Yields:
        Generator[str, None, None]: A generator yielding valid words from source files.
    """
    words = set()
    for file in os.listdir(path):
        full_path = os.path.join(path, file)
        words.update(fetch_single_file(path=full_path, validate=is_valid_word))
    yield from words

def write_words_to_file(path: str, words: Generator[str, None, None], sort=False) -> None:
    """
    Sort and write a set of valid words to a destination file.
    Args:
        path (str): The path to the destination file.
        words (set): A set of valid words to be written to the file.
    """
    words = sorted(words) if sort else words
    with open(path, "w") as file:
        file.writelines(f"{word}\n" for word in words)

def generate_wordlist(source: str, destination: str) -> None:
    """
    Generate a wordlist file from multiple files in a source folder.

    Args:
        source (str): The path to the source folder.
        destination (str): The path to the destination file.
    """
    words = fetch_multiple_files(path=source)
    write_words_to_file(path=destination, words=words, sort=True)
    print("Wordlist file successfully generated from sources")
