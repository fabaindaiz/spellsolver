from typing import Any
from fastapi import FastAPI, APIRouter, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


class BaseRouter:
    """Represents a abstract fastapi router"""
    def __init__(self, **kwargs: dict) -> None:
        self.router: APIRouter = APIRouter(**kwargs)
        
    def error(self, response: Any) -> JSONResponse:
        """Return a default error with a message"""
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN,
            content=jsonable_encoder(response),
        )

class BaseAPI:
    """Represents a abstract fastapi API"""
    def __init__(self, version: str) -> None:
        self.api = FastAPI(
            title="Spellsolver API",
            docs_url="/docs",
            version=version
            )
        
        self.api.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"]
            )
    
    def include_router(self, router: BaseRouter):
        """Include a router in the API"""
        self.api.include_router(router.router)
