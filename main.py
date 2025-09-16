from src.api import api
import uvicorn
from src.elemento import elemento_routes

app = api.app


def run():
    app.include_router(elemento_routes)
    uvicorn.run(app, host="localhost", port=8000)


if __name__ == '__main__':
    run()
