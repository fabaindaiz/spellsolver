
class LNode:

    def __init__(self, letter):
        self.letter = letter
        self.end_of_word = False
        self.word = []
        self.childs = {}
    
    def insert(self, word, complete_word):
        if len(word) == 0:
            self.end_of_word = True
            self.word += [complete_word]
            return

        next_letter = word[0]
        next_word = word[1:]
        
        if next_letter not in self.childs:
            self.childs[next_letter] = LNode(next_letter)
        self.childs[next_letter].insert(next_word, complete_word)

    def get_words(self, word):
        actual_word = word + self.letter
        words = []

        if self.end_of_word:
            words += [actual_word]
        
        for child in self.childs.values():
            words += child.get_words(actual_word)

        return words


class Solver:

    def __init__(self):
        self.tree = LNode('')
        self.complete = {}
    
    def from_file(self, path, swap=True):
        with open(path) as file:
            for word in file.readlines():
                if swap:
                    for pos in range(len(word[:-1])):
                        incomplete_word = word[:pos] + word[pos+1:-1]
                        self.tree.insert(incomplete_word, word[:-1])
                self.tree.insert(word[:-1], word[:-1])
                
    def exists(self, word):
        actual_node = self.tree

        try:
            for letter in word:
                actual_node = actual_node.childs[letter]
            return True, actual_node.end_of_word, actual_node.word
        except:
            return False, False, ""
    
    def get_words(self, word):
        actual_node = self.tree

        try:
            for letter in word:
                actual_node = actual_node.childs[letter]
            return actual_node.get_words(word[:-1])
        except:
            print(f"There are any word started in {word}")
    
    def main_loop(self):
        while(True):
            word = input("Insert a word: ")
            print(self.exists(word))
            result = self.get_words(word)
            print(f"Posible words started with {word}")
            print(result)


if __name__ == "__main__":
    solver = Solver()
    solver.from_file("wordlist_english.txt", swap=True)
    solver.main_loop()