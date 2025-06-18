# api/__init__.py
from fastapi import APIRouter
from api.v1 import submit_data

api_router = APIRouter()

api_router.include_router(
    submit_data.router,
    prefix="",
    tags=["Pereval"]
)