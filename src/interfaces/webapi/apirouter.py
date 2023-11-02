from typing import Any, Dict

from src.interfaces.webapi.interfaces import Response, SolverData
from src.interfaces.webapi.baseapi import BaseRouter
from src.interfaces.baseui import BaseUI


class SolverRouter(BaseRouter):
    """Represents a spellsolver fastapi router"""

    def __init__(self, app: BaseUI, **kwargs: dict):
        super().__init__(**kwargs)
        self.app: BaseUI = app

        @self.router.post("/solve")
        async def spellsolver_solve(data: SolverData) -> Response:
            """Endpoint that solve spellsolver game"""
            response = self.solve(data)

            if not response["successful"]:
                return self.error(response)
            return response

    def solve(self, data: SolverData) -> Dict[str, Any]:
        """Solve a spellsolver game"""
        try:
            solver = self.app.safesolver()
            solver.load(data.gameboard)

            if data.mult:
                mult_cord = (int(data.mult[0]), int(data.mult[1]))
                solver.gameboard.set_mult_word(mult_cord)
            if data.DL:
                DL_cord = (int(data.DL[0]), int(data.DL[1]))
                solver.gameboard.set_mult_letter(DL_cord, 2)
            if data.TL:
                TL_cord = (int(data.TL[0]), int(data.TL[1]))
                solver.gameboard.set_mult_letter(TL_cord, 3)
            if data.gems:
                gem_cord = tuple(
                    (int(gem[0]), int(gem[1])) for gem in data.gems
                )
                solver.gameboard.set_gems(gem_cord)

            results = solver.solve(data.swap)
            sorted_words = results.sorted_words()
            sorted_dict = results.words_to_dict(sorted_words[:10])
            response = {
                "elapsed": results.timer.elapsed_millis(),
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
