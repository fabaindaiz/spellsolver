
def get_neighbors_from_cords(x, y):
    neighbors = [(x-1,y-1), (x,y-1), (x+1,y-1), (x-1,y), (x,y), (x+1,y), (x-1,y+1), (x,y+1), (x+1,y+1)]
    return [(x, y) for x, y in neighbors if 0 <= x < 5 and 0 <= y < 5]
    

class Gametile:

    def __init__(self, letter, cord):
        self.letter = letter
        self.cord = cord
        self.neighbors = []


class Gameboard:

    def __init__(self, gameboard):
        self.gameboard_string = gameboard
        self.gameboard = {}

        self.init_nodes()
        self.conect_nodes()

    def init_nodes(self):
        aux_cord = 0

        for letter in self.gameboard_string:
            x = aux_cord % 5
            y = aux_cord // 5
            aux_cord += 1

            self.gameboard[(x, y)] = Gametile(letter, (x, y))
    
    def conect_nodes(self):
        for x, y in self.gameboard.keys():
            neighbors_cords = get_neighbors_from_cords(x, y)
            node = self.gameboard[(x, y)]

            for x, y in neighbors_cords:
                node.neighbors += [self.gameboard[(x, y)]]
    
    def print_gameboard(self):
        print(self.gameboard)


if __name__ == "__main__":
    game_string = input("Insert a gameboard: ")
    gameboard = Gameboard(game_string)
    gameboard.print_gameboard()

