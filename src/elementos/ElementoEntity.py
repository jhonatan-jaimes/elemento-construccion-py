from src.elemento import Elemento


class ElementoEntity(Elemento):
    def __init__(self, id: int = 0, name: str = "", lot: int = 0):
        super().__init__(id, name)
        self.lot = lot
