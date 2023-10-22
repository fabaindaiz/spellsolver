from typing import Generator
from src.modules.wordlist.wordlist import WordList


class Trie:

    def insert_trie(self, loader: WordList) -> None:
        raise NotImplementedError()
    
    def query_trie(self) -> "TrieQuery":
        raise NotImplementedError()


class TrieQuery:
    
    def get_key(self, word: str) -> str:
        raise NotImplementedError()

    def get_leaf(self, word: str) -> Generator[str, None, None]:
        raise NotImplementedError()
