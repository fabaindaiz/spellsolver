from pydantic import BaseModel
from src.interfaces.baseapi import BaseRouter
from src.interfaces.baseui import BaseUI


class Response(BaseModel):
    successful: bool
    message: str
    data: object

class SolverData(BaseModel):
    """Data model for spellsolver_solve endpoint"""
    gameboard: str
    mult: tuple[int] | None = None
    DL: tuple[int] | None = None
    TL: tuple[int] | None = None
    swap: bool | None = None


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
    
    def solve(self, data: SolverData) -> dict[str, object]:
        """Solve a spellsolver game"""
        try:
            solver = self.app.safesolver()
            solver.load(data.gameboard)

            if data.mult:
                solver.gameboard.set_mult_word(data.mult)
            if data.DL:
                solver.gameboard.set_mult_letter(data.DL, 2)
            if data.TL:
                solver.gameboard.set_mult_letter(data.TL, 3)
            
            results = solver.solve(data.swap)
            sorted_data = results.sorted(api=True)
            response = {
                "elapsed": results.timer.elapsed_millis(),
                "results": sorted_data
            }
            return {
                "successful": True, "message": "Spellsolver successfully found a result", "data": response }
    
        except Exception as e:
            return { "successful": False, "message": "Spellsolver cannot find a result", "data": e }
