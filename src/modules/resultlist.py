from src.modules.gameboard import GameTile
from src.utils import Timer


class ResultList():
    """Represents a result list"""
    def __init__(self, timer: Timer=None) -> None:
        self.data: dict[str, ResultWord] = {}
        self.timer: Timer = timer
    
    def update(self, results: list['ResultWord']) -> None:
        """Update result list"""
        for res in results:
            self.data.update({(res.points, res.word): res})
    
    def sorted(self, console: bool=False, api: bool=False) -> list['ResultWord']:
        """Return result list sorted by points"""
        sorted_data = sorted(self.data.values(), reverse=True, key=lambda x: x.points)
        if console:
            sorted_list = "[" + ", ".join(word.text(console=console) for word in sorted_data[:10]) + "]"
            print(f"The following words have been found (elapsed time: {self.timer.elapsed_millis()} milliseconds)")
            print(sorted_list)
        if api:
            return [word.dict() for word in sorted_data[:10]]
        return sorted_data

class ResultWord:
    """Represents a spellsolver result"""
    def __init__(self, points: int, word: str, path: tuple[GameTile], swap: int=-1) -> None:
        self.points: int = points
        self.word: str = word
        self.path: tuple[GameTile] = path
        self.swap: int = swap
    
    def text(self, console=False) -> str:
        """Get text representation of result"""
        if not console:
            return f"({self.points} {self.word})"
        # Console prints
        elif -1 < self.swap < len(self.path):
            return f"({self.points} {self.word} {self.path[0].cord} | {self.word[self.swap]} {self.path[self.swap].cord})"
        else:
            return f"({self.points} {self.word} {self.path[0].cord})"
        
    def dict(self) -> dict[str, object]:
        return {
            "points": self.points,
            "word": self.word,
            "path": [node.cord for node in self.path],
            "swap": self.swap
        }
