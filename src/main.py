from contextlib import asynccontextmanager

from fastapi import FastAPI

from .routes.customers_api_endpoints import customers_router
from .routes.sellers_api_endpoints import sellers_router
from .routes.products_api_endpoints import products_router

from .sqlalchemy_models.base import Base


###
# INITIALIZE A DATABASE BY INTERPRETING A MODULE.
from .db.db import engine
###


@asynccontextmanager
async def lifespan(app: FastAPI):
    # THE APP START UP LOGIC GOES HERE.
    Base.metadata.create_all(bind=engine)
    yield
    # THE APP CLEAN UP LOGIC GOES HERE.
    engine.dispose()


app = FastAPI(lifespan=lifespan, debug=True)
app.include_router(customers_router)
app.include_router(products_router)
app.include_router(sellers_router)


@app.get("/")
async def get_root():
    return {"success": True}
