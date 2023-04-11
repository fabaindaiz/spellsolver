
from utils import Timer


class TrieNode:

    def __init__(self, letter):
        self.letter = letter
        self.childs = {}
        self.words = {}

    def insert_word(self, **kwargs):
        for key, value in kwargs.items():
            self.words.setdefault(key, []).append(value)
    
    def insert(self, iter_word, **kwargs):
        if len (iter_word) == 0:
            self.insert_word(**kwargs)
            return
        
        letter = iter_word[0]
        self.childs.setdefault(letter, TrieNode(letter)).insert(iter_word[1:], **kwargs)

    def _get_words(self, key: str):
        words = self.words.get(key, [])
        for node in self.childs.values():
            words += node.get_words(key)
        return words

    def get_words(self, swap=True):
        return self._get_words("word0"), self._get_words("word1")
    
    def __repr__(self):
        return f"word0: {self.lword0}\nword1: {self.lword1}\n"


class WordValidate:

    def __init__(self):
        self.tree = TrieNode('')
        self.timer = Timer()
    
    def from_file(self, path, swap=True):
        self.timer.reset_timer()
        print("Initializing WordValidate, this will take several seconds")

        with open(path) as file:
            for word in file.readlines():
                word = word[:-1]
                if swap:
                    for pos in range(len(word)):
                        incomplete_word = word[:pos] + word[pos+1:]
                        self.tree.insert(incomplete_word, word1=word)
                self.tree.insert(word, word0=word)
        
        print(f"WordValidate successfully initialized (elapsed time: {self.timer.elapsed_seconds()} seconds)")
    
    def get_node(self, word):
        node = self.tree
        for letter in word:
            if letter not in node.childs:
                return False
            node = node.childs[letter]  
        return node


if __name__ == "__main__":
    print("Init WordValidate")
    validate = WordValidate()
    validate.from_file("wordlist_english.txt", swap=True)

    while(True):
        word = input("Insert a word: ")
        node = validate.get_node(word)
        if node:
            print(node)
        else:
            print(f"There are any word started in {word}")