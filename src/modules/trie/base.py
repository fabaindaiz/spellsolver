from typing import Generator, List
from src.modules.wordlist.wordlist import WordList


class Trie:

    def insert_trie(self, loader: WordList) -> None:
        raise NotImplementedError()
    
    def query_trie(self) -> "TrieQuery":
        raise NotImplementedError()


class TrieQuery:
    
    pass