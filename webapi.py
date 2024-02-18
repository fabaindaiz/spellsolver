import uvicorn
from fastapi import FastAPI

from src import HOST, PORT, VERSION
from src.interfaces import BaseUI
from src.interfaces.webapi import BaseAPI, BaseRouter, SolverRouter


class WebAPI(BaseUI):
    """Web API"""

    def __init__(self) -> None:
        super().__init__()
        self.init()

        self.app: BaseAPI = BaseAPI(version=VERSION)
        self.api: FastAPI = self.app.api

        self.webconfig: uvicorn.Config = uvicorn.Config(
            app = self.api,
            host = HOST,
            port = PORT,
            log_level = "info"
        )
        self.server: uvicorn.Server = uvicorn.Server(config=self.webconfig)

        self.solver: BaseRouter = SolverRouter(self, tags={"spellsolver": "true"})
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
