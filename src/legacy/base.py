from typing import Any, Dict


class TrieLeaf:
    """Interface that represents a leaf of a trie"""

    def insert(self, **kwargs: dict) -> None:
        """Insert kwargs value in TrieLeaf"""
        raise NotImplementedError()

    def get(self, **kwargs: dict) -> Any:
        """Get kwargs value from TrieLeaf"""
        raise NotImplementedError()

    def heuristic(self, **kwargs: dict) -> Any:
        """Get heuristic values from TrieLeaf"""
        raise NotImplementedError()
    
    def merge_leafs(self, leaf: "TrieLeaf") -> None:
        """Merge other_leaf into main_leaf"""
        raise NotImplementedError()


class TrieNode:
    """Represents a node of a trie"""

    def __init__(self, leaf_class: TrieLeaf) -> None:
        raise NotImplementedError()

    def insert(self, iter_word: str, **kwargs: dict) -> None:
        """Insert a word recursively in the trie"""
        raise NotImplementedError()
    
    def finish_insert(self) -> None:
        """Finish insertions in the trie"""
        pass

    def get_key(self, letter: str) -> "TrieNode":
        """Get node representing a letter in the trie"""
        raise NotImplementedError()

    def get_node(self, word: str) -> "TrieNode":
        """Get node representing a word in the trie"""
        raise NotImplementedError()

    def get_leaf(self, recursive=False, **kwargs: dict) -> Any:
        """Get content from trie leaf using kwargs"""
        raise NotImplementedError()
    
    def merge_tries(self, trie: "TrieNode") -> None:
        """Merge other_trie into main_trie"""
        raise NotImplementedError()

class Trie:

    def insert(self, word: str) -> None:
        """Insert a word in the trie"""
        raise NotImplementedError()
    
    def finish_insert(self) -> None:
        """Finish insertions in the trie"""
        raise NotImplementedError()
    
    def get_key(self, letter: str) -> "TrieNode":
        """Get node representing a letter in the trie"""
        raise NotImplementedError()

    def get_node(self, word: str) -> "TrieNode":
        """Get node representing a word in the trie"""
        raise NotImplementedError()

    def get_leaf(self, recursive=False, **kwargs: dict) -> Any:
        """Get content from trie leaf using kwargs"""
        raise NotImplementedError()
    
    def merge_tries(self, trie: "TrieNode") -> None:
        """Merge other_trie into main_trie"""
        raise NotImplementedError()
    
