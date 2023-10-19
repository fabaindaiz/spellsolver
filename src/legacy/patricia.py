from typing import Any, Dict
from src.tries.base import TrieLeaf, TrieNode


class PatriciaLeaf(TrieLeaf):
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


class PatriciaNode(TrieNode):
    """Represents a node of a Patricia trie"""

    def __init__(self, leaf_class: TrieLeaf) -> None:
        self.childs: Dict[str, TrieNode] = {}
        self.leaf: TrieLeaf = leaf_class()

    def insert(self, iter_word: str, **kwargs: dict) -> None:
        """Insert a word recursively in the trie"""
        if not iter_word:
            return self.leaf.insert(**kwargs)

        common_prefix = next((prefix for prefix in self.childs.keys() if iter_word.startswith(prefix)), None)
        if common_prefix:
            next_word = iter_word[len(common_prefix):]
            child = self.childs[common_prefix]
        else:
            common_prefix = iter_word[0]
            next_word = iter_word[1:]
            child = self.childs.setdefault(common_prefix, TrieNode(type(self.leaf)))

        child.insert(next_word, **kwargs)

    def get_key(self, letter: str) -> "TrieNode":
        next((key for key in self.childs if key.startswith(letter)), None)

    def get_node(self, word: str) -> "TrieNode":
        """Get node representing a word in the trie"""
        node = self
        while word:
            prefix = next((p for p in node.childs.keys() if word.startswith(p)), None)
            if not prefix:
                return None
            node = node.childs[prefix]
            word = word[len(prefix):]
        return node

    def get_leaf(self, recursive=False, **kwargs: dict) -> Any:
        """Get content from trie leaf using kwargs"""
        words = self.leaf.get(**kwargs)
        if recursive:
            for node in self.childs.values():
                words += node.get_leaf(recursive=True, **kwargs)
        return words
    
    def merge_tries(self, trie: "TrieNode") -> None:
        """Merge other_trie into main_trie"""
        self.leaf.merge_leafs(trie.leaf)

        for prefix, child in trie.childs.items():
            if prefix in self.childs:
                self.childs[prefix].merge_tries(child)
            else:
                self.childs[prefix] = child
