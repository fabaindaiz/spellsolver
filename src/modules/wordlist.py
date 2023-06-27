import os
from io import TextIOWrapper
from src.utils.utils import valid_word
from src.config import SOURCES, WORDLIST


class WordList:
    """"""
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
        """Generate a wordlist files from multiples filesin a source folder"""
        files = [os.path.join(self.source_path, file) for file in os.listdir(self.source_path)]
            
        words = set()
        for file in files:
            with open(file) as f:
                for word in f.readlines():
                    word = word[:-1].lower()
                    if valid_word(word):
                        words.add(word)

        words = sorted(words)
        with open(self.dest_path, 'w') as f:
            for word in words:
                f.write("%s\n" % word)
