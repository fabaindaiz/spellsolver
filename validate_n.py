

class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.childs = {}
        self.words = {}

    def insert(self, iter_word, **kwargs):
        if len(iter_word) == 0:
            for key, value in kwargs.items():
                self.words.setdefault(key, []).append(value)
            return
        
        letter = iter_word[0]
        self.childs.setdefault(letter, TrieNode(letter)).insert(iter_word[1:], **kwargs)

    def get_words(self, swap=True):
        words = self.words
        for node in self.childs.values():
            for key, value in node.get_words().items():
                words.set

class WordValidate:
    pass