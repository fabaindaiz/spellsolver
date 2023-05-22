

class ResultList:
    def __init__(self) -> None:
        self.data: dict = {}
        self.time: float = None

class ResultWord:
    def __init__(self, points: int, word: str, path: list, swap: bool=False) -> None:
        self.points: int = points
        self.word: str = word
        self.path: str = path
        self.swap: bool = swap
    
    def text(self) -> tuple:
        return (self.points, self.word)

    def __hash__(self) -> int:
        return hash((self.points, self.word, self.path))

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, ResultWord): return False
        return self.points == __value.points and self.word == __value.word and self.path == __value.path