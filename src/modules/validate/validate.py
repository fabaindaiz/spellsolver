from src.modules.trie import Trie, TrieQuery, MarisaTrie
from .wordlist import WordList


class WordValidate:
    def __init__(self) -> None:
        self.wordlist: WordList = WordList()
        self.trie: Trie = MarisaTrie()

    def init(self, swap: int) -> None:
        self.trie.insert(self.wordlist, swap)

    def get_trie(self) -> TrieQuery:
        return self.trie.query()

    def base_node(self) -> TrieQuery:
        return self.get_trie().get_root()
