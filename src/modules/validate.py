from typing import Any, List
from itertools import combinations
from src.modules.trie import TrieLeaf, TrieNode
from src.modules.wordlist import WordList
from src.utils.iteration import pairwise
from src.config import SWAP


class ValidateLeaf(TrieLeaf):
    """Implements TrieLeaf interface to store words"""

    def __init__(self) -> None:
        self.words: List[str] = []

    def insert(self, **kwargs: dict) -> None:
        """Insert a word in the TrieLeaf"""
        self.words.append(kwargs.get("word"))

    def get(self, **kwargs: dict) -> List[str]:
        """Get a list of words in the TrieLeaf"""
        return self.words

    def heuristic(self, **kwargs: dict) -> Any:
        """Get heuristic values from TrieLeaf"""
        pass


class WordValidate:
    """Validate a word using a trie"""

    def __init__(self) -> None:
        self.wordlist = WordList()
        self.trie: TrieNode = TrieNode(ValidateLeaf)

    def _word_iter(self, word, num):
        for t in combinations(range(len(word)), num):
            yield (-1, *t, len(word))

    def insert(self, word: str, num: int) -> None:
        for t in self._word_iter(word, num):
            iword = "0".join(word[i + 1 : j] for i, j in pairwise(t))
            self.trie.insert(ValidateLeaf, iword, word=word)

    def load_wordlist(self) -> None:
        """Initialize the trie with all words from a file"""
        wordlist_file = self.wordlist.open_file()
        print("WordValidate is being initialized, this will take several seconds")

        with wordlist_file as file:
            for word in file.readlines():
                word = word[:-1]
                for num in range(SWAP + 1):
                    self.insert(word, num)


if __name__ == "__main__":
    validate = WordValidate()
    validate.load_wordlist()

    def node_str(node: TrieNode) -> str:
        """Return a string representation of a TrieNode"""
        return "\n".join(
            [f"{swap}: {node.get_leaf(recursive=True, key=swap)}" for swap in SWAP]
        )

    while True:
        word = input("Insert a word: ")
        node = validate.trie.get_node(word)
        print(node_str(node) if node else f"There are no word started in {word}")
