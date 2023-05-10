

class TrieLeaf:
    def insert(**kwargs: dict) -> None:
        pass

    def get(key: str) -> list:
        pass

class TrieNode:
    def __init__(self, letter: str, leaf_class: TrieLeaf) -> None:
        self.letter: str = letter
        self.childs: dict = {}

        self.leaf_class: type = leaf_class
        self.leaf: TrieLeaf = leaf_class()

    def insert(self, iter_word: str, **kwargs: dict) -> None:
        if len(iter_word) == 0:
            return self.leaf.insert(**kwargs)
        
        next_letter = iter_word[0]
        next_word = iter_word[1:]
        self.childs.setdefault(next_letter, TrieNode(next_letter, self.leaf_class)).insert(next_word, **kwargs)

    def get_node(self, word: str) -> 'TrieNode':
        node = self
        for letter in word:
            if letter not in node.childs:
                return None
            node = node.childs[letter]
        return node
    
    def get_words(self, key: str, recursive=False) -> list:
        words = self.leaf.get(key)
        if recursive:
            for node in self.childs.values():
                words += node.get_words(key, recursive=True)
        return words
