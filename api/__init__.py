# api/__init__.py
from fastapi import APIRouter
from api.v1.auth import auth_router
from api.v1.snippet import snippet_router

api_router = APIRouter()

api_router.include_router(auth_router)
api_router.include_router(snippet_router)
