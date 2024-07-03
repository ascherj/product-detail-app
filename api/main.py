from fastapi import FastAPI

from routers import product

app = FastAPI()

app.include_router(product.router)
