from pydantic import BaseModel


class Settings(BaseModel):
    version: str
    debug: bool

    spellsolver: 'Spellsolver'
    heuristic: 'Heuristic'
    wordlist: 'Wordlist'
    fastapi: 'Fastapi'


class Spellsolver(BaseModel):
    """"""
    swaps: int

class Heuristic(BaseModel):
    """"""
    active: bool
    mode: str

class Wordlist(BaseModel):
    """"""
    source: str
    wordlist: str

class Fastapi(BaseModel):
    """"""
    host: str
    port: int
