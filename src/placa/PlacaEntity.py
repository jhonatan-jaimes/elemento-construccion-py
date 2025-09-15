from src.elemento import Elemento


class PlacaEntity(Elemento):
    def __init__(self, id: int = 0, name: str = "", material: str = ""):
        super().__init__(id, name)
        self.material = material
