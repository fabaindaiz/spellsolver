from typing import Any, Dict, Optional


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
    """Represents a node of a Patricia trie"""

    def __init__(self, leaf_class: TrieLeaf, value: Optional[str] = None) -> None:
        self.children: Dict[str, TrieNode] = {}
        self.value: str = value or ""
        self.leaf: TrieLeaf = leaf_class()

    def insert(self, iter_word: str, **kwargs: dict) -> None:
        """Insert a word recursively in the trie"""
        if not iter_word:
            return self.leaf.insert(**kwargs)

        # Find common prefix
        i = 0
        while i < len(iter_word) and i < len(self.value) and iter_word[i] == self.value[i]:
            i += 1

        # Split if needed
        if i < len(self.value):
            child = TrieNode(type(self.leaf), self.value[i:])
            child.children, child.leaf, self.children, self.leaf = self.children, self.leaf, {self.value[i]: child}, type(self.leaf)()
            
        # Recursive insertion
        if i < len(iter_word):
            next_key = iter_word[i]
            if next_key not in self.children:
                self.children[next_key] = TrieNode(type(self.leaf), iter_word[i:])
            else:
                self.children[next_key].insert(iter_word[i:], **kwargs)
        else:
            self.leaf.insert(**kwargs)

    def get_node(self, word: str) -> "TrieNode":
        """Get node representing a word in the trie"""
        node = self
        while word:
            # If word is not a prefix of value, then node is not found
            if not word.startswith(node.value):
                return None
            word = word[len(node.value):]
            if not word:
                return node
            next_key = word[0]
            if next_key not in node.children:
                return None
            node = node.children[next_key]
        return node

    def get_leaf(self, recursive=False, **kwargs: dict) -> Any:
        """Get content from trie leaf using kwargs"""
        words = self.leaf.get(**kwargs)
        if recursive:
            for node in self.children.values():
                words += node.get_leaf(recursive=True, **kwargs)
        return words