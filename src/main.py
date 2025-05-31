import os
from contextlib import asynccontextmanager

from fastapi import FastAPI

from .routes import users_router
from .routes import products_router
from .db_models import Base
from .db import engine


@asynccontextmanager
async def lifespan(_: FastAPI):
    # THE APP START UP LOGIC GOES HERE.
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()
    # THE APP CLEAN UP LOGIC GOES HERE.


app = FastAPI(lifespan=lifespan, debug=True)
app.include_router(users_router)
app.include_router(products_router)


@app.get(os.environ["APP_API_PATHS_ROOT_INDEX"])
async def get_root():
    return {"success": True}
