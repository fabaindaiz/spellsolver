from typing import Any
from fastapi.responses import JSONResponse

from src.config import SWAP
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
            solver = self.app.load(data.gameboard)
            solver.set_modifiers(data.blocked, data.gems)
            solver.set_multipliers(data.x2_mult, data.dl_mult, data.tl_mult)
            
            swap = data.swap if data.swap else SWAP
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
