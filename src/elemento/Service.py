from src.elemento import Elemento


class Service:
    def __init__(self):
        self.repo = []

    def save_elemento(self, elemento: Elemento):
        self.repo.append(elemento)

    def delete_elementos(self):
        self.repo = []

    def get_elementos(self):
        return self.repo


service = Service()
