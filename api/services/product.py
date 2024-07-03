from models.product import ProductIn, ProductOut
from db.pool import pool

class ProductRepository:
    def create_product(self, product: ProductIn) -> ProductOut:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cursor:
                    result = cursor.execute(
                        "INSERT INTO products (name, slogan, description, category, default_price) VALUES (%s, %s, %s, %s, %s) RETURNING *",
                        (product.name, product.slogan, product.description, product.category, product.default_price)
                    )
                    id = cursor.fetchone()[0]
                    old_data = product.model_dump()
                    return ProductOut(id=id, **old_data)
        except Exception as e:
            return {"error": str(e)}

    def get_products(self) -> list[ProductOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT * FROM products")
                    return [self._record_to_ProductOut(record) for record in cursor.fetchall()]
        except Exception as e:
            return {"error": str(e)}

    def _record_to_ProductOut(self, record) -> ProductOut:
        return ProductOut(
            id=record[0],
            name=record[1],
            slogan=record[2],
            description=record[3],
            category=record[4],
            default_price=record[5]
        )
