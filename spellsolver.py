
from gameboard import Gameboard
from solver import Solver


points = {'a': 1, 'b': 4, 'c': 5, 'd': 3, 'e': 1, 'f': 5, 'g': 3, 'h': 4, 'i': 1, 'j': 7, 'k': 6, 'l': 3, 'm': 4,
            'n': 2, 'o': 1, 'p': 4, 'q': 8, 'r': 2, 's': 2, 't': 2, 'u': 4, 'v': 5, 'w': 5, 'x': 7, 'y': 4, 'z': 8}


def get_word_points(word):
    word_points = 0

    for letter in word:
        word_points += points[letter]

    return word_points


def path_in_mult(path, cord):
    for node in path:
        if node.cord == cord:
            return True
    return False


def get_posible_paths(solver, word, path, mult_cord):
    arr = []

    for neighbor in path[-1].neighbors:
        if neighbor not in path:

            actual_word = word + neighbor.letter
            actual_path = path + [neighbor]

            exist, is_word = solver.exists(actual_word)

            if is_word:
                points = get_word_points(actual_word)

                if path_in_mult(actual_path[1:], mult_cord):
                    points *= 2

                arr += [[points, actual_word, actual_path[1].cord]]
            
            if exist:
                arr += get_posible_paths(solver, actual_word, actual_path, mult_cord)
    
    return arr


class Spellsolver:

    def __init__(self, gameboard, solver, mult_cord):
        self.gameboard = gameboard
        self.solver = solver
        self.mult_cord = mult_cord
    
    def get_words(self):
        arr = []

        for tile in self.gameboard.gameboard.values():
            arr += get_posible_paths(self.solver, "", [tile], self.mult_cord)
        
        #print(arr)
        return arr

    def get_best_word(self, word_list):
        word_list.sort(reverse=True, key=lambda x: x[0])
        
        print(word_list[0:20])


if __name__ == "__main__":
    print("Init solver")
    solver = Solver()
    solver.from_file("words_alpha.txt")

    while(True):
        game_string = input("Insert a gameboard: ")
        cord_string = input("Insert 2x cord: ")
        
        cord = (cord_string[0], cord_string[1])
        gameboard = Gameboard(game_string)
        
        spellsolver = Spellsolver(gameboard, solver, cord)
        words = spellsolver.get_words()
        spellsolver.get_best_word(words)

# ryewaliwxrytpiltxfiiwsiag