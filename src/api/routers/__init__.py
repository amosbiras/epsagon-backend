from typing import List

from fastapi import APIRouter

from .requests import requests_metrics_router

routers: List[APIRouter] = [
    requests_metrics_router,
]
