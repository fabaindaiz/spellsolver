
from gameboard import GameBoard
from validate import WordValidate
from spellsolver import SpellSolver
from utils import valid_word


class ConsoleUI:

    def main_loop(self, validate):
        gameboard_string = input("Insert a gameboard: ")
        if not valid_word(gameboard_string) or len(gameboard_string) != 25:
            return

        mult_string = input("Insert 2x cord: ")
        DL_string = input("Insert DL cord: ")
        TL_string = input("Insert TL cord: ")
        swap_string = input("Use swap?: ")

        gameboard = GameBoard()
        gameboard.init_nodes(gameboard_string)

        if mult_string != "":
            mult_cord = (int(mult_string[0]), int(mult_string[1]))
            gameboard.set_mult_word(mult_cord)
        if DL_string != "":
            DL_cord = (int(DL_string[0]), int(DL_string[1]))
            gameboard.set_mult_letter(DL_cord, 2)
        if TL_string != "":
            TL_cord = (int(TL_string[0]), int(TL_string[1]))
            gameboard.set_mult_letter(TL_cord, 3)

        spellsolver = SpellSolver(validate, gameboard)
        spellsolver.get_word_list(swap=swap_string)


if __name__ == "__main__":
    consoleui = ConsoleUI()
    print("Init WordValidate")
    validate = WordValidate()
    validate.from_file("wordlist_english.txt", swap=True)

    while(True):
        consoleui.main_loop(validate)
