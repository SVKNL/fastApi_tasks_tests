import os

from dotenv import find_dotenv, load_dotenv
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from src.api import router



def create_fast_api_app() -> FastAPI:


    fastapi_app = FastAPI()

    fastapi_app.include_router(router, prefix='/api')
    return fastapi_app


app = create_fast_api_app()
