from typing import Generator, List
from concurrent.futures import ThreadPoolExecutor
from src.modules.resultlist import ResultList, ResultWord
from src.modules.gameboard import GameBoard, GameTile
from src.modules.validate import WordValidate
from src.modules.trie import TrieNode
from src.modules.path import Path
from src.utils.timer import Timer
from src.config import SWAP


class SpellSolver:
    """Solve a Spellcast game"""

    def __init__(self, validate: WordValidate, gameboard: GameBoard) -> None:
        self.gameboard: GameBoard = gameboard
        self.validate: WordValidate = validate

    def process_node(
        self, node: TrieNode, actual_word: str, actual_path: List[GameTile]
    ) -> Generator[ResultWord, None, None]:
        """Recursively process a node to find possible valid words"""
        swaps = [i for i, letter in enumerate(actual_word) if letter == "0"]

        for word in node.get_leaf():
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
        node: TrieNode,
        word: str,
        path: List[GameTile],
        swap: int,
        letter: str,
    ) -> Generator[ResultWord, None, None]:
        child_key = node.get_key(letter)
        if child_key:
            actual_word = word + child_key
            actual_node = node.childs[child_key]
            yield from self.process_node(actual_node, actual_word, path)
            yield from self.process_path(tile, actual_node, actual_word, path, swap)

    def process_path(
        self, tile: GameTile, node: TrieNode, word: str, path: List[GameTile], swap: int
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
    
    def process_tile(self, tile: GameTile, swap: int) -> Generator[ResultWord, None, None]:
        """Process a single tile for valid words"""
        return self.process_path(
            tile=tile, node=self.validate.trie, word="", path=[tile], swap=swap
        )

    def process_gameboard(self, swap: int) -> Generator[ResultWord, None, None]:
        """Iterate over all the squares on the board to start processing the paths"""
        with ThreadPoolExecutor() as executor:
            results = list(executor.map(self.process_tile, self.gameboard.tiles.values(), [swap] * len(self.gameboard.tiles)))
            for tile_results in results:
                yield from tile_results

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
