from gameboard import GameBoard
from validate import WordValidate
from trie import TrieNode
from path import Path
from utils import Timer


class SpellSolver:
    """Solve a Spellcast game"""
    def __init__(self, validate: WordValidate, gameboard: GameBoard) -> None:
        self.gameboard: GameBoard = gameboard
        self.validate: WordValidate = validate
        self.timer: Timer = Timer()

    def process_node(self, node: TrieNode, actual_word: str, actual_path: Path, swap: bool) -> set:
        """Recursively process a node to find posible valid words"""
        paths = set()

        for word in node.get_words("word0"):
            points = actual_path.word_points()
            paths.add((points, word, actual_path.path[1].cord, actual_path.path_tuple()))
        
        if swap:
            for word in node.get_words("word1"):
                index = next((i for i in range(len(actual_word)) if word[i]!=actual_word[i]), len(actual_word))
                posible_paths = actual_path.complete_path(self.gameboard.tiles, word, index)
                
                for path in posible_paths:
                    points = path.word_points()
                    paths.add((points, word, actual_path.path[1].cord, word[index], path.path[index+1].cord, path.path_tuple()))
    
        return paths

    def posible_paths(self, word, path: Path, swap: bool) -> set:
        """Get all posible paths that complete a path using swap"""
        paths = set()

        for neighbor in path.path[-1].neighbors:
            if neighbor not in path.path:
                actual_word = word + neighbor.letter
                actual_path = Path(path.path + [neighbor])

                node = self.validate.trie.get_node(actual_word)
                if node:
                    paths.update(self.process_node(node, actual_word, actual_path, swap))
                    paths.update(self.posible_paths(actual_word, actual_path, swap))
        return paths

    def word_list(self, swap: bool=True) -> list:
        """Get a valid words list from a solver Spellcast game"""
        self.timer.reset_timer()
        check = set()
        word_list = []

        for tile in self.gameboard.tiles.values():
            result = self.posible_paths("", Path([tile]), swap)
            for res in result:
                size = len(check)
                check.add(res[0:2])
                if size != len(check):
                    word_list += [res]
        word_list.sort(reverse=True, key=lambda x: x[0])

        print(f"The following words have been found (elapsed time: {self.timer.elapsed_millis()} milliseconds)")
        print([w[:-1] for w in word_list[0:10]])
        return word_list


if __name__ == "__main__":
    validate = WordValidate()
    validate.load_file("wordlist/wordlist_english.txt")

    while(True):
        gameboard_string = input("Insert a gameboard: ")
        swap = input("Use swap?: ") != "0"

        gameboard = GameBoard(gameboard_string)
        spellsolver = SpellSolver(validate, gameboard)
        spellsolver.word_list(swap=swap)