from collections.abc import Generator
from dataclasses import dataclass
from typing import Any, Optional

from src import SWAP
from src.modules.gameboard import GameBoard, GamePath, GameTile, ResultList, ResultWord
from src.modules.validate import WordValidate
from src.utils import Timer

type WordGenerator = Generator[ResultWord, None, None]


@dataclass
class Exploratory:
    tile: GameTile
    node: Any
    current_word: str
    current_path: list[GameTile]
    remaining_swaps: int
    letter: Optional[str] = None

    def __iter__(self):
        yield self.tile
        yield self.node
        yield self.current_word
        yield self.current_path
        yield self.remaining_swaps

        if self.letter:
            yield self.letter


class SpellSolver:
    def __init__(self, word_validator: WordValidate, game_board: GameBoard) -> None:
        self.game_board: GameBoard = game_board
        self.word_validator: WordValidate = word_validator

    def generate_words(
        self, node: Any, current_word: str, current_path: tuple[GameTile, ...]
    ) -> WordGenerator:
        blank_positions = tuple(
            index for index, letter in enumerate(current_word) if letter == "0"
        )

        for actual_word in self.word_validator.trie.get_leaf(node):
            actual_path = GamePath.update_path(
                current_path, actual_word, blank_positions
            )
            yield ResultWord(
                word=actual_word,
                path=actual_path,
                swaps=blank_positions,
            )

    def explore_paths_auxiliary(self, paths: Exploratory) -> WordGenerator:
        tile, node, current_word, current_path, remaining_swaps, letter = paths
        trie = self.word_validator.trie
        actual_node, child_key = trie.get_key(node, letter)

        if not child_key:
            return

        actual_word = current_word + child_key

        paths = Exploratory(
            tile=tile,
            node=actual_node,
            current_word=actual_word,
            current_path=current_path,
            remaining_swaps=remaining_swaps,
        )

        yield from self.generate_words(actual_node, actual_word, tuple(current_path))
        yield from self.explore_paths(paths)

    def explore_paths(self, paths: Exploratory) -> WordGenerator:
        tile, node, current_word, current_path, remaining_swaps = paths

        for actual_tile in tile.suggest_tiles(current_path):
            actual_path = current_path + [actual_tile]

            first_path = Exploratory(
                tile=actual_tile,
                node=node,
                current_word=current_word,
                current_path=actual_path,
                remaining_swaps=remaining_swaps,
                letter=actual_tile.letter,
            )

            second_path = Exploratory(
                tile=actual_tile,
                node=node,
                current_word=current_word,
                current_path=actual_path,
                remaining_swaps=remaining_swaps - 1,
                letter="0",
            )

            yield from self.explore_paths_auxiliary(first_path)

            if not remaining_swaps:
                continue

            yield from self.explore_paths_auxiliary(second_path)

    def process_gameboard(self, remaining_swaps: int) -> WordGenerator:
        base_tile = self.game_board.base_tile()
        base_node = self.word_validator.base_node()

        path = Exploratory(
            tile=base_tile,
            node=base_node,
            current_word="",
            current_path=[],
            remaining_swaps=remaining_swaps,
        )

        yield from self.explore_paths(path)

    def word_list(self, remaining_swaps: int, timer: Timer) -> ResultList:
        results_generator = self.process_gameboard(
            remaining_swaps=min(remaining_swaps, SWAP)
        )

        results = ResultList(timer=timer)
        results.update(results_generator)
        return results
