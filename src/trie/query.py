from typing import Tuple
from src.trie.base import Trie


class TrieQuery:

    def __init__(self, trie: Trie):
        self.trie = trie

    def update_state(self, state: str, letter: str) -> Tuple[str, str]:
        """Check if a word exists in the trie"""
        