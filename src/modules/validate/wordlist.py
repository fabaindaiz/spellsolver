import os
import sys
from typing import Generator, TextIO

from src.modules.validate.generate import generate_wordlist
from src.config import SOURCES, WORDLIST


def resource_path(relative_path: str) -> str:
    """Obtener la ruta absoluta al recurso en el sistema de archivos."""
    try:
        # PyInstaller crea un archivo temporal y lo coloca en _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)


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
        self.source = resource_path(SOURCES)
        self.destination = resource_path(WORDLIST)

    def open_file(self) -> TextIO:
        """
        Load a wordlist file, generate it if it doesn't exist.

        Returns:
            TextIO: A file object representing the opened wordlist file.
        """
        if not os.path.exists(self.destination):
            generate_wordlist(source=self.source, destination=self.destination)
        return open(self.destination, "r")
    
    def get_words(self) -> Generator[str, None, None]:
        """
        Get the next word from the wordlist file.

        Returns:
            Generator[str, None, None]: A generator that yields the next word.
        """
        file = self.open_file()
        for line in file:
            yield line.strip().lower()
        file.close()
