from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from core.logger import LOGGING_CONFIG
import logging.config
from api import api_router

app = FastAPI()
logging.config.dictConfig(LOGGING_CONFIG)
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

app.include_router(api_router)
