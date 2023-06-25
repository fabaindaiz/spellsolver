from src.modules.trie import TrieLeaf, TrieHeuristic, TrieNode
from src.config import SWAP


class ValidateLeaf(TrieLeaf):
    """Implements TrieLeaf interface to store words"""
    def __init__(self) -> None:
        self.words: dict[str, list[str]] = {}

    def insert(self, **kwargs: dict) -> None:
        """Insert a word in the TrieLeaf"""
        for key, value in kwargs.items():
            self.words.setdefault(key, []).append(value)
    
    def get(self, **kwargs: dict) -> list[str]:
        """Get a list of words in the TrieLeaf"""
        if "key" in kwargs:
            key = kwargs.get("key")
            return self.words.get(key, [])

class ValidateHeuristic(TrieHeuristic):
    """Implements TrieHeuristic interface to store heuristic values"""
    def __init__(self) -> None:
        pass

    def insert(**kwargs: dict) -> None:
        """Insert heuristic values in TrieHeuristic"""
        pass

    def get(**kwargs: dict) -> list['TrieNode']:
        """Get kwargs heuristic values from TrieHeuristic"""
        pass

class WordValidate:
    """Validate a word using a trie"""
    def __init__(self) -> None:
        self.trie: TrieNode = TrieNode('', ValidateLeaf)

    def word0(self, word: str) -> None:
        """Insert a word as word0 in the trie"""
        self.trie.insert(word, word0=word)

    def word1(self, word: str) -> None:
        """Insert a word as word1 in the trie"""
        for pos in range(len(word)):
            iword = word[:pos] + "0" + word[pos+1:]
            self.trie.insert(iword, word1=word)
    
    def word2(self, word: str) -> None:
        """Insert a word as word1 in the trie"""
        for pos2 in range(len(word)):
            for pos1 in range(pos2-1):
                iword = word[:pos1] + "0" + word[pos1+1:pos2] + "0" + word[pos2+1:]
                self.trie.insert(iword, word2=word)

    def load_file(self, path: str) -> None:
        """Initialize the trie with all words from a file"""
        with open(path) as file:
            for word in file.readlines():
                word = word[:-1]
                if "word0" in SWAP:
                    self.word0(word)
                if "word1" in SWAP:
                    self.word1(word)
                if "word2" in SWAP:
                    self.word2(word)


if __name__ == "__main__":
    validate = WordValidate()
    validate.load_file("src/wordlist/wordlist_english.txt")

    def node_str(node: TrieNode) -> str:
        """Return a string representation of a TrieNode"""
        return "\n".join([f"{swap}: {node.get_leaf(recursive=True, key=swap)}" for swap in SWAP])

    while(True):
        word = input("Insert a word: ")
        node = validate.trie.get_node(word)
        print(node_str(node) if node else f"There are no word started in {word}")
