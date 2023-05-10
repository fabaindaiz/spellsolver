from gameboard import GameBoard
from validate import WordValidate
from spellsolver import SpellSolver


class ConsoleUI:
    """Console UI"""
    def __init__(self, validate: WordValidate) -> None:
        self.validate: WordValidate = validate

    def mainloop(self) -> None:
        """Mainloop of the Console UI"""
        gameboard_string = input("Insert a gameboard: ")

        mult_string = input("Insert 2x cord: ")
        DL_string = input("Insert DL cord: ")
        TL_string = input("Insert TL cord: ")
        swap = input("Use swap?: ") != "0"

        gameboard = GameBoard(gameboard_string)
        if mult_string != "":
            mult_cord = (int(mult_string[0]), int(mult_string[1]))
            gameboard.set_mult_word(mult_cord)
        if DL_string != "":
            DL_cord = (int(DL_string[0]), int(DL_string[1]))
            gameboard.set_mult_letter(DL_cord, 2)
        if TL_string != "":
            TL_cord = (int(TL_string[0]), int(TL_string[1]))
            gameboard.set_mult_letter(TL_cord, 3)

        spellsolver = SpellSolver(self.validate, gameboard)
        spellsolver.word_list(swap=swap)


if __name__ == "__main__":
    validate = WordValidate()
    validate.load_file("wordlist/wordlist_english.txt")
    app = ConsoleUI(validate)

    while(True):
        try:
            app.mainloop()
        except Exception as e:
            print("Exception", e)
