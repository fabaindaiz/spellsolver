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

    def process_node(self, node: TrieNode, actual_word: str, actual_path: Path, swap: int) -> list[ResultWord]:
        """Recursively process a node to find posible valid words"""
        paths = []
        for word in node.get_leaf(key="word0"):
            paths += [ResultWord(points=actual_path.word_points(), word=word, path=actual_path.path_tuple())]

        if swap >= 1:
            for word in node.get_leaf(key="word1"):
                # Gets the index of the letter that is in word but not in actual_word
                index = next((i for i in range(len(actual_word)) if word[i]!=actual_word[i]), len(actual_word))

                letter = word[index]
                tile = actual_path.path[index+1]

                new_path = actual_path.path.copy()
                new_path[index+1] = tile.copy(letter)
                path = Path(new_path)

                paths += [ResultWord(points=path.word_points(), word=word, path=path.path_tuple(), swap=index)]
        
        if swap >= 2:
            for word in node.get_leaf(key="word2"):
                index1 = next((i for i in range(len(actual_word)) if word[i]!=actual_word[i]), len(actual_word))
                index2 = next((i for i in range(index1+1, len(actual_word)) if word[i]!=actual_word[i]), len(actual_word))

                letter1 = word[index1]
                tile1 = actual_path.path[index1+1]
                actual_path.path[index1+1] = tile1.copy(letter1)

                letter2 = word[index2]
                tile2 = actual_path.path[index2+1]
                actual_path.path[index2+1] = tile2.copy(letter2)

                paths += [ResultWord(points=actual_path.word_points(), word=word, path=actual_path.path_tuple(), swap=index1)]

        return paths

    def posible_paths(self, word: str, path: Path, swap: int, act_swap: int=0) -> list[ResultWord]:
        """Get all posible paths that complete a path using swap"""
        paths = []
        for neighbor in path.suggest_node(path.path[-1].neighbors):
            # Normal path
            actual_word = word + neighbor.letter
            actual_path = Path(path.path + [neighbor])

            node = self.validate.trie.get_node(actual_word)
            if node:
                paths += self.process_node(node, actual_word, actual_path, swap)
                paths += self.posible_paths(actual_word, actual_path, swap, act_swap)
            
            if act_swap >= swap:
                continue
            
            # Swap path
            actual_word = word + "0"
            actual_path = Path(path.path + [neighbor])

            node = self.validate.trie.get_node(actual_word)
            if node:
                paths += self.process_node(node, actual_word, actual_path, swap)
                paths += self.posible_paths(actual_word, actual_path, swap, act_swap+1)
        return paths

    def word_list(self, swap: int=1, timer: Timer=None) -> ResultList:
        """Get a valid words list from a solver Spellcast game"""
        results = ResultList(timer=timer)
        for tile in self.gameboard.tiles.values():
            paths = self.posible_paths(word="", path=Path([tile]), swap=swap)
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
