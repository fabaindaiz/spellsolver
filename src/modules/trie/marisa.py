from collections.abc import Generator
from typing import Any

from marisa_trie import RecordTrie

from src.modules.validate.wordlist import WordList
from .loader import pair_iter
from .trie import Trie, TrieQuery


class MarisaTrie(Trie):
    def __init__(self) -> None:
        self.trie: RecordTrie = None
        self.words: list[str] = []

    def insert(self, loader: WordList, swap: int) -> None:
        self.words = list(loader.get_words())
        self.trie = RecordTrie("<i", pair_iter(self.words, swap))

    def query(self) -> TrieQuery:
        return MarisaTrieQuery(self)


class MarisaTrieQuery(TrieQuery):
    def __init__(self, trie: Trie) -> None:
        self.trie: MarisaTrie = trie

    def get_root(self) -> str:
        return ""

    def get_key(self, node: str, letter: str) -> tuple[Any, str]:
        word = node + letter
        return word, letter if self.trie.trie.has_keys_with_prefix(word) else None

    def get_leaf(self, node: str) -> Generator[str, None, None]:
        for i in self.trie.trie.get(node, []):
            yield self.trie.words[i[0]]
