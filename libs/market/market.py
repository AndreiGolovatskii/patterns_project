import logging

import attr


@attr.s
class Market:
    price = attr.ib(factory=dict)
    units = attr.ib(factory=dict)
    free_unit_id = attr.ib(default=0)

    def can_buy(self, product):
        return product in self.price

    def get_price(self, product):
        return self.price[product]

    def buy(self, product):
        res = product(unit_id=self.free_unit_id)
        self.free_unit_id += 1
        return res

    def set_product_price(self, product, price):
        self.price[product] = price
        self.units[product.class_id] = product

    def visit(self, visitor):
        visitor.visit_market(self)
