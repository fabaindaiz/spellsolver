
from gameboard import Gameboard
from solver import Solver


def get_word_points(path):
    word_points = 0
    word_bonus = 0
    word_mult = 1

    for node in path:
        word_mult *= node.word_mult
        word_points += node.points
    
    if len(path) >= 6:
        word_bonus += 10

    return word_points * word_mult + word_bonus


def get_posible_paths(solver, word, path):
    arr = []

    for neighbor in path[-1].neighbors:
        if neighbor not in path:

            actual_word = word + neighbor.letter
            actual_path = path + [neighbor]

            exist, is_word = solver.exists(actual_word)

            if is_word:
                points = get_word_points(actual_path[1:])
                arr += [[points, actual_word, actual_path[1].cord]]
            
            if exist:
                arr += get_posible_paths(solver, actual_word, actual_path)
    
    return arr


class Spellsolver:

    def __init__(self, solver, gameboard):
        self.gameboard = gameboard
        self.solver = solver
    
    def get_words(self):
        arr = []

        for tile in self.gameboard.gameboard.values():
            arr += get_posible_paths(self.solver, "", [tile])
        
        return arr

    def get_best_word(self, word_list):
        word_list.sort(reverse=True, key=lambda x: x[0])
        
        print(word_list[0:20])


if __name__ == "__main__":
    print("Init solver")
    solver = Solver()
    solver.from_file("wordlist_english.txt")

    while(True):
        game_string = input("Insert a gameboard: ")
        mult_string = input("Insert 2x cord: ")
        DL_string = input("Insert DL cord: ")
        TL_string = input("Insert TL cord: ")

        gameboard = Gameboard(game_string.lower())
        if mult_string != "":
            mult_cord = (int(mult_string[0]), int(mult_string[1]))
            gameboard.set_mult_word(mult_cord)
        if DL_string != "":
            DL_cord = (int(DL_string[0]), int(DL_string[1]))
            gameboard.set_mult_letter(DL_cord, 2)
        if TL_string != "":
            TL_cord = (int(TL_string[0]), int(TL_string[1]))
            gameboard.set_mult_letter(TL_cord, 3)
        
        spellsolver = Spellsolver(solver, gameboard)
        words = spellsolver.get_words()
        spellsolver.get_best_word(words)

# ryewaliwxrytpiltxfiiwsiag