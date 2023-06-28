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
        if self.mult.DL_cord != None:
            self.app.gameboard.set_mult_letter(self.mult.DL_cord, 2)
        if self.mult.TL_cord != None:
            self.app.gameboard.set_mult_letter(self.mult.TL_cord, 3)
        
        results = self.app.solve(swap)
        sorted = results.sorted(console=True)
        self.set_results(sorted)

class MultHandler:
    """Handle Spellcast word & letter multipliers"""
    def __init__(self, board: Board) -> None:
        self.board: Board = board

        self.mult_cord: tuple = None
        self.DL_cord: tuple = None
        self.TL_cord: tuple = None
    
    def set_mult_word(self, cord: tuple) -> None:
        """Set a mult_word in a tile"""
        if self.mult_cord != None:
            self.board.tiles[self.mult_cord].multiplier("black")

        self.mult_cord = cord
        self.board.tiles[self.mult_cord].multiplier("deep pink")

    def set_mult_DL(self, cord: tuple) -> None:
        """Set a mult_DL in a tile"""
        if self.DL_cord != None:
            self.board.tiles[self.DL_cord].multiplier("black")
        
        self.DL_cord = cord
        self.board.tiles[self.DL_cord].multiplier("gold")

    def set_mult_TL(self, cord: tuple) -> None:
        """Set a mult_TL in a tile"""
        if self.TL_cord != None:
            self.board.tiles[self.TL_cord].multiplier("black")
        
        self.TL_cord = cord
        self.board.tiles[self.TL_cord].multiplier("gold")

    def configure_mult(self) -> None:
        """Change colors of a tile based in the multipliers"""
        if self.mult_cord != None:
            self.board.tiles[self.mult_cord].multiplier("deep pink")
        if self.DL_cord != None:
            self.board.tiles[self.DL_cord].multiplier("gold")
        if self.TL_cord != None:
            self.board.tiles[self.TL_cord].multiplier("gold")
        
    def remove_mult(self) -> None:
        """Remove colors of a tile"""
        if self.mult_cord != None:
            self.board.tiles[self.mult_cord].multiplier("black")
        if self.DL_cord != None:
            self.board.tiles[self.DL_cord].multiplier("black")
        if self.TL_cord != None:
            self.board.tiles[self.TL_cord].multiplier("black")
        
        self.mult_cord = None
        self.DL_cord = None
        self.TL_cord = None
