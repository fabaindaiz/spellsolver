from src import CONSOLE, SWAP, VERSION
from src.entities import Coordinates
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

    def set_modifiers(self, blocked_string: str, gems_string: str) -> None:
        if blocked_string!= "":
            cords = blocked_string.split(".")
            blocked = (Coordinates.from_string(cord) for cord in cords)
            self.game_board.set_blocked(blocked)

        if gems_string != "":
            cords = gems_string.split(".")
            gems = (Coordinates.from_string(cord) for cord in cords)
            self.game_board.set_gems(gems)

    def set_multipliers(self, X2_string: str, DL_string: str, TL_string: str) -> None:
        """Set values for multipliers"""
        if X2_string!= "":
            cords = X2_string.split(" ")
            word_mult = {Coordinates.from_string(cord): 2 for cord in cords}
            self.game_board.set_word_mult(word_mult)

        if DL_string != "":
            cords = DL_string.split(" ")
            tile_mult = {Coordinates.from_string(cord): 2 for cord in cords}
            self.game_board.set_tile_mult(tile_mult)

        if TL_string != "":
            cords = TL_string.split(" ")
            tile_mult = {Coordinates.from_string(cord): 3 for cord in cords}
            self.game_board.set_tile_mult(tile_mult)

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
        return spellsolver.word_list(swap=swap, timer=self.timer)


class BaseUI:
    def __init__(self):
        """
        Initialize a BaseUI for managing the game interface.
        """
        self.timer = Timer()
        self.validate = WordValidate()

    def init(self, swap: int = SWAP):
        """
        Initialize the word validation utility with a specified swap value.

        Args:
            swap (int, optional): The swap value.
        """
        if CONSOLE:
            print(f"Spellsolver {VERSION}")
            print("WordValidate is being initialized, this will take several seconds")
        self.timer.reset_timer()
        self.validate.init(swap=swap)

        elapsed_seconds = self.timer.elapsed_seconds
        if CONSOLE:
            print(
                f"WordValidate successfully initialized (elapsed time: {elapsed_seconds} seconds)"
            )

    def load(self, game_board_string: str) -> GameSolver:
        """
        Load a game board from a string representation and create a GameSolver instance.

        Args:
            game_board_string (str): The string representation of the game board.
        
        Returns:
            GameSolver: A GameSolver instance.
        """
        timer = Timer()
        game_board = GameBoard()
        game_board.init(game_board_string)
        return GameSolver(self.validate, game_board, timer)

    def mainloop(self) -> bool:
        """
        The main loop of the game. (Needs to be implemented by a derived class)
        """
        raise NotImplementedError()
