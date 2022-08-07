from decimal import Decimal
from typing import Callable, NamedTuple, Optional, Sequence

# DeliveryChargeRule returns cost of delivery if applicable, else None
DeliveryChargeRule = Callable[[Decimal], Optional[Decimal]]


class Product(NamedTuple):
    name: str
    code: str
    price: Decimal


class ProductNotFound(Exception):
    pass


class ProductCatalogue:
    def __init__(self, products: Sequence[Product]) -> None:
        self.products_database = {p.code: p for p in products}

    def get_product(self, product_code: str) -> Product:
        try:
            return self.products_database[product_code]
        except KeyError:
            raise ProductNotFound(product_code)
