from src.trie.base import Trie
from src.wordlist.wordlist import WordList


def _word_iter(self, word, num):
        for t in combinations(range(len(word)), num):
            yield "".join("0" if i in t else word[i] for i in range(len(word)))

def insert(self, word: str, num: int) -> None:
    for iword in self._word_iter(word, num):
        self.trie.insert(iword)

def _insert_chunk(self, words: List[str]) -> TrieNode:
    """Insert a chunk of words into the trie and return it"""
    for word in words:
        for num in range(SWAP + 1):
            self.insert(word, num)
    
    self.trie.finish_insert()
    return self.trie

def load_trie(trie: Trie, wordlist: WordList) -> Trie:
        generator = wordlist.generator()
        trie.insert_words(generator)
        return trie