from src.baseui import BaseUI


class ConsoleUI(BaseUI):
    """Console UI"""
    def __init__(self) -> None:
        super().__init__()

    def mainloop(self) -> None:
        """Mainloop of the Console UI"""
        gameboard_string = input("Insert a gameboard: ")
        self.load(gameboard_string)

        mult_string = input("Insert 2x cord: ")
        if mult_string != "":
            mult_cord = (int(mult_string[0]), int(mult_string[1]))
            self.gameboard.set_mult_word(mult_cord)
        
        DL_string = input("Insert DL cord: ")
        if DL_string != "":
            DL_cord = (int(DL_string[0]), int(DL_string[1]))
            self.gameboard.set_mult_letter(DL_cord, 2)
        
        TL_string = input("Insert TL cord: ")
        if TL_string != "":
            TL_cord = (int(TL_string[0]), int(TL_string[1]))
            self.gameboard.set_mult_letter(TL_cord, 3)

        swap = input("Use swap?: ") == "1"
        self.solve(swap)


if __name__ == "__main__":
    app = ConsoleUI()

    while(True):
        try:
            app.mainloop()
        except Exception as e:
            print("Exception", e)
