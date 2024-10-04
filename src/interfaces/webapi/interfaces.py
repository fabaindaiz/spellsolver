from typing import Any, Optional

from pydantic import BaseModel


class Response(BaseModel):
    """Data model for spellsolver_solve endpoint"""

    successful: bool
    message: str
    data: Any


class SolverData(BaseModel):
    """Data model for spellsolver_solve endpoint"""

    gameboard: str = "rslesrotvegifovxqmbabaaif"
    swap: Optional[int] = 1
    blocked: Optional[str] = ""
    gems: Optional[str] = ""
    x2_mult: Optional[str] = "23"
    dl_mult: Optional[str] = "23"
    tl_mult: Optional[str] = ""
