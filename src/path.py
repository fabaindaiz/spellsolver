

class Path:
    def __init__(self, path: list):
        self.path: list = path

    def copy(self):
        node = Path(self.path)
        return node

    def word_points(self):
        word_points = 0
        word_bonus = 0
        word_mult = 1

        if len(self.path) >= 6:
            word_bonus += 10
        for node in self.path:
            word_points += node.points()
            word_mult *= node.word_mult
        return word_points * word_mult + word_bonus
    
    def suggest_node(self, neighbors):
        nodes = []
        for node in neighbors:
            if node not in self.path:
                nodes += [node]
        return nodes
    
    def complete_path(self, tiles, word, pos):
        nodes = set(tiles)
        if 0 <= pos < len(word):
            nodes = nodes.intersection(self.path[pos].suggest_node(self.path))
        if 0 <= pos+1 < len(word):
            nodes = nodes.intersection(self.path[pos+1].suggest_node(self.path))
        
        paths = []
        letter = word[pos]
        for node in nodes:
            if node not in self.path:
                new_node = node.copy(letter)
                new_path = self.path.copy()
                new_path.insert(pos+1, new_node)
                paths += [new_path]
        return paths