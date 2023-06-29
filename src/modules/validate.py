from src.modules.trie import TrieLeaf, TrieNode
from src.modules.wordlist import WordList
from src.config import SWAP


class ValidateLeaf(TrieLeaf):
    """Implements TrieLeaf interface to store words"""
    def __init__(self) -> None:
        self.words: list[str] = []

    def insert(self, **kwargs: dict) -> None:
        """Insert a word in the TrieLeaf"""
        self.words.append(kwargs.get("word"))
    
    def get(self, **kwargs: dict) -> list[str]:
        """Get a list of words in the TrieLeaf"""
        return self.words

    def heuristic(self, **kwargs: dict) -> any:
        """Get heuristic values from TrieLeaf"""
        pass

class WordValidate:
    """Validate a word using a trie"""
    def __init__(self) -> None:
        self.wordlist = WordList()
        self.trie: TrieNode = TrieNode(ValidateLeaf)
    
    def _insert(self, iword: str, word: str) -> None:
        self.trie.insert(ValidateLeaf, iword, word=word)

    def word0(self, word: str) -> None:
        """Insert a word as word0 in the trie"""
        self._insert(word, word)

    def word1(self, word: str) -> None:
        """Insert a word as word1 in the trie"""
        for pos in range(len(word)):
            iword = word[:pos] + "0" + word[pos+1:]
            self._insert(iword, word)
    
    def word2(self, word: str) -> None:
        """Insert a word as word1 in the trie"""
        for pos2 in range(len(word)):
            for pos1 in range(pos2-1):
                iword = word[:pos1] + "0" + word[pos1+1:pos2] + "0" + word[pos2+1:]
                self._insert(iword, word)

    def load_wordlist(self) -> None:
        """Initialize the trie with all words from a file"""
        wordlist_file = self.wordlist.open_file()
        print("WordValidate is being initialized, this will take several seconds")
        
        with wordlist_file as file:
            for word in file.readlines():
                word = word[:-1]
                if "swap0" in SWAP:
                    self.word0(word)
                if "swap1" in SWAP:
                    self.word1(word)
                if "swap2" in SWAP:
                    self.word2(word)


if __name__ == "__main__":
    validate = WordValidate()
    validate.load_wordlist()

    def node_str(node: TrieNode) -> str:
        """Return a string representation of a TrieNode"""
        return "\n".join([f"{swap}: {node.get_leaf(recursive=True, key=swap)}" for swap in SWAP])

    while(True):
        word = input("Insert a word: ")
        node = validate.trie.get_node(word)
        print(node_str(node) if node else f"There are no word started in {word}")
