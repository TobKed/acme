from decimal import ROUND_UP, Decimal

from src.main import Basket, SpecialOffer

predefined_special_offers: list[SpecialOffer] = []


def predefined_special_offer(offer: SpecialOffer) -> SpecialOffer:
    predefined_special_offers.append(offer)
    return offer


@predefined_special_offer
def special_offer_second_red_widget_for_half_price(basket: "Basket") -> Decimal:
    red_widgets = [p for p in basket.products if "red" in p.name.lower()]
    nr_of_pairs = len(red_widgets) // 2
    discount = (
        nr_of_pairs * (red_widgets[0].price / 2) if nr_of_pairs else Decimal(0)
    )
    return discount.quantize(Decimal(".01"), rounding=ROUND_UP)
