from abc import ABC

from pydantic import BaseModel


class Elemento(ABC):
    def __init__(self, id: int = 0, name: str = "", lot: int = 0):
        self.id = id
        self.name = name
        self.lot = lot
