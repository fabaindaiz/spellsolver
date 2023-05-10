from utils import letter_points


class GameTile:
    def __init__(self, letter, cord):
        self.letter = letter
        self.cord = cord
        self.swap = False

        self.word_mult = 1
        self.letter_mult = 1
        self.points = letter_points(letter)

        self.neighbors = []

    def copy(self, letter):
        node = GameTile(letter, self.cord)
        node.swap = True
        node.word_mult = self.word_mult
        node.letter_mult = self.letter_mult
        return node
    
    def points(self):
        return self.points * self.letter_mult
    
    def init_neighbors(self, tiles):
        x, y = self.cord
        cords = [(x-1,y-1), (x,y-1), (x+1,y-1), (x-1,y), (x+1,y), (x-1,y+1), (x,y+1), (x+1,y+1)]
        neighbors_cords = [(x, y) for x, y in cords if 0 <= x < 5 and 0 <= y < 5]

        self.neighbors += [tiles[(x, y)] for x, y in neighbors_cords]

class GameBoard:
    def __init__(self, gameboard: str):
        self.tiles: dict = {}

        for aux, letter in enumerate(gameboard):
            x = aux % 5
            y = aux // 5
            self.tiles[(x, y)] = GameTile(letter, (x, y))
        
        for node in self.tiles.values():
            node.init_neighbors(self.tiles)

    def set_mult_word(self, mult_cord):
        self.tiles[mult_cord].word_mult = 2
        
    def set_mult_letter(self, mult_cord, mult):
        self.tiles[mult_cord].letter_mult = mult

    def __repr__(self):
        r = list(self.tiles.values())
        return f"{' '.join([l.letter for l in r[0:5]])}\n{' '.join([l.letter for l in r[5:10]])}\n{' '.join([l.letter for l in r[10:15]])}\n{' '.join([l.letter for l in r[15:20]])}\n{' '.join([l.letter for l in r[20:25]])}\n{' '.join([l.letter for l in r[25:30]])}"


if __name__ == "__main__":
    gameboard_string = input("Insert a gameboard: ")
    gameboard = GameBoard(gameboard_string)
    print(gameboard)
