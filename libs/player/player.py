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

    def __attrs_post_init__(self):
        self.player_id = 0
        self.player_name = "user"
