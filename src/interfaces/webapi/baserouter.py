from typing import Any

from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


class BaseRouter:
    """Represents a abstract fastapi router"""

    def __init__(self, **kwargs: dict) -> None:
        self.router: APIRouter = APIRouter(**kwargs)

    def error(self, response: Any) -> JSONResponse:
        """
        Return a default error with a message.

        Args:
            response (Any): The error response content.

        Returns:
            JSONResponse: A FastAPI JSONResponse with an error status.
        """
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN,
            content=jsonable_encoder(response),
        )
