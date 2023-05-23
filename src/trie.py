

class TrieLeaf:
    """Interface that represents a leaf of a trie"""

    def insert(**kwargs: dict) -> None:
        """Insert kwargs value in TrieLeaf"""
        pass

    def get(**kwargs: dict) -> list[str]:
        """Get kwargs value in TrieLeaf"""
        pass

class TrieNode:
    """Represents a node of a trie"""
    def __init__(self, letter: str, leaf_class: TrieLeaf) -> None:
        self.letter: str = letter
        self.childs: dict[str, TrieNode] = {}

        self.leaf_class: type = leaf_class
        self.leaf: TrieLeaf = leaf_class()

    def insert(self, iter_word: str, **kwargs: dict) -> None:
        """Insert a word recursively in the trie"""
        if len(iter_word) == 0:
            return self.leaf.insert(**kwargs)
        
        next_letter = iter_word[0]
        next_word = iter_word[1:]
        self.childs.setdefault(next_letter, TrieNode(next_letter, self.leaf_class)).insert(next_word, **kwargs)

    def get_node(self, word: str) -> 'TrieNode':
        """Get node representing a word in the trie"""
        node = self
        for letter in word:
            if letter not in node.childs:
                return None
            node = node.childs[letter]
        return node
    
    def get_words(self, key: str, recursive=False) -> list[str]:
        """Get words from trie using a key"""
        words = self.leaf.get(key=key)
        if recursive:
            for node in self.childs.values():
                words += node.get_words(key, recursive=True)
        return words
