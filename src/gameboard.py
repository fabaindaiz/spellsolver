
points = {'a': 1, 'b': 4, 'c': 5, 'd': 3, 'e': 1, 'f': 5, 'g': 3, 'h': 4, 'i': 1, 'j': 7, 'k': 6, 'l': 3, 'm': 4,
            'n': 2, 'o': 1, 'p': 4, 'q': 8, 'r': 2, 's': 2, 't': 2, 'u': 4, 'v': 5, 'w': 5, 'x': 7, 'y': 4, 'z': 8}


class GameTile:

    def __init__(self, letter, cord):
        self.letter = letter
        self.cord = cord
        self.swap = False

        self.word_mult = 1
        self.letter_mult = 1
        self.points = points[letter]

        self.neighbors = []
    
    def node_copy(self, letter):
        node = GameTile(letter, self.cord)

        node.swap = True
        node.word_mult = self.word_mult
        node.letter_mult = self.letter_mult
        #node.neighbors = self.neighbors

        return node

    def init_neighbors(self, tiles):
        x, y = self.cord
        cords = [(x-1,y-1), (x,y-1), (x+1,y-1), (x-1,y), (x+1,y), (x-1,y+1), (x,y+1), (x+1,y+1)]
        neighbors_cords = [(x, y) for x, y in cords if 0 <= x < 5 and 0 <= y < 5]
        
        self.neighbors += [tiles[(x, y)] for x, y in neighbors_cords]
    
    def suggest_node(self, path):
        nodes = []

        for node in self.neighbors:
            if node not in path:
                nodes += [node]
        
        return nodes

    def get_points(self):
        return self.points * self.letter_mult
    
    #def __repr__(self):
    #    return f"{' '.join(str(n.cord) for n in self.neighbors)}\n"


class GameBoard:

    def __init__(self):
        self.tiles = {}

    def init_nodes(self, gameboard_string):
        aux_cord = 0

        for letter in gameboard_string:
            x = aux_cord % 5
            y = aux_cord // 5
            aux_cord += 1

            self.tiles[(x, y)] = GameTile(letter, (x, y))
        
        for node in self.tiles.values():
            node.init_neighbors(self.tiles)
    
    def complete_path(self, path, word, pos):
        nodes = set(self.tiles.values())

        if 0 <= pos < len(word):
            nodes = nodes.intersection(path[pos].suggest_node(path))

        if 0 <= pos+1 < len(word):
            nodes = nodes.intersection(path[pos+1].suggest_node(path))
        
        paths = []
        letter = word[pos]

        for node in nodes:
            if node not in path:
                new_node = node.node_copy(letter)
                new_path = path.copy()
                new_path.insert(pos+1, new_node)
                paths += [new_path]
                #print(f"{word} {word[pos]} {new_node.letter} {[n.letter for n in paths[0]]}")

        return paths
    
    def set_mult_word(self, mult_cord):
        self.tiles[mult_cord].word_mult = 2
        
    def set_mult_letter(self, mult_cord, mult):
        self.tiles[mult_cord].letter_mult = mult

    def __repr__(self):
        r = list(self.tiles.values())
        return f"{' '.join([l.letter for l in r[0:5]])}\n{' '.join([l.letter for l in r[5:10]])}\n{' '.join([l.letter for l in r[10:15]])}\n{' '.join([l.letter for l in r[15:20]])}\n{' '.join([l.letter for l in r[20:25]])}\n{' '.join([l.letter for l in r[25:30]])}\n"


if __name__ == "__main__":
    gameboard_string = input("Insert a gameboard: ")
    gameboard = GameBoard()
    gameboard.init_nodes(gameboard_string)
    print(gameboard.tiles[(2,2)])