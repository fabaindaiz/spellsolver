
class LNode:

    def __init__(self, letter):
        self.letter = letter
        self.end_of_word = False
        self.childs = {}
    
    def insert(self, word):
        if len(word) == 0:
            self.end_of_word = True
            return

        next_letter = word[0]
        next_word = word[1:]
        
        if next_letter not in self.childs:
            self.childs[next_letter] = LNode(next_letter)
        self.childs[next_letter].insert(next_word)

    def get_words(self, word):
        actual_word = word + self.letter
        arr = []

        if self.end_of_word:
            arr += [actual_word]
        
        for child in self.childs.values():
            arr += child.get_words(actual_word)

        return arr


class Solver:

    def __init__(self):
        self.tree = LNode('')
    
    def from_file(self, path):
        with open(path) as file:
            for word in file.readlines():
                self.tree.insert(word[:-1])
    
    def exists(self, word):
        actual_node = self.tree

        try:
            for letter in word:
                actual_node = actual_node.childs[letter]
            return True, actual_node.end_of_word
        except:
            return False, False
    
    def get_words(self, word):
        actual_node = self.tree

        try:
            for letter in word:
                actual_node = actual_node.childs[letter]
            return actual_node.get_words(word)
        except:
            print(f"There are any word started in {word}")
    
    def main_loop(self):
        while(True):
            word = input("Insert a word: ")
            result = self.get_words(word)
            print(f"Posible words started with {word}")
            print(result)


if __name__ == "__main__":
    solver = Solver()
    solver.from_file("wordlist_english.txt")
    solver.main_loop()