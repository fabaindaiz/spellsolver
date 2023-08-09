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


class TrieNode:
    """Represents a node of a trie"""

    def __init__(self, leaf_class: TrieLeaf) -> None:
        self.childs: Dict[str, TrieNode] = {}
        self.leaf: TrieLeaf = leaf_class()

    def insert(self, leaf_class: type, iter_word: str, **kwargs: dict) -> None:
        """Insert a word recursively in the trie"""
        if iter_word == "":
            return self.leaf.insert(**kwargs)

        next_letter = iter_word[0]
        next_word = iter_word[1:]
        child = self.childs.setdefault(next_letter, TrieNode(leaf_class))
        child.insert(leaf_class, next_word, **kwargs)

    def get_letter(self, letter: str) -> "TrieNode":
        """Get node representing a letter in the trie"""
        return self.childs.get(letter, None)

    def get_node(self, word: str) -> "TrieNode":
        """Get node representing a word in the trie"""
        node = self
        for letter in word:
            if letter not in node.childs:
                return None
            node = node.childs.get(letter, None)
        return node

    def get_leaf(self, recursive=False, **kwargs: dict) -> Any:
        """Get content from trie leaf using kwargs"""
        words = self.leaf.get(**kwargs)
        if recursive:
            for node in self.childs.values():
                words += node.get_leaf(recursive=True, **kwargs)
        return words
