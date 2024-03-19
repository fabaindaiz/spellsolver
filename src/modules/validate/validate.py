from src.modules.trie import MarisaTrie, Trie
from .wordlist import WordList


class WordValidate:
    def __init__(self) -> None:
        self.wordlist: WordList = WordList()
        self.trie: Trie = MarisaTrie()

    def init(self, swap: int) -> None:
        self.trie.insert(self.wordlist, swap)

    def get_trie(self) -> Trie:
        return self.trie

    def base_node(self) -> Trie:
        return self.trie.get_root()
