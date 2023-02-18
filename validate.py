
from utils import Timer


class TrieNode:

    def __init__(self, letter):
        self.letter = letter
        self.childs = {}

        self.word0 = False
        self.lword0 = []
        self.word1 = False
        self.lword1 = []

    def insert_word(self, **kwargs):
        if "word0" in kwargs:
            self.word0 = True
            self.lword0 += [kwargs["word0"]]
        if "word1" in kwargs:
            self.word1 = True
            self.lword1 += [kwargs["word1"]]
    
    def insert(self, iter_word, **kwargs):
        if len (iter_word) == 0:
            self.insert_word(**kwargs)
            return
        
        letter = iter_word[0]
        iter_word = iter_word[1:]
        
        if letter not in self.childs:
            self.childs[letter] = TrieNode(letter)
        self.childs[letter].insert(iter_word, **kwargs)

    def get_words(self, swap=True):
        words0 = []
        words1 = []

        if self.word0:
            words0 += self.lword0
        if self.word1:
            words1 += self.lword1
        for node in self.childs.values():
            twords0, twords1 = node.get_words(swap)
            words0 += twords0
            words1 += twords1
        return words0, words1
    
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