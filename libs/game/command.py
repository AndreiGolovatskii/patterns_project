import logging
from abc import abstractproperty

import attr

from libs.game.game import Game
from libs.base_units.base_unit import BaseUnit
from libs.terrain.terrain import Cell, Terrain, TerrainSpot


@attr.s
class Command:
    author_id = attr.ib(validator=attr.validators.is_instanceof(str))
    author = attr.ib(init=False)

    def __attrs_post_init__(self):
        self.author = self.game.playes.get(self.author_id, None)
        if not self.author:
            raise Exception("user is not recognized")

    def execute(self, game: Game):
        """execute command"""
        if not self.author:
            return False
        return self._execute(game)


@attr.s
class BuyUnitCommand(Command):
    unit_class = attr.ib()
    unit_position = attr.ib()

    def _execute(self, game):
        if not game.terrain.can_get_spot(self.unit_position, self.unit_class.size):
            return False

        if not game.market.can_buy(self.unit_class):
            return False

        price = game.market.get_price(self.unit_class)
        if not self.author.can_buy(price):
            return False

        self.author.wallet -= price
        unit: BaseUnit = game.market.buy(self.unit_class)
        terrain_spot: TerrainSpot = game.terrain.get_spot(
            self.unit_position, self.unit_class.size
        )
        unit.spot = terrain_spot
        self.author.add_unit(unit)
        return True


@attr.s
class RemoveUnitCommand(Command):
    unit_id = attr.ib(validator=attr.validators.instance_of(str))

    def _execute(self, game):
        try:
            unit = self.author.get_unit(self.unit_id)
        except Exception:
            logging.error("no unit with id")
            return False

        game.terrain.remove_spot(unit.spot)
        self.author.remove_unit(unit_id)
