from decimal import Decimal

import pytest

from src.delivery_charge_rules import predefined_delivery_charge_rules
from src.main import Basket, Product, ProductCatalogue, ProductNotFound
from src.special_offers import predefined_special_offers


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


@pytest.fixture
def basket(product_catalogue) -> Basket:
    return Basket(
        product_catalogue,
        predefined_delivery_charge_rules,
        predefined_special_offers,
    )


@pytest.mark.parametrize(
    "product_codes,expected_total",
    [
        (("B01", "G01"), "37.85"),
        (("R01", "R01"), "54.37"),
        (("R01", "G01"), "60.85"),
        (("B01", "G01"), "37.85"),
        (("B01", "B01", "R01", "R01", "R01"), "98.27"),
        ((), "0"),
    ],
)
def test_basic_basket(basket, product_codes, expected_total) -> None:
    for pc in product_codes:
        basket.add(pc)
    assert basket.total() == Decimal(expected_total)


def test_empty_product_catalogue_basket() -> None:
    basket = Basket(
        ProductCatalogue([]),
        predefined_delivery_charge_rules,
        predefined_special_offers,
    )
    with pytest.raises(ProductNotFound):
        basket.add("xyz")
    assert basket.total() == Decimal("0")


def test_empty_delivery_charge_rules(product_catalogue) -> None:
    basket = Basket(product_catalogue, [], predefined_special_offers)
    basket.add("B01")
    basket.add("G01")
    assert basket.total() == Decimal("32.90")


def test_empty_special_offers(product_catalogue) -> None:
    basket = Basket(product_catalogue, predefined_delivery_charge_rules, [])
    for pc in ("B01", "B01", "R01", "R01", "R01"):
        basket.add(pc)
    assert basket.total() == Decimal("114.75")
