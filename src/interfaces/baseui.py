from src import CONSOLE, SWAP, VERSION
from src.entities import Coordinates
from src.modules import SpellSolver
from src.modules.gameboard import GameBoard, ResultList
from src.modules.validate import WordValidate
from src.utils import Timer


class GameSolver:
    def __init__(self, validate: WordValidate, game_board: GameBoard, timer: Timer):
        self.validate = validate
        self.game_board = game_board
        self.timer = timer

    def set_modifier(self, cords_str: str, modifier_setter: callable):
        if cords_str:
            cords = cords_str.split(" ")
            modifiers = (Coordinates.from_string(cord) for cord in cords)
            modifier_setter(modifiers)

    def set_multiplier(self, cords_str: str, multiplier: int):
        if cords_str:
            cords = cords_str.split(" ")
            mult_dict = {Coordinates.from_string(cord): multiplier for cord in cords}
            self.game_board.set_tile_mult(mult_dict)

    def set_modifiers(self, blocked_string: str, gems_string: str) -> None:
        self.set_modifier(blocked_string, self.game_board.set_blocked)
        self.set_modifier(gems_string, self.game_board.set_gems)

    def set_multipliers(self, x2_string: str, dl_string: str, tl_string: str) -> None:
        self.set_multiplier(x2_string, 2)
        self.set_multiplier(dl_string, 2)
        self.set_multiplier(tl_string, 3)

    def solve(self, swap: int) -> ResultList:
        self.timer.reset_timer()
        spellsolver = SpellSolver(self.validate, self.game_board)
        return spellsolver.word_list(remaining_swaps=swap, timer=self.timer)


class BaseUI:
    def __init__(self):
        self.timer = Timer()
        self.validate = WordValidate()

    def init(self, swap: int = SWAP):
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
        timer = Timer()
        game_board = GameBoard()
        game_board.init(game_board_string)
        return GameSolver(self.validate, game_board, timer)

    def mainloop(self) -> bool:
        raise NotImplementedError()
