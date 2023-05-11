from src.trie import TrieLeaf, TrieNode


class ValidateLeaf(TrieLeaf):
    """Implements TrieLeaf interface to store words"""
    def __init__(self) -> None:
        self.words: dict = {}

    def insert(self, **kwargs: dict) -> None:
        """Insert a word in the TrieLeaf"""
        for key, value in kwargs.items():
            self.words.setdefault(key, []).append(value)
    
    def get(self, **kwargs: dict) -> list:
        """Get a list of words in the TrieLeaf"""
        key = kwargs.get("key")
        return self.words.get(key, [])

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
            iword = word[:pos] + word[pos+1:]
            self.trie.insert(iword, word1=word)

    def load_file(self, path) -> None:
        """Initialize the trie with all words from a file"""
        with open(path) as file:
            for word in file.readlines():
                word = word[:-1]
                self.word1(word)
                self.word0(word)

        
if __name__ == "__main__":
    validate = WordValidate()
    validate.load_file("wordlist/wordlist_english.txt")

    def node_str(node: TrieNode) -> str:
        """Return a string representation of a TrieNode"""
        return f"word0: {node.get_words('word0', recursive=True)}\nword1: {node.get_words('word1', recursive=True)}\n"

    while(True):
        word = input("Insert a word: ")
        node = validate.trie.get_node(word)
        print(node_str(node) if node else f"There are no word started in {word}")
