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
        if api:
            return [word.dict() for word in sorted_data[:10]]
        if console:
            sorted_list = ", ".join(word.text(console=console) for word in sorted_data[:10])
            print(f"The following words have been found (elapsed time: {self.timer.elapsed_millis()} milliseconds)")
            print(f"[{sorted_list}]")
        return sorted_data

class ResultWord:
    """Represents a spellsolver result"""
    def __init__(self, points: int, word: str, path: tuple[GameTile], swaps: list[int]=[]) -> None:
        self.points: int = points
        self.word: str = word
        self.path: tuple[GameTile] = path
        self.swaps: list[int] = swaps
    
    def text(self, console: bool=False) -> str:
        """Get text representation of result"""
        if not console:
            return f"{self.points} {self.word}"
        
        # Console prints
        word = f"{self.points} {self.word} {self.path[0].cord}"
        result = " | ".join([f"{self.word[swap]} {self.path[swap].cord}" for swap in self.swaps])
        return f"({word} | {result})"
        
    def dict(self) -> dict[str, object]:
        return {
            "points": self.points,
            "word": self.word,
            "path": [node.cord for node in self.path],
            "swap": self.swaps
        }
