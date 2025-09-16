class Medidas2D:
    def __init__(self, largo: float = 0.0, ancho: float = 0.0):
        self.largo = largo
        self.ancho = ancho


class Medidas3D(Medidas2D):
    def __init__(self, largo: float = 0.0, ancho: float = 0.0, alto: float = 0.0):
        super().__init__(largo, ancho)
        self.alto = alto


class Medidas:
    def __init__(self, kind_medidas: str = "", medidas2d: Medidas2D = None, medidas3d: Medidas3D = None):
        self.kind_medidas = kind_medidas
        self.medidas2d = medidas2d
        self.medidas3d = medidas3d
