from decimal import Decimal
from typing import Callable, NamedTuple, Optional, Sequence

# DeliveryChargeRule returns cost of delivery if applicable, else None
DeliveryChargeRule = Callable[[Decimal], Optional[Decimal]]

# SpecialOffer returns discount amount based on basket
SpecialOffer = Callable[["Basket"], Decimal]


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


class Basket:
    def __init__(
        self,
        product_catalogue: ProductCatalogue,
        delivery_charge_rules: Sequence[DeliveryChargeRule],
        special_offers: Optional[Sequence[SpecialOffer]] = None,
    ) -> None:
        self.product_catalogue = product_catalogue
        self.delivery_charge_rules = delivery_charge_rules
        self.special_offers = special_offers or []
        self.products: list[Product] = []

    def add(self, product_code: str) -> None:
        product = self.product_catalogue.get_product(product_code)
        self.products.append(product)

    def total(self) -> Decimal:
        """
        Return the total cost of the basket,
        taking into account the delivery and offer rules.
        """
        raw_total = sum(p.price for p in self.products)
        total_with_discount = (
            raw_total - self.__get_best_special_offer_discount()
        )
        delivery_charge = self.__get_delivery_cost(total_with_discount)
        return total_with_discount + delivery_charge

    def __get_delivery_cost(self, cost: Decimal) -> Decimal:
        if self.delivery_charge_rules and self.products:
            return max(
                delivery_cost
                for charge_rule in self.delivery_charge_rules
                if (delivery_cost := charge_rule(cost)) is not None
            ) or Decimal("0")
        return Decimal("0")

    def __get_best_special_offer_discount(self) -> Decimal:
        return (
            max(offer(self) for offer in self.special_offers)
            if self.special_offers
            else Decimal("0")
        )

    def __repr__(self) -> str:
        return f"<Basket total: {self.total():.2f}>"
