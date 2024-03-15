from collections.abc import Generator
from typing import Any

try:
    import marisa_trie  # type: ignore
except ImportError:
    print(
        "Marisa Trie is not installed. Please install it with `pip install marisa-trie`"
    )

from src.modules.validate.wordlist import WordList
from .loader import pair_iter
from .trie import Trie, TrieQuery


class MarisaTrie(Trie):
    def __init__(self) -> None:
        self.trie: marisa_trie.RecordTrie = None
        self.words: list[str] = []

    def insert(self, loader: WordList, swap: int) -> None:
        self.words = list(loader.get_words())
        self.trie = marisa_trie.RecordTrie("<i", pair_iter(self.words, swap))

    def query(self) -> TrieQuery:
        return MarisaTrieQuery(self)


class MarisaTrieQuery(TrieQuery):
    def __init__(self, trie: MarisaTrie) -> None:
        self.trie: MarisaTrie = trie

    def get_root(self) -> str:
        return ""

    def get_key(self, node: str, letter: str) -> tuple[Any, str | None]:
        word = node + letter
        return word, letter if self.trie.trie.has_keys_with_prefix(word) else None

    def get_leaf(self, node: str) -> Generator[str, None, None]:
        for i in self.trie.trie.get(node, []):
            yield self.trie.words[i[0]]
