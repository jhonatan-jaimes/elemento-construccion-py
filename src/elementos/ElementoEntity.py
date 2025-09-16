from src.elemento import Elemento
from src.entitys import Medidas, Areas, Materiales


class ElementoEntity(Elemento):
    def __init__(self, id: int = 0, name: str = "", lot: int = 0,
                 medidas: Medidas = None, areas: Areas = None, materiales: Materiales = None):
        super().__init__(id, name, lot)
        self.medidas = medidas
        self.areas = areas
        self.materiales = materiales

