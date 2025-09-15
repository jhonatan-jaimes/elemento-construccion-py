from fastapi import FastAPI


class Api:
    def __init__(self):
        self.app = FastAPI(
            title="Elementos de construccion",
            description="Api para crear elementos de construccion",
            version="1.0.0"
        )


api = Api()
