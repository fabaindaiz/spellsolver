from src.modules.validate.validate import WordValidate
from src.modules.gameboard.resultlist import ResultList
from src.modules.gameboard.gameboard import GameBoard
from src.modules.spellsolver import SpellSolver
from src.utils.timer import Timer
from src.config import VERSION


class ThreadSolver:
    """Represents a thread safe spellcast solver"""

    def __init__(self, app: "BaseUI") -> None:
        self.app: BaseUI = app
        self.timer: Timer = Timer()
        self.gameboard: GameBoard = GameBoard()

    def load(self, gameboard_string: str) -> None:
        """Load all values of the gameboard"""
        self.gameboard.load(gameboard_string)

    def solve(self, swap: bool) -> ResultList:
        """Solve the spellcast game"""
        self.timer.reset_timer()
        spellsolver = SpellSolver(self.app.validate, self.gameboard)
        return spellsolver.word_list(swap=int(swap), timer=self.timer)


class BaseUI:
    """Represents a base implementation of UI with all basics methods"""

    def __init__(self) -> None:
        self.timer: Timer = Timer()
        self.gameboard: GameBoard = GameBoard()
        self.validate: WordValidate = WordValidate()

        print(f"Spellsolver {VERSION} - fabaindaiz")
        self.timer.reset_timer()
        self.validate.init_trie()
        print(
            f"WordValidate successfully initialized (elapsed time: {self.timer.elapsed_seconds()} seconds)"
        )

    def safesolver(self) -> ThreadSolver:
        return ThreadSolver(self)

    def load(self, gameboard_string: str) -> None:
        """Load all values of the gameboard"""
        self.gameboard.load(gameboard_string)

    def solve(self, swap: int) -> ResultList:
        """Solve the spellcast game"""
        self.timer.reset_timer()
        spellsolver = SpellSolver(self.validate, self.gameboard)
        return spellsolver.word_list(swap=int(swap), timer=self.timer)

    def mainloop(self) -> bool:
        """Mainloop of the Graphic UI"""
        raise NotImplementedError()
