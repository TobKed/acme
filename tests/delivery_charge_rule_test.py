from decimal import Decimal

import pytest

from src.delivery_charge_rules import (
    delivery_rule_90_or_more,
    delivery_rule_under_50,
    delivery_rule_under_90,
)


@pytest.mark.parametrize(
    "cost,expected",
    [
        (Decimal("0"), None),
        (Decimal("1"), Decimal("4.95")),
        (Decimal("49"), Decimal("4.95")),
        (Decimal("50"), None),
        (Decimal("51"), None),
    ],
)
def test_delivery_rule_under_50(cost, expected):
    assert delivery_rule_under_50(cost) == expected


@pytest.mark.parametrize(
    "cost,expected",
    [
        (Decimal("0"), None),
        (Decimal("1"), Decimal("2.95")),
        (Decimal("89"), Decimal("2.95")),
        (Decimal("90"), None),
        (Decimal("91"), None),
    ],
)
def test_delivery_rule_under_90(cost, expected):
    assert delivery_rule_under_90(cost) == expected


@pytest.mark.parametrize(
    "cost,expected",
    [
        (Decimal("0"), None),
        (Decimal("1"), None),
        (Decimal("89"), None),
        (Decimal("90"), Decimal(0)),
        (Decimal("91"), Decimal(0)),
    ],
)
def test_delivery_rule_90_or_more(cost, expected):
    assert delivery_rule_90_or_more(cost) == expected
