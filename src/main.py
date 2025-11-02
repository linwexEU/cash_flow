from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.api import router
from src.api.middleware.exception_middleware import ExceptionHandlerMiddleware
from src.utils.logger import configure_logging


@asynccontextmanager 
async def lifespan(app: FastAPI): 
    configure_logging()
    yield


def create_app() -> FastAPI: 
    app = FastAPI(lifespan=lifespan, swagger_ui_parameters={"docExpansion": "none"}) 
    
    # Include routers
    app.include_router(router) 

    # Include middlewares
    app.add_middleware(ExceptionHandlerMiddleware)

    return app


app = create_app()
