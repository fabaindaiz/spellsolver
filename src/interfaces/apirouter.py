from typing import Any, Dict
from pydantic import BaseModel
from src.interfaces.baseapi import BaseRouter
from src.interfaces.baseui import BaseUI


class Response(BaseModel):
    successful: bool
    message: str
    data: Any

class SolverData(BaseModel):
    """Data model for spellsolver_solve endpoint"""
    gameboard: str
    mult: str | None = None
    DL: str | None = None
    TL: str | None = None
    swap: int | None = None


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
            
            results = solver.solve(data.swap)
            sorted_data = results.sorted_dict()
            response = {
                "elapsed": results.timer.elapsed_millis(),
                "results": sorted_data
            }
            return {
                "successful": True, "message": "Spellsolver successfully found a result", "data": response }
    
        except Exception as e:
            return { "successful": False, "message": "Spellsolver cannot find a result", "data": e }
