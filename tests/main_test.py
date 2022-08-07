from decimal import Decimal

import pytest

from src.main import Product, ProductCatalogue, ProductNotFound


@pytest.fixture
def product_catalogue() -> ProductCatalogue:
    products = [
        Product(name="Red Widget", code="R01", price=Decimal("32.95")),
        Product(name="Green Widget", code="G01", price=Decimal("24.95")),
        Product(name="Blue Widget", code="B01", price=Decimal("7.95")),
    ]
    return ProductCatalogue(products)


def test_product_catalogue(product_catalogue) -> None:
    product = product_catalogue.get_product("R01")
    assert product.code == "R01"


def test_product_catalogue_product_not_found(product_catalogue) -> None:
    with pytest.raises(ProductNotFound):
        product_catalogue.get_product("xyz")
