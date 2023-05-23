

class ResultList():
    def __init__(self) -> None:
        self.data: dict = {}
        self.time: float = None
    
    def update(self, results: list) -> None:
        for res in results:
            self.data.update({res.word: res})
    
    def sorted(self, console: bool=False) -> list:
        sorted_data = sorted(self.data.values(), reverse=True, key=lambda x: x.points)
        if console:
            print(f"The following words have been found (elapsed time: {self.time} milliseconds)")
            print([word.text(console=console) for word in sorted_data[:10]])
        return sorted_data

class ResultWord:
    def __init__(self, points: int, word: str, path: tuple, swap: int=-1) -> None:
        self.points: int = points
        self.word: str = word
        self.path: tuple = path
        self.swap: int = swap
    
    def text(self, console=False) -> str:
        if not console:
            return f"({self.points} {self.word})"
        elif -1 < self.swap < len(self.path):
            return f"({self.points} {self.word} {self.path[0].cord} | {self.word[self.swap]} {self.path[self.swap].cord})"
        else:
            return f"({self.points} {self.word} {self.path[0].cord})"

    def __hash__(self) -> int:
        return hash((self.points, self.word, self.path))

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, ResultWord): return False
        return self.points == __value.points and self.word == __value.word and self.path == __value.path