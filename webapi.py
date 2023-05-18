from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import src.apirouter as apirouter
from src.baseui import BaseUI


class WebAPI(BaseUI):
    """Console UI"""
    def __init__(self) -> None:
        super().__init__()

        self.app = FastAPI(
            title="Spellsolver API",
            version="1.3",
            docs_url="/docs"
            )
        
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"]
            )
        
        self.app.include_router(apirouter.router)
    
    def set_multipliers(self, mult_string: str, DL_string: str, TL_string: str) -> None:
        """Set values for multipliers"""
        if mult_string and mult_string != "":
            mult_cord = (int(mult_string[0]), int(mult_string[1]))
            self.gameboard.set_mult_word(mult_cord)
        
        if DL_string and DL_string != "":
            DL_cord = (int(DL_string[0]), int(DL_string[1]))
            self.gameboard.set_mult_letter(DL_cord, 2)
        
        if TL_string and TL_string != "":
            TL_cord = (int(TL_string[0]), int(TL_string[1]))
            self.gameboard.set_mult_letter(TL_cord, 3)
  

    def mainloop(self) -> bool:
        """Main loop of the Console UI"""

        try:
            gameboard_string = ""
            self.load(gameboard_string)

            mult_string = ""
            DL_string = ""
            TL_string = ""
            self.set_multipliers(mult_string, DL_string, TL_string)

            swap = "1"
            self.solve(swap)
        except Exception as e:
            print("Exception:", e)
        
        return True


if __name__ == "__main__":
    app = WebAPI()

    loop = True
    while(loop):
        loop = app.mainloop()