from src.resultlist import ResultList, ResultWord
from src.gameboard import GameBoard
from src.validate import WordValidate
from src.trie import TrieNode
from src.utils import Timer
from src.path import Path


class SpellSolver:
    """Solve a Spellcast game"""
    def __init__(self, validate: WordValidate, gameboard: GameBoard) -> None:
        self.gameboard: GameBoard = gameboard
        self.validate: WordValidate = validate

    def process_node(self, node: TrieNode, actual_word: str, actual_path: Path, swap: bool) -> set[ResultWord]:
        """Recursively process a node to find posible valid words"""
        paths = set()

        for word in node.get_words("word0"):
            paths.add(ResultWord(points=actual_path.word_points(), word=word, path=actual_path.path_tuple()))

        if swap:
            for word in node.get_words("word1"):
                index = next((i for i in range(len(actual_word)) if word[i]!=actual_word[i]), len(actual_word))
                
                for path in actual_path.complete_path(self.gameboard.tiles, word, index):
                    paths.add(ResultWord(points=path.word_points(), word=word, path=path.path_tuple(), swap=index))
        return paths

    def posible_paths(self, word, path: Path, swap: bool) -> set[ResultWord]:
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

    def word_list(self, swap: bool=True, timer: Timer=None) -> ResultList:
        """Get a valid words list from a solver Spellcast game"""
        results = ResultList(timer=timer)
        for tile in self.gameboard.tiles.values():
            results.update(self.posible_paths("", Path([tile]), swap))
        return results


if __name__ == "__main__":
    gameboard = GameBoard()
    validate = WordValidate()
    validate.load_file("wordlist/wordlist_english.txt")

    while(True):
        gameboard_string = input("Insert a gameboard: ")
        gameboard.load(gameboard_string)
        spellsolver = SpellSolver(validate, gameboard)

        swap = input("Use swap?: ") != "0"
        spellsolver.word_list(swap=swap)
