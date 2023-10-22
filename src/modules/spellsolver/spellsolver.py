from typing import Generator, List
from src.modules.spellsolver.validate import WordValidate
from src.modules.gameboard.gameboard import GameBoard, GameTile
from src.modules.gameboard.resultlist import ResultList, ResultWord
from src.modules.gameboard.path import Path
from src.modules.trie.base import TrieQuery
from src.utils.timer import Timer
from src.config import SWAP


class SpellSolver:
    """Solve a Spellcast game"""

    def __init__(self, validate: WordValidate, gameboard: GameBoard) -> None:
        self.gameboard: GameBoard = gameboard
        self.validate: WordValidate = validate

    def process_node(
        self, trie: TrieQuery, actual_word: str, actual_path: List[GameTile]
    ) -> Generator[ResultWord, None, None]:
        """Recursively process a node to find possible valid words"""
        swaps = [i for i, letter in enumerate(actual_word) if letter == "0"]

        for word in trie.get_leaf(actual_word):
            path = Path(actual_path).swap_index(word, swaps=swaps)
            yield ResultWord(
                points=path.word_points(),
                word=word,
                path=path.path_tuple(),
                swaps=swaps,
            )

    def process_path_aux(
        self,
        tile: GameTile,
        trie: TrieQuery,
        word: str,
        path: List[GameTile],
        swap: int,
        letter: str,
    ) -> Generator[ResultWord, None, None]:
        actual_word = word + letter
        if trie.get_key(actual_word):
            yield from self.process_node(trie, actual_word, path)
            yield from self.process_path(tile, trie, actual_word, path, swap)

    def process_path(
        self, tile: GameTile, trie: TrieQuery, word: str, path: List[GameTile], swap: int
    ) -> Generator[ResultWord, None, None]:
        """Get all posible paths that complete a path using swap"""
        for actual_tile in tile.suggest_tile(path):
            actual_path = path + [actual_tile]
            yield from self.process_path_aux(
                actual_tile, trie, word, actual_path, swap, actual_tile.letter
            )
            if swap:
                yield from self.process_path_aux(
                    actual_tile, trie, word, actual_path, swap - 1, "0"
                )

    def process_gameboard(self, swap: int) -> Generator[ResultWord, None, None]:
        """Iterate over all the squares on the board to start processing the paths"""
        for tile in self.gameboard.tiles.values():
            yield from self.process_path(
                tile=tile, trie=self.validate.get_trie(), word="", path=[tile], swap=swap
            )

    def word_list(self, swap: int, timer: Timer = None) -> ResultList:
        """Get a valid words list from a solver Spellcast game"""
        results = ResultList(timer=timer)
        results.update(self.process_gameboard(swap=min(swap, SWAP)))
        return results


if __name__ == "__main__":
    gameboard = GameBoard()
    validate = WordValidate()
    validate.load_wordlist()

    while True:
        gameboard_string = input("Insert a gameboard: ")
        gameboard.load(gameboard_string)
        spellsolver = SpellSolver(validate, gameboard)

        swap = input("Use swap?: ")
        spellsolver.word_list(swap=int(swap))
