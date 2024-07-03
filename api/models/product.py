from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    slogan: str
    description: str
    category: str
    default_price: float

class ProductIn(ProductBase):
    pass

class ProductOut(ProductBase):
    id: int
