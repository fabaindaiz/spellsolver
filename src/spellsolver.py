import multiprocessing
from typing import Any, Generator, List
from src.modules.wordlist.validate import WordValidate
from src.modules.gameboard.gameboard import GameBoard, GameTile
from src.modules.gameboard.resultlist import ResultList, ResultWord
from src.modules.gameboard.path import Path
from src.utils.timer import Timer
from src.config import SWAP


class SpellSolver:
    """Solve a Spellcast game"""

    def __init__(self, validate: WordValidate, gameboard: GameBoard) -> None:
        self.gameboard: GameBoard = gameboard
        self.validate: WordValidate = validate

    def process_node(
        self, node: Any, word: str, path: List[GameTile]
    ) -> Generator[ResultWord, None, None]:
        """Recursively process a node to find possible valid words"""
        swaps = [i for i, letter in enumerate(word) if letter == "0"]

        for actual_word in self.validate.get_trie().get_leaf(node):
            actual_path = Path(path).swap_index(actual_word, swaps=swaps)
            yield ResultWord(
                points=actual_path.word_points(),
                word=actual_word,
                path=actual_path.path_tuple(),
                swaps=swaps,
            )

    def process_path_aux(
        self,
        tile: GameTile,
        node: Any,
        word: str,
        path: List[GameTile],
        swap: int,
        letter: str,
    ) -> Generator[ResultWord, None, None]:
        actual_node, child_key = self.validate.get_trie().get_key(node, letter)
        if child_key:
            actual_word = word + child_key
            yield from self.process_node(actual_node, actual_word, path)
            yield from self.process_path(tile, actual_node, actual_word, path, swap)

    def process_path(
        self, tile: GameTile, node: Any, word: str, path: List[GameTile], swap: int
    ) -> Generator[ResultWord, None, None]:
        """Get all posible paths that complete a path using swap"""
        for actual_tile in tile.suggest_tile(path):
            actual_path = path + [actual_tile]
            yield from self.process_path_aux(
                actual_tile, node, word, actual_path, swap, actual_tile.letter
            )
            if swap:
                yield from self.process_path_aux(
                    actual_tile, node, word, actual_path, swap - 1, "0"
                )

    def process_gameboard(self, swap: int) -> Generator[ResultWord, None, None]:
        """Iterate over all the squares on the board to start processing the paths"""
        for tile in self.gameboard.tiles.values():
            yield from self.process_path(
                tile=tile, node=self.validate.get_trie().get_root(), word="", path=[tile], swap=swap
            )

    def word_list(self, swap: int, timer: Timer = None) -> ResultList:
        """Get a valid words list from a solver Spellcast game"""
        results = ResultList(timer=timer)
        results.update(self.process_gameboard(swap=min(swap, SWAP)))
        return results
