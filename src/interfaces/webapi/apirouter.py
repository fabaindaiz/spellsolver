from typing import Any
from fastapi.responses import JSONResponse

from src.entities import Coordinates
from src.interfaces import BaseUI
from .baseapi import BaseRouter
from .interfaces import SolverData


class SolverRouter(BaseRouter):
    """Represents a spellsolver fastapi router"""

    def __init__(self, app: BaseUI, **kwargs: dict):
        super().__init__(**kwargs)
        self.app: BaseUI = app

        @self.router.post("/solve")
        async def spellsolver_solve(data: SolverData) -> JSONResponse:
            """Endpoint that solve spellsolver game"""
            response = self.solve(data)

            if not response["successful"]:
                return self.error(response)
            return JSONResponse(response)

    def solve(self, data: SolverData) -> dict[str, Any]:
        """Solve a spellsolver game"""
        try:
            solver = self.app.safe_solver()
            solver.game_board.load(data.gameboard)

            if data.mult:
                mult_cord = Coordinates(int(data.mult[0]), int(data.mult[1]))
                solver.game_board.set_mult_word(mult_cord)
            if data.DL:
                DL_cord = Coordinates(int(data.DL[0]), int(data.DL[1]))
                solver.game_board.set_mult_letter(DL_cord, 2)
            if data.TL:
                TL_cord = Coordinates(int(data.TL[0]), int(data.TL[1]))
                solver.game_board.set_mult_letter(TL_cord, 3)
            if data.gems:
                gem_cord = list(Coordinates(int(gem[0]), int(gem[1])) for gem in data.gems)
                solver.game_board.set_gems(gem_cord)
            if data.ices:
                ice_cord = list(Coordinates(int(ice[0]), int(ice[1])) for ice in data.ices)
                solver.game_board.set_ices(ice_cord)

            swap = data.swap if data.swap else 1
            results = solver.solve(swap=swap)
            sorted_words = results.sorted_words
            sorted_dict = results.words_to_dict(sorted_words[:10])
            response = {
                "elapsed": results.timer.elapsed_millis,
                "results": sorted_dict,
            }
            return {
                "successful": True,
                "message": "Spellsolver successfully found a result",
                "data": response,
            }

        except Exception as e:
            return {
                "successful": False,
                "message": "Spellsolver cannot find a result",
                "data": e,
            }
