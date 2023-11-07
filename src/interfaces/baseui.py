from src import CONSOLE, SWAP, VERSION
from src.modules import SpellSolver
from src.modules.gameboard import GameBoard, ResultList
from src.modules.validate import WordValidate
from src.utils import Timer


class GameSolver:
    def __init__(self, validate: WordValidate, game_board: GameBoard, timer: Timer):
        """
        Initialize a GameSolver for solving word combinations on the game board.

        Args:
            validate (WordValidate): The word validation utility.
            game_board (GameBoard): The game board.
            timer (Timer): The timer utility.
        """
        self.validate = validate
        self.game_board = game_board
        self.timer = timer

    def solve(self, swap: int) -> ResultList:
        """
        Solve the game with a specified swap value.

        Args:
            swap (int): The swap value.

        Returns:
            ResultList: A list of word combinations.
        """
        self.timer.reset_timer()
        spellsolver = SpellSolver(self.validate, self.game_board)
        return spellsolver.word_list(swap=int(swap), timer=self.timer)


class BaseUI:
    def __init__(self):
        """
        Initialize a BaseUI for managing the game interface.
        """
        self.timer = Timer()
        self.game_board = GameBoard()
        self.validate = WordValidate()

    def init_spellsolver(self, swap: int = SWAP):
        """
        Initialize the word validation utility with a specified swap value.

        Args:
            swap (int, optional): The swap value.
        """
        if CONSOLE:
            print(f"Spellsolver {VERSION} - fabaindaiz")
            print("WordValidate is being initialized, this will take several seconds")
        self.timer.reset_timer()
        self.validate.init_trie(swap=swap)

        elapsed_seconds = self.timer.elapsed_seconds()
        if CONSOLE:
            print(
                f"WordValidate successfully initialized (elapsed time: {elapsed_seconds} seconds)"
            )

    def safe_solver(self) -> GameSolver:
        """
        Create a safe GameSolver instance.

        Returns:
            GameSolver: A GameSolver instance.
        """
        return GameSolver(self.validate, self.game_board, self.timer)

    def load(self, game_board_string: str):
        """
        Load a game board from a string representation.

        Args:
            game_board_string (str): The string representation of the game board.
        """
        self.game_board.load(game_board_string)

    def solve(self, swap: int) -> ResultList:
        """
        Solve the game board with a specified swap value.

        Args:
            swap (int): The swap value.

        Returns:
            ResultList: A list of word combinations.
        """
        return self.safe_solver().solve(swap)

    def mainloop(self) -> bool:
        """
        The main loop of the game. (Needs to be implemented by a derived class)
        """
        raise NotImplementedError()
