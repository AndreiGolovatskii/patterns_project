import logging

import attr


@attr.s
class Player:
    wallet = attr.ib()
    player_name = attr.ib()
    player_id = attr.ib()
    units_by_id = attr.ib(factory=dict)

    def add_unit(self, unit):
        self.units_by_id[unit.unit_id] = unit

    def get_unit(self, unit_id):
        return self.units_by_id[unit_id]

    def remove_unit(self, unit_id):
        del self.units_by_id[unit_id]

    def can_buy(self, price):
        return self.wallet >= price

    def visit(self, visitor):
        visitor.visit_player(self)

    def iteration(self, elapsed_time):
        for unit in self.units_by_id.values():
            self.wallet += unit.work() * elapsed_time
