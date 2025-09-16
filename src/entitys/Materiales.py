
class Mortero:
    def __init__(self, kind_area: str = "", cemento: float = 0.0,
                 arena: float = 0.0, agua: float = 0.0):
        self.kind_area = kind_area
        self.cemento = cemento
        self.arena = arena
        self.agua = agua


class Concreto(Mortero):
    def __init__(self, kind: str = "", cemento: float = 0.0,
                 arena: float = 0.0, grava: float = 0.0, agua: float = 0.0):
        super().__init__(kind, cemento, arena, agua)
        self.grava = grava


class Materiales:
    def __init__(self, kind_material: str = "", mortero: Mortero = None, concreto: Concreto = None):
        self.kind_material = kind_material
        self.mortero = mortero
        self.concreto = concreto
