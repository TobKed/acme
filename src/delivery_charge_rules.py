from decimal import Decimal
from typing import Optional

from src.main import DeliveryChargeRule

predefined_delivery_charge_rules: list[DeliveryChargeRule] = []


def predefined_delivery_charge_rule(
    rule: DeliveryChargeRule,
) -> DeliveryChargeRule:
    predefined_delivery_charge_rules.append(rule)
    return rule


@predefined_delivery_charge_rule
def delivery_rule_under_50(basket_cost: Decimal) -> Optional[Decimal]:
    return (
        Decimal("4.95") if basket_cost and basket_cost < Decimal("50") else None
    )


@predefined_delivery_charge_rule
def delivery_rule_under_90(basket_cost: Decimal) -> Optional[Decimal]:
    return (
        Decimal("2.95") if basket_cost and basket_cost < Decimal("90") else None
    )


@predefined_delivery_charge_rule
def delivery_rule_90_or_more(basket_cost: Decimal) -> Optional[Decimal]:
    return (
        Decimal("0") if basket_cost and basket_cost >= Decimal("90") else None
    )
