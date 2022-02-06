from typing import NoReturn

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from src.api import routers
from src.exceptions import HTTPException


def bootstrap(app: FastAPI) -> NoReturn:
    __add_routers(app)
    __handle_exceptions(app)


def __add_routers(app: FastAPI) -> NoReturn:
    for router in routers:
        app.include_router(router)


def __handle_exceptions(app: FastAPI) -> NoReturn:
    app.add_exception_handler(HTTPException, __handle_http_exception)
    app.add_exception_handler(Exception, __handle_general_exception)


def __handle_http_exception(request: Request, exception: HTTPException) -> JSONResponse:
    return JSONResponse(
        status_code=exception.status_code,
        content={'error': exception.message}
    )


def __handle_general_exception(request: Request, exception: Exception) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={'error': 'An internal error occurred. Please wait for the maintenance to handle the problem.'}
    )
