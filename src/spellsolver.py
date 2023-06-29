from typing import Generator
from src.modules.resultlist import ResultList, ResultWord
from src.modules.gameboard import GameBoard
from src.modules.validate import WordValidate
from src.modules.trie import TrieNode
from src.modules.path import Path
from src.utils.timer import Timer


class SpellSolver:
    """Solve a Spellcast game"""
    def __init__(self, validate: WordValidate, gameboard: GameBoard) -> None:
        self.gameboard: GameBoard = gameboard
        self.validate: WordValidate = validate  

    def process_node(self, node: TrieNode, actual_path: Path, actual_word: str) -> Generator[ResultWord, None, None]:
        """Recursively process a node to find posible valid words"""
        swaps = [i for i, letter in enumerate(actual_word) if letter == "0"]
        
        for word in node.get_leaf():
            path = actual_path.swap_index(word, swaps=swaps)
            yield ResultWord(points=path.word_points(), word=word, path=path.path_tuple(), swaps=swaps)

    def process_path(self, node: TrieNode, path: Path, word: str, swap: int) -> Generator[ResultWord, None, None]:
        """Get all posible paths that complete a path using swap"""
        for tile in path.suggest_tile():  
            actual_path = Path(path.path + [tile])

            actual_word = word + tile.letter
            actual_node = node.get_letter(tile.letter)
            if actual_node:
                yield from self.process_node(actual_node, actual_path, actual_word)
                yield from self.process_path(actual_node, actual_path, actual_word, swap)

            if swap:
                actual_word = word + "0"
                actual_node = node.get_letter("0")
                if actual_node:
                    yield from self.process_node(actual_node, actual_path, actual_word)
                    yield from self.process_path(actual_node, actual_path, actual_word, swap-1)
    
    def process_gameboard(self, swap: int) -> Generator[ResultWord, None, None]:
        """"""
        for tile in self.gameboard.tiles.values():
            yield from self.process_path(node=self.validate.trie, path=Path([tile]), word="", swap=swap)

    def word_list(self, swap: int, timer: Timer=None) -> ResultList:
        """Get a valid words list from a solver Spellcast game"""
        results = ResultList(timer=timer)
        results.update(self.process_gameboard(swap=swap))
        return results


if __name__ == "__main__":
    gameboard = GameBoard()
    validate = WordValidate()
    validate.load_wordlist()

    while(True):
        gameboard_string = input("Insert a gameboard: ")
        gameboard.load(gameboard_string)
        spellsolver = SpellSolver(validate, gameboard)

        swap = input("Use swap?: ")
        spellsolver.word_list(swap=int(swap))
