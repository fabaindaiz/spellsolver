from typing import Any, Optional

from pydantic import BaseModel


class Response(BaseModel):
    """Data model for spellsolver_solve endpoint"""

    successful: bool
    message: str
    data: Any


class SolverData(BaseModel):
    """Data model for spellsolver_solve endpoint"""

    gameboard: str
    mult: Optional[str] = None
    DL: Optional[str] = None
    TL: Optional[str] = None
    swap: Optional[int] = None
    gems: Optional[tuple[str, ...]] = None
    ices: Optional[tuple[str, ...]] = None
