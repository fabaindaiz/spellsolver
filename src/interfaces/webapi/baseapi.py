from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.interfaces.webapi.baserouter import BaseRouter


class BaseAPI:
    """Represents a abstract fastapi API"""

    def __init__(self, version: str) -> None:
        self.api = FastAPI(title="Spellsolver API", docs_url="/docs", version=version)

        self.api.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def include_router(self, router: BaseRouter):
        """Include a router in the API"""
        self.api.include_router(router.router)
