import uvicorn
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

        self.webconfig: uvicorn.Config = uvicorn.Config(self.api, port=8080, log_level="info")
        self.server: uvicorn.Server = uvicorn.Server(config=self.webconfig)

        self.solver: BaseRouter = SolverRouter(self, tags=["spellsolver"])
        self.api.include_router(self.solver.router)

    def mainloop(self) -> bool:
        """Mainloop of the Graphic UI"""
        self.server.run()
        return False


if __name__=="__main__":
    app = WebAPI()
    
    loop = True
    while(loop):
        loop = app.mainloop()
