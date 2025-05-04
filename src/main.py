from contextlib import asynccontextmanager

from fastapi import FastAPI

###
# ALWAYS MAKE SURE ENVIRONMENT IS LOADED.
from dotenv import load_dotenv

load_dotenv("./.env.production")
###

from .routes import customers_router
from .routes import sellers_router
from .routes import products_router
from .db_models import Base
from .db import engine


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
