from fastapi import FastAPI, APIRouter, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


class BaseRouter:
    def __init__(self, **kwargs) -> None:
        self.router: APIRouter = APIRouter(**kwargs)
        
    def error(self, response) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN,
            content=jsonable_encoder(response),
        )

class BaseAPI:
    def __init__(self) -> None:
        self.api = FastAPI(
            title="Spellsolver API",
            version="1.3",
            docs_url="/docs"
            )
        
        self.api.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"]
            )
    
    def include_router(self, router: BaseRouter):
        self.api.include_router(router.router)
