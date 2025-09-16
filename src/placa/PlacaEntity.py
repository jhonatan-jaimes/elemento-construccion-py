from src.elemento import Elemento
from src.entitys import Medidas, Materiales, Areas


class PlacaEntity(Elemento):
    def __init__(self, id: int = 0, name: str = "", lot: int = 0,
                 medidas_uno: Medidas = None, medidas_dos: Medidas = None, area_general: Areas = None,
                 area_uno: Areas = None, area_dos: Areas = None, material_uno: Materiales = None,
                 material_dos: Materiales = None):
        super().__init__(id, name, lot)
        self.medidas_uno = medidas_uno
        self.medidas_dos = medidas_dos
        self.area_general = area_general
        self.area_uno = area_uno
        self.area_dos = area_dos
        self.material_uno = material_uno
        self.material_dos = material_dos
