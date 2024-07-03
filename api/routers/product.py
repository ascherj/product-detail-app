from fastapi import APIRouter, Depends

from models.product import ProductIn, ProductOut
from services.product import ProductRepository

router = APIRouter()

@router.post("/products")
def create_product(product: ProductIn, repo: ProductRepository = Depends()) -> ProductOut:
    return repo.create_product(product)


@router.get("/products")
def get_products(repo: ProductRepository = Depends()) -> list[ProductOut]:
    return repo.get_products()
