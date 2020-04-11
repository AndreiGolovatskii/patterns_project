import logging

import attr

from libs.base_unit.base_unit import BaseUnit


@attr.s
class Market:
    price = attr.ib(factory=dict)

    def can_buy(self, product):
        return product in self.price

    def get_price(self, product):
        return self.price[product]

    def buy(self, product):
        res = product()
        return res

    def set_product_price(self, product, price):
        self.price[product] = price
