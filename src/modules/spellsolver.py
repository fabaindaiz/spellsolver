from typing import Any, Generator, List, Tuple

from src import SWAP
from src.modules.gameboard import GameTile, GameBoard, Path, ResultList, ResultWord
from src.modules.validate import WordValidate
from src.utils import Timer


class SpellSolver:
    """Solve a Spellcast game"""

    def __init__(self, validate: WordValidate, gameboard: GameBoard) -> None:
        self.gameboard: GameBoard = gameboard
        self.validate: WordValidate = validate

    def process_node(
        self, node: Any, word: str, path: Tuple[GameTile, ...]
    ) -> Generator[ResultWord, None, None]:
        """Recursively process a node to find possible valid words"""
        swaps = tuple(i for i, letter in enumerate(word) if letter == "0")

        for actual_word in self.validate.get_trie().get_leaf(node):
            actual_path = Path.get_path(path, actual_word, swaps)
            yield ResultWord(
                points=Path.word_points(actual_path),
                gems=Path.word_gems(actual_path),
                word=actual_word,
                path=actual_path,
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
            yield from self.process_node(actual_node, actual_word, tuple(path))
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
        base_tile = self.gameboard.get_base_tile()
        base_node = self.validate.get_trie().get_root()
        yield from self.process_path(
            tile=base_tile, node=base_node, word="", path=[], swap=swap
        )

    def word_list(self, swap: int, timer: Timer = None) -> ResultList:
        """Get a valid words list from a solver Spellcast game"""
        results = ResultList(timer=timer)
        results.update(self.process_gameboard(swap=min(swap, SWAP)))
        return results
