from collections.abc import Generator
from typing import Any

from src import SWAP
from src.modules.gameboard import GameBoard, GamePath, GameTile, ResultList, ResultWord
from src.modules.validate import WordValidate
from src.utils import Timer


class SpellSolver:
    def __init__(self, word_validator: WordValidate, game_board: GameBoard) -> None:
        self.game_board: GameBoard = game_board
        self.word_validator: WordValidate = word_validator

    def generate_words(
        self, node: Any, current_word: str, current_path: tuple[GameTile, ...]
    ) -> Generator[ResultWord, None, None]:
        blank_positions = tuple(
            index for index, letter in enumerate(current_word) if letter == "0"
        )

        for actual_word in self.word_validator.get_trie().get_leaf(node):
            actual_path = GamePath.update_path(
                current_path, actual_word, blank_positions
            )
            yield ResultWord(
                points=GamePath.calculate_points(actual_path),
                gems=GamePath.calculate_gems(actual_path),
                word=actual_word,
                path=actual_path,
                swaps=blank_positions,
            )

    def explore_paths_auxiliary(
        self,
        tile: GameTile,
        node: Any,
        current_word: str,
        current_path: list[GameTile],
        remaining_swaps: int,
        letter: str,
    ) -> Generator[ResultWord, None, None]:
        actual_node, child_key = self.word_validator.get_trie().get_key(node, letter)
        if not child_key:
            return

        actual_word = current_word + child_key

        yield from self.generate_words(actual_node, actual_word, tuple(current_path))
        yield from self.explore_paths(
            tile, actual_node, actual_word, current_path, remaining_swaps
        )

    def explore_paths(
        self,
        tile: GameTile,
        node: Any,
        current_word: str,
        current_path: list[GameTile],
        remaining_swaps: int,
    ) -> Generator[ResultWord, None, None]:
        for actual_tile in tile.suggest_tiles(current_path):
            actual_path = current_path + [actual_tile]

            yield from self.explore_paths_auxiliary(
                actual_tile,
                node,
                current_word,
                actual_path,
                remaining_swaps,
                actual_tile.letter,
            )

            if not remaining_swaps:
                continue

            yield from self.explore_paths_auxiliary(
                actual_tile,
                node,
                current_word,
                actual_path,
                remaining_swaps - 1,
                "0",
            )

    def process_gameboard(
        self, remaining_swaps: int
    ) -> Generator[ResultWord, None, None]:
        base_tile = self.game_board.base_tile()
        base_node = self.word_validator.base_node()

        yield from self.explore_paths(
            tile=base_tile,
            node=base_node,
            current_word="",
            current_path=[],
            remaining_swaps=remaining_swaps,
        )

    def word_list(self, remaining_swaps: int, timer: Timer) -> ResultList:
        results_generator = self.process_gameboard(
            remaining_swaps=min(remaining_swaps, SWAP)
        )

        results = ResultList(timer=timer)
        results.update(results_generator)
        return results
