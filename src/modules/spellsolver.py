from collections.abc import Generator
from typing import Any

from src import SWAP
from src.modules.gameboard import GameTile, GamePath, GameBoard, ResultList, ResultWord
from src.modules.validate import WordValidate
from src.utils import Timer


class SpellSolver:
    def __init__(self, validate: WordValidate, gameboard: GameBoard) -> None:
        self.gameboard: GameBoard = gameboard
        self.validate: WordValidate = validate

    def process_node(
        self, node: Any, word: str, path: tuple[GameTile, ...]
    ) -> Generator[ResultWord, None, None]:
        swaps = tuple(i for i, letter in enumerate(word) if letter == "0")

        for actual_word in self.validate.get_trie().get_leaf(node):
            actual_path = GamePath.update_path(path, actual_word, swaps)
            yield ResultWord(
                points=GamePath.calculate_points(actual_path),
                gems=GamePath.calculate_gems(actual_path),
                word=actual_word,
                path=actual_path,
                swaps=swaps,
            )

    def process_path_aux(
        self,
        tile: GameTile,
        node: Any,
        word: str,
        path: list[GameTile],
        swap: int,
        letter: str,
    ) -> Generator[ResultWord, None, None]:
        actual_node, child_key = self.validate.get_trie().get_key(node, letter)
        if child_key:
            actual_word = word + child_key

            yield from self.process_node(actual_node, actual_word, tuple(path))
            yield from self.process_path(tile, actual_node, actual_word, path, swap)

    def process_path(
        self, tile: GameTile, node: Any, word: str, path: list[GameTile], swap: int
    ) -> Generator[ResultWord, None, None]:
        for actual_tile in tile.suggest_tiles(path):
            actual_path = path + [actual_tile]

            yield from self.process_path_aux(
                actual_tile, node, word, actual_path, swap, actual_tile.letter
            )

            if swap:
                yield from self.process_path_aux(
                    actual_tile, node, word, actual_path, swap - 1, "0"
                )

    def process_gameboard(self, swap: int) -> Generator[ResultWord, None, None]:
        base_tile = self.gameboard.base_tile
        base_node = self.validate.base_node

        yield from self.process_path(
            tile=base_tile, node=base_node, word="", path=[], swap=swap
        )

    def word_list(self, swap: int, timer: Timer) -> ResultList:
        results_generator = self.process_gameboard(swap=min(swap, SWAP))

        results = ResultList(timer=timer)
        results.update(results_generator)
        return results
