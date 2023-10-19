import marisa_trie
from typing import Generator
#from src.trie.base import TrieLeaf, TrieNode
from src.wordlist.wordlist import WordList
from src.trie.base import Trie
from src.trie.loader import load_trie


class MarisaTrie(Trie):

    def __init__(self):
        self.trie: marisa_trie.Trie = None

    def insert_words(self, words: Generator[str, None, None]) -> None:
        words = list(words)
        self.trie = marisa_trie.Trie(words)  

    def exists_word(self, word: str) -> None:
        """Check if a word exists in the trie"""
        return word in self.trie
    
    def get_words(self, prefix: str) -> None:
        """Get all words with a prefix"""
        return self.trie.has_keys_with_prefix(prefix)


if __name__ == "__main__":
    wordlist = WordList()
    trie = MarisaTrie()
    trie = load_trie(trie=trie, wordlist=wordlist)

    while True:
        word = input("Insert a word: ")
        print(trie.get_words(word))