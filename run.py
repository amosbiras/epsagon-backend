import uvicorn

from typing import NoReturn

from app import create_app


def run() -> NoReturn:
    app = create_app()
    uvicorn.run(app)


if __name__ == '__main__':
    run()
