from fastapi import FastAPI
from src.baseapi import BaseAPI, BaseRouter
from src.apirouter import SolverRouter
from src.baseui import BaseUI


class WebAPI(BaseUI):
    """Console UI"""
    def __init__(self) -> None:
        super().__init__()

        self.app: BaseAPI = BaseAPI()
        self.api: FastAPI = self.app.api

        self.solver: BaseRouter = SolverRouter(self, tags=["spellsolver"])
        self.api.include_router(self.solver.router)


app = WebAPI()
