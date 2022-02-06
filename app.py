from fastapi import FastAPI

from bootstrap import bootstrap


def create_app() -> FastAPI:
    app = FastAPI()
    bootstrap(app)
    return app
