
from gameboard import GameBoard
from validate import WordValidate
from utils import get_word_points


class SpellSolver:

    def __init__(self, validate, gameboard):
        self.gameboard = gameboard
        self.validate = validate

    def process_node(self, node, actual_word, actual_path, swap):
        paths = set()

        if node.word0:
            for word in node.lword0:
                points = get_word_points(actual_path[1:])
                paths.add((points, word, actual_path[1].cord, tuple(actual_path[1:])))
        
        if swap == "1" and node.word1:
            for word in node.lword1:
                index = next((i for i in range(len(actual_word)) if word[i]!=actual_word[i]), len(actual_word))
                posible_paths = self.gameboard.complete_path(actual_path, word, index)
                
                for path in posible_paths:
                    points = get_word_points(path[1:])
                    paths.add((points, word, actual_path[1].cord, word[index], tuple(path[1:]))) # path[index+1].cord, tuple([(t.cord, t.letter) for t in path[1:]])
    
        return paths

    def get_posible_paths(self, word, path, swap):
        paths = set()

        for neighbor in path[-1].neighbors:
            if neighbor not in path:
                actual_word = word + neighbor.letter
                actual_path = path + [neighbor]

                node = self.validate.get_node(actual_word)
                
                if node != False:
                    paths.update(self.process_node(node, actual_word, actual_path, swap))
                    
                    paths.update(self.get_posible_paths(actual_word, actual_path, swap))

        return paths

    def get_word_list(self, swap=True):
        check = set()
        word_list = []

        for tile in self.gameboard.tiles.values():
            result = self.get_posible_paths("", [tile], swap)
            for res in result:
                size = len(check)
                check.add(res[0:2])
                if size != len(check):
                    word_list += [res]
        
        word_list.sort(reverse=True, key=lambda x: x[0])
        print([w[:-1] for w in word_list[0:20]])
        
        return word_list


if __name__ == "__main__":
    print("Init WordValidate")
    validate = WordValidate()
    validate.from_file("wordlist_english.txt", swap=True)

    while(True):
        gameboard_string = input("Insert a gameboard: ")
        swap_string = input("Use swap?: ")

        gameboard = GameBoard()
        gameboard.init_nodes(gameboard_string)

        spellsolver = SpellSolver(validate, gameboard)
        spellsolver.get_word_list(swap=swap_string)