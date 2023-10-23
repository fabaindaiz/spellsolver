from typing import Any, Generator, Tuple

from src.modules.validate.wordlist import WordList


class Trie:
    """Represents a Patricia Trie"""

    def insert_trie(self, loader: WordList) -> None:
        """Insert the words from the loader into the trie"""
        raise NotImplementedError()
    
    def query_trie(self) -> "TrieQuery":
        """Obtains an object that allows queries to be made to the trie"""
        raise NotImplementedError()


class TrieQuery:
    """Represents a Patricia Trie Query"""

    def get_root(self) -> Any:
        """Obtains a representation of the base node of the trie"""
        return NotImplementedError()
    
    def get_key(self, node: Any, letter: str) -> Tuple[Any, str]:
        """Obtains the key associated with a letter from a node"""
        raise NotImplementedError()

    def get_leaf(self, node: Any) -> Generator[str, None, None]:
        """Gets the words associated with a node"""
        raise NotImplementedError()
