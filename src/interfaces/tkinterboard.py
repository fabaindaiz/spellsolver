from src.interfaces.tkinterwidget import Board
from src.interfaces.baseui import BaseUI


class TkinterBoard(Board):
    """Represents a board with his logic"""
    def __init__(self, app: BaseUI) -> None:
        super().__init__(app)
        self.mult: MultHandler = MultHandler(self)

    def button_command(self, swap: int) -> None:
        """Execute SpellSolver when a button is pressed"""
        gameboard_string = "".join(tile.letter() for tile in self.tiles.values())
        self.app.gameboard.load(gameboard_string)

        if self.mult.mult_cord != None:
            self.app.gameboard.set_mult_word(self.mult.mult_cord)
        if self.mult.letter_cord != None:
            self.app.gameboard.set_mult_letter(self.mult.letter_cord, self.mult.letter_mult)
        
        results = self.app.solve(swap)
        sorted = results.sorted(console=True)
        self.set_results(sorted)

class MultHandler:
    """Handle Spellcast word & letter multipliers"""
    def __init__(self, board: Board) -> None:
        self.board: Board = board

        self.mult_cord: tuple = None
        self.letter_mult: int = None
        self.letter_cord: tuple = None
    
    def set_mult_word(self, cord: tuple) -> None:
        """Set a mult_word in a tile"""
        if self.mult_cord != None:
            self.board.tiles[self.mult_cord].multiplier("black")
        
        self.mult_cord = cord
        self.configure_mult()

    def set_mult_letter(self, cord: tuple, mult: int) -> None:
        """Set a mult_TL in a tile"""
        if self.letter_cord != None:
            self.board.tiles[self.letter_cord].multiplier("black")

        self.letter_mult = mult
        self.letter_cord = cord
        self.configure_mult()

    def configure_mult(self) -> None:
        """Change colors of a tile based in the multipliers"""
        if self.letter_cord != None:
            self.board.tiles[self.letter_cord].multiplier("gold")
        if self.mult_cord != None:
            self.board.tiles[self.mult_cord].multiplier("deep pink")
        
    def remove_mult(self) -> None:
        """Remove colors of a tile"""
        if self.letter_cord != None:
            self.board.tiles[self.letter_cord].multiplier("black")
        if self.mult_cord != None:
            self.board.tiles[self.mult_cord].multiplier("black")
        
        self.letter_cord = None
        self.mult_cord = None
