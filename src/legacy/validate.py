from typing import Any, List, Tuple
from itertools import combinations
from collections import defaultdict
from multiprocessing import Pool, cpu_count
from src.tries.base import Trie, TrieNode, TrieLeaf
from src.modules.wordlist import WordList
from src.config import MULTIPROCESS, SWAP, TRIE





class ValidateLeaf(TrieLeaf):
    """Implements TrieLeaf interface to store words"""

    def __init__(self) -> None:
        self.words: List[str] = []

    def insert(self, word: str) -> None:
        """Insert a word in the TrieLeaf"""
        self.words.append(word)

    def get(self) -> List[str]:
        """Get a list of words in the TrieLeaf"""
        return self.words

    def heuristic(self) -> Any:
        """Get heuristic values from TrieLeaf"""
        return {
            "words_count": len(self.words),
        }
    
    def merge_leafs(self, leaf: "ValidateLeaf") -> None:
        """Merge other_leaf into main_leaf"""
        self.words += leaf.words


class WordValidate:
    """Validate a word using a trie"""

    def __init__(self) -> None:
        self.wordlist = WordList()
        self.trie_class = get_trie()
        self.trie: TrieNode = self.trie_class()

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
    
    def chunk_process(self, words: List[str]) -> None:
        """Insert a chunk of words based on the number of cores into the trie and return it"""
        chunk_size = len(words) // cpu_count()
        chunks = [words[i:i + chunk_size] for i in range(0, len(words), chunk_size)]

        with Pool(cpu_count()) as pool:
            local_tries = pool.map(self._insert_chunk, chunks)
        
        for local_trie in local_tries:
            self.trie.merge_tries(local_trie)

    def bucket_process(self, words: List[str]) -> None:
        """Insert a bucket of words based on the first letter into the trie and return it"""
        word_buckets = defaultdict(list)
        for word in words:
            word_buckets[word[0]].append(word)

        with Pool(cpu_count()) as pool:
            local_tries = pool.map(self._insert_chunk, word_buckets.values())
        
        for local_trie in local_tries:
            self.trie.merge_tries(local_trie)

    def load_wordlist(self) -> None:
        """Initialize the trie with all words from a file"""
        wordlist_file = self.wordlist.open_file()
        print("WordValidate is being initialized, this will take several seconds")

        words = [word[:-1] for word in ]

        process_fun = self.chunk_process if MULTIPROCESS else self._insert_chunk
        process_fun(words)


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
