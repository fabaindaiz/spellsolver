from typing import Generator
from src.modules.gameboard import GameTile


class Path:
    """Represents a path of GameTiles forming a word"""
    def __init__(self, path: list[GameTile]) -> None:
        self.path: list[GameTile] = path
    
    def path_tuple(self) -> tuple[GameTile]:
        """Get a tuple with the path nodes"""
        return tuple(self.path[1:])

    def word_points(self) -> int:
        """Get points value of actual word"""
        path = self.path[1:]
        word_points = 0
        word_mult = 1

        word_bonus = 0
        if len(path) >= 6:
            word_bonus += 10
        
        for node in path:
            word_points += node.points()
            word_mult *= node.word_mult
        return word_points * word_mult + word_bonus
    
    def suggest_tile(self) -> Generator[GameTile, None, None]:
        """Get all nodes in neighbors that are not in path"""
        return (tile for tile in self.path[-1].neighbors if tile not in self.path)
    
    def swap_index(self, word: str, swaps: list[int]) -> 'Path':
        """Get a new path with swap nodes replaced"""
        if swaps == []:
            return self
            
        new_path = self.path.copy()
        for index in swaps:
            letter = word[index]
            node = self.path[index+1]
            new_path[index+1] = node.copy(letter)

        return Path(new_path)
