from decimal import Decimal

import pytest

from src.main import Basket, Product, ProductCatalogue
from src.special_offers import special_offer_second_red_widget_for_half_price


@pytest.mark.parametrize(
    "nr_of_reds,expected_discount",
    [
        (1, Decimal("0")),
        (2, Decimal("5")),
        (3, Decimal("5")),
        (4, Decimal("10")),
        (5, Decimal("10")),
    ],
)
def test_special_offer_second_red_widget_for_half_price(
    nr_of_reds, expected_discount
):
    product_catalogue = ProductCatalogue(
        [
            Product(name="Red Widget", code="R01", price=Decimal("10.00")),
        ]
    )
    basket = Basket(product_catalogue, [], [])
    for _ in range(nr_of_reds):
        basket.add("R01")
    assert (
        special_offer_second_red_widget_for_half_price(basket)
        == expected_discount
    )
