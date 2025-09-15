from api import api
import uvicorn
from elementos import router as elementos_routes
from elemento import router as elemento_routes

app = api.app


def run():
    app.include_router(elementos_routes)
    app.include_router(elemento_routes)
    uvicorn.run(app, host="localhost", port=8000)


if __name__ == '__main__':
    run()
