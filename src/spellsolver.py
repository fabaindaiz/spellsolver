from src.gameboard import GameBoard
from src.validate import WordValidate
from src.trie import TrieNode
from src.path import Path


class SpellSolver:
    """Solve a Spellcast game"""
    def __init__(self, validate: WordValidate, gameboard: GameBoard) -> None:
        self.gameboard: GameBoard = gameboard
        self.validate: WordValidate = validate

    def process_node(self, node: TrieNode, actual_word: str, actual_path: Path, swap: bool) -> set:
        """Recursively process a node to find posible valid words"""
        paths = set()

        for word in node.get_words("word0"):
            paths.add((actual_path.word_points(), word, actual_path.path[1].cord, actual_path.path_tuple()))
        
        if swap:
            for word in node.get_words("word1"):
                index = next((i for i in range(len(actual_word)) if word[i]!=actual_word[i]), len(actual_word))
                
                for path in actual_path.complete_path(self.gameboard.tiles, word, index):
                    paths.add((path.word_points(), word, actual_path.path[1].cord, word[index], path.path[index+1].cord, path.path_tuple()))
        return paths

    def posible_paths(self, word, path: Path, swap: bool) -> set:
        """Get all posible paths that complete a path using swap"""
        paths = set()
        for neighbor in path.suggest_node(path.path[-1].neighbors):
            actual_word = word + neighbor.letter
            actual_path = Path(path.path + [neighbor])

            node = self.validate.trie.get_node(actual_word)
            if node:
                paths.update(self.process_node(node, actual_word, actual_path, swap))
                paths.update(self.posible_paths(actual_word, actual_path, swap))
        return paths

    def word_list(self, swap: bool=True) -> list:
        """Get a valid words list from a solver Spellcast game"""
        word_list = {}
        for tile in self.gameboard.tiles.values():
            for res in self.posible_paths("", Path([tile]), swap):
                word_list.update({res[1]: res})
        return sorted(word_list.values(), reverse=True, key=lambda x: x[0])


if __name__ == "__main__":
    gameboard = GameBoard()
    validate = WordValidate()
    validate.load_file("wordlist/wordlist_english.txt")

    while(True):
        gameboard_string = input("Insert a gameboard: ")
        gameboard.init(gameboard_string)
        spellsolver = SpellSolver(validate, gameboard)

        swap = input("Use swap?: ") != "0"
        spellsolver.word_list(swap=swap)
