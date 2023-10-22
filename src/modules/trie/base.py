from typing import Any, Generator, Tuple
from src.modules.wordlist.wordlist import WordList


class Trie:

    def insert_trie(self, loader: WordList) -> None:
        raise NotImplementedError()
    
    def query_trie(self) -> "TrieQuery":
        raise NotImplementedError()


class TrieQuery:

    def get_status(self) -> Any:
        return NotImplementedError()
    
    def get_key(self, status: Any, word: str) -> Tuple[Any, str]:
        raise NotImplementedError()

    def get_leaf(self, status: Any, word: str) -> Generator[str, None, None]:
        raise NotImplementedError()
