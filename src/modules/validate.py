from src.modules.trie import TrieHeuristic, TrieLeaf, TrieNode
from src.modules.wordlist import WordList
from src.config import SWAP


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

class ValidateLeaf(TrieLeaf):
    """Implements TrieLeaf interface to store words"""
    def __init__(self) -> None:
        self.words: list[str] = []

    def insert(self, **kwargs: dict) -> None:
        """Insert a word in the TrieLeaf"""
        if "word" in kwargs:
            self.words.append(kwargs.get("word"))
    
    def get(self, **kwargs: dict) -> list[str]:
        """Get a list of words in the TrieLeaf"""
        return self.words

class WordValidate:
    """Validate a word using a trie"""
    def __init__(self) -> None:
        self.wordlist = WordList()
        self.trie: TrieNode = TrieNode(ValidateLeaf)

    def word0(self, word: str) -> None:
        """Insert a word as word0 in the trie"""
        self.trie.insert(word, word=word)

    def word1(self, word: str) -> None:
        """Insert a word as word1 in the trie"""
        for pos in range(len(word)):
            iword = word[:pos] + "0" + word[pos+1:]
            self.trie.insert(iword, word=word)
    
    def word2(self, word: str) -> None:
        """Insert a word as word1 in the trie"""
        for pos2 in range(len(word)):
            for pos1 in range(pos2-1):
                iword = word[:pos1] + "0" + word[pos1+1:pos2] + "0" + word[pos2+1:]
                self.trie.insert(iword, word=word)

    def load_wordlist(self) -> None:
        """Initialize the trie with all words from a file"""
        wordlist_file = self.wordlist.open_file()
        print("WordValidate is being initialized, this will take several seconds")
        
        with wordlist_file as file:
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
    validate.load_wordlist()

    def node_str(node: TrieNode) -> str:
        """Return a string representation of a TrieNode"""
        return "\n".join([f"{swap}: {node.get_leaf(recursive=True, key=swap)}" for swap in SWAP])

    while(True):
        word = input("Insert a word: ")
        node = validate.trie.get_node(word)
        print(node_str(node) if node else f"There are no word started in {word}")
