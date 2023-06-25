from src.modules.resultlist import ResultList, ResultWord
from src.modules.gameboard import GameBoard
from src.modules.validate import WordValidate
from src.modules.trie import TrieNode
from src.modules.path import Path
from src.utils import Timer


class SpellSolver:
    """Solve a Spellcast game"""
    def __init__(self, validate: WordValidate, gameboard: GameBoard) -> None:
        self.gameboard: GameBoard = gameboard
        self.validate: WordValidate = validate

    def process_word(self, words: list[str], actual_word: str, actual_path: Path) -> list[ResultWord]:
        paths = []
        swaps = [i for i, letter in enumerate(actual_word) if letter == "0"]
        for word in words:
            actual_path = actual_path.swap_index(word, swaps=swaps)
            paths += [ResultWord(points=actual_path.word_points(), word=word, path=actual_path.path_tuple(), swaps=swaps)]
        return paths

    def process_node(self, node: TrieNode, actual_word: str, actual_path: Path, swap: int) -> list[ResultWord]:
        """Recursively process a node to find posible valid words"""
        paths = self.process_word(node.get_leaf(key="word0"), actual_word, actual_path)
        if swap >= 1:
            paths += self.process_word(node.get_leaf(key="word1"), actual_word, actual_path)
        if swap >= 2:
            paths += self.process_word(node.get_leaf(key="word2"), actual_word, actual_path)
        return paths
    
    def process_path_aux(self, actual_word: str, actual_path: Path, swap: int, act_swap: int) -> list[ResultWord]:
        paths = []
        node = self.validate.trie.get_node(actual_word)
        if node:
            paths += self.process_path(actual_word, actual_path, swap, act_swap)
            paths += self.process_node(node, actual_word, actual_path, swap)
        return paths

    def process_path(self, word: str, path: Path, swap: int, act_swap: int=0) -> list[ResultWord]:
        """Get all posible paths that complete a path using swap"""
        paths = []
        for neighbor in path.suggest_node(path.path[-1].neighbors):
            actual_path = Path(path.path + [neighbor])
            
            # Normal path
            actual_word = word + neighbor.letter
            paths += self.process_path_aux(actual_word, actual_path, swap, act_swap)
            
            # Swap path
            if act_swap < swap:
                actual_word = word + "0"
                paths += self.process_path_aux(actual_word, actual_path, swap, act_swap+1)
        return paths

    def word_list(self, swap: int=1, timer: Timer=None) -> ResultList:
        """Get a valid words list from a solver Spellcast game"""
        results = ResultList(timer=timer)
        for tile in self.gameboard.tiles.values():
            paths = self.process_path(word="", path=Path([tile]), swap=swap)
            results.update(paths)
        return results


if __name__ == "__main__":
    gameboard = GameBoard()
    validate = WordValidate()
    validate.load_file("wordlist/wordlist_english.txt")

    while(True):
        gameboard_string = input("Insert a gameboard: ")
        gameboard.load(gameboard_string)
        spellsolver = SpellSolver(validate, gameboard)

        swap = input("Use swap?: ")
        spellsolver.word_list(swap=int(swap))
