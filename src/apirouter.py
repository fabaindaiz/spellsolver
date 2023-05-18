from fastapi import APIRouter


router = APIRouter(
    tags=["spellsolver"],
)

@router.post("/solve")
async def spellsolver_solve():
    """Solve spellsolver game"""
    pass