from typing import Any, Dict, Generator, List, Tuple

from src.modules.trie.base import Trie, TrieQuery
from src.modules.validate.wordlist import WordList
from src.modules.trie.loader import word_iter


class PrefixNode:
    """Represents a node of a Patricia Trie"""

    def __init__(self) -> None:
        self.childs: Dict[str, PrefixNode] = {}
        self.words: List[str] = []

    def insert(self, iter_word: str, word: str) -> None:
        """Insert a word recursively in the trie"""
        if not iter_word:
            return self.words.append(word)

        next_letter = iter_word[0]
        next_word = iter_word[1:]
        child = self.childs.setdefault(next_letter, PrefixNode())
        child.insert(next_word, word)

    def get_key(self, letter: str) -> "PrefixNode":
        """Get node representing a letter in the trie"""
        if letter in self.childs:
            return letter

    def get_node(self, word: str) -> "PrefixNode":
        """Get node representing a word in the trie"""
        node = self
        for letter in word:
            node = node.childs.get(letter)
            if not node:
                return None
        return node

    def get_leaf(self, recursive=False) -> Any:
        """Get content from trie leaf using kwargs"""
        words = self.words
        if recursive:
            for node in self.childs.values():
                words += node.get_leaf(recursive=True)
        return words
    
    def merge_tries(self, trie: "PrefixNode") -> None:
        """Merge other_trie into main_trie"""
        self.words += trie.words
        
        for letter, child in trie.childs.items():
            if letter in self.childs:
                self.childs[letter].merge_tries(child)
            else:
                self.childs[letter] = child


class PrefixTrie(Trie):
    """Represents a Prefix Trie"""

    def __init__(self) -> None:
        self.node: PrefixNode = PrefixNode()

    def insert_trie(self, loader: WordList) -> None:
        """Insert the words from the loader into the trie"""
        for word in loader.get_words():
            for iword in word_iter(word):
                self.node.insert(iword, word)
    
    def query_trie(self) -> "PrefixTrieQuery":
        """Obtains an object that allows queries to be made to the trie"""
        return PrefixTrieQuery(self)


class PrefixTrieQuery(TrieQuery):
    """Represents a Patricia Trie Query"""

    def __init__(self, trie: Trie) -> None:
        self.trie: PrefixTrie = trie
    
    def get_root(self) -> PrefixNode:
        """Obtains a representation of the base node of the trie"""
        return self.trie.node

    def get_key(self, node: PrefixNode, letter: str) -> Tuple[Any, str]:
        """Obtains the key associated with a letter from a node"""
        child_key = node.get_key(letter)
        return node.childs[child_key] if child_key else None, child_key

    def get_leaf(self, node: PrefixNode) -> Generator[str, None, None]:
        """Gets the words associated with a node"""
        yield from node.get_leaf()
