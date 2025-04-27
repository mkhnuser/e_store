from fastapi import FastAPI

from .routes.customers_api_endpoints import customers_router
from .routes.sellers_api_endpoints import sellers_router
from .routes.products_api_endpoints import products_router


app = FastAPI(debug=True)
app.include_router(customers_router)
app.include_router(products_router)
app.include_router(sellers_router)


@app.get("/")
async def get_root():
    return {"success": True}
