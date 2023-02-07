
points = {'a': 1, 'b': 4, 'c': 5, 'd': 3, 'e': 1, 'f': 5, 'g': 3, 'h': 4, 'i': 1, 'j': 7, 'k': 6, 'l': 3, 'm': 4,
            'n': 2, 'o': 1, 'p': 4, 'q': 8, 'r': 2, 's': 2, 't': 2, 'u': 4, 'v': 5, 'w': 5, 'x': 7, 'y': 4, 'z': 8}


class Gametile:

    def __init__(self, letter, cord):
        self.letter = letter
        self.cord = cord

        self.points = points[letter]
        self.word_mult = 1

        self.neighbors = []
    
    def init_neighbors(self, gameboard):
        x, y = self.cord
        tiles = [(x-1,y-1), (x,y-1), (x+1,y-1), (x-1,y), (x,y), (x+1,y), (x-1,y+1), (x,y+1), (x+1,y+1)]
        neighbors_cords = [(x, y) for x, y in tiles if 0 <= x < 5 and 0 <= y < 5]
        
        for x, y in neighbors_cords:
            self.neighbors += [gameboard[(x, y)]]


class Gameboard:

    def __init__(self, gameboard):
        self.gameboard_string = gameboard
        self.gameboard = {}

        self.init_nodes()

    def init_nodes(self):
        aux_cord = 0

        for letter in self.gameboard_string:
            x = aux_cord % 5
            y = aux_cord // 5
            aux_cord += 1

            self.gameboard[(x, y)] = Gametile(letter, (x, y))
        
        for node in self.gameboard.values():
            node.init_neighbors(self.gameboard)
    
    def set_mult_word(self, mult_cord):
        self.gameboard[mult_cord].word_mult = 2
        
    def set_mult_letter(self, mult_cord, mult):
        self.gameboard[mult_cord].points *= mult
    
    def print_gameboard(self):
        print(self.gameboard)


if __name__ == "__main__":
    game_string = input("Insert a gameboard: ")
    gameboard = Gameboard(game_string)
    gameboard.print_gameboard()

