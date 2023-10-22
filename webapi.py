import uvicorn
from fastapi import FastAPI
from src.interfaces.webapi.baseapi import BaseAPI, BaseRouter
from src.interfaces.webapi.apirouter import SolverRouter
from src.interfaces.baseui import BaseUI
from src.config import VERSION, HOST, PORT


class WebAPI(BaseUI):
    """Web API"""

    def __init__(self) -> None:
        super().__init__()

        self.app: BaseAPI = BaseAPI(version=VERSION)
        self.api: FastAPI = self.app.api

        self.webconfig: uvicorn.Config = uvicorn.Config(
            self.api, host=HOST, port=PORT, log_level="info"
        )
        self.server: uvicorn.Server = uvicorn.Server(config=self.webconfig)

        self.solver: BaseRouter = SolverRouter(self, tags=["spellsolver"])
        self.api.include_router(self.solver.router)

    def mainloop(self) -> bool:
        """Mainloop of the WebAPI"""
        self.server.run()
        return False


if __name__ == "__main__":
    app = WebAPI()

    loop = True
    while loop:
        loop = app.mainloop()
