from src.spellsolver import SpellSolver
from src.validate import WordValidate
from src.gameboard import GameBoard
from src.utils import Timer


class BaseUI:
    """Represents a base implementation of UI with all basics methods"""
    def __init__(self) -> None:
        self.timer: Timer = Timer()
        self.validate = WordValidate()
        self.gameboard = GameBoard()

        print("WordValidate is being initialized, this will take several seconds")
        self.timer.reset_timer()
        self.validate.load_file("src/wordlist/wordlist_english.txt")
        print(f"WordValidate successfully initialized (elapsed time: {self.timer.elapsed_seconds()} seconds)")

    def load(self, gameboard_string: str) -> None:
        """Load all values of the gameboard"""
        self.gameboard.load(gameboard_string)

    def solve(self, swap: bool, num: int=10) -> list:
        """Solve the spellcast game"""
        self.timer.reset_timer()
        spellsolver = SpellSolver(self.validate, self.gameboard)
        word_list = spellsolver.word_list(swap=swap)

        print(f"The following words have been found (elapsed time: {self.timer.elapsed_millis()} milliseconds)")
        print([word.text() for word in word_list[:num]])
        return [word.text() for word in word_list[:num]]