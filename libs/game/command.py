import logging
from abc import abstractproperty

import attr

from libs.base_unit.base_unit import BaseUnit
from libs.terrain.terrain import Cell, Terrain, TerrainSpot, Position


@attr.s
class Command:
    player_id = attr.ib(validator=attr.validators.instance_of(int))
    player = attr.ib(init=False)

    def execute(self, game):
        """execute command"""
        self.player = game.players.get(self.player_id, None)
        if not self.player:
            logging.error("player with id %s not found", self.player_id)
            return False
        return self._execute(game)


@attr.s
class BuyUnitCommand(Command):
    unit_class_id = attr.ib()
    unit_position: Position = attr.ib()

    def _execute(self, game):
        self.unit_class = game.market.units[self.unit_class_id]
        if not game.terrain.can_get_spot(self.unit_position, self.unit_class.size):
            return False

        if not game.market.can_buy(self.unit_class):
            return False

        price = game.market.get_price(self.unit_class)
        if not self.player.can_buy(price):
            return False

        self.player.wallet -= price
        unit: BaseUnit = game.market.buy(self.unit_class)
        terrain_spot: TerrainSpot = game.terrain.get_spot(self.unit_position, self.unit_class.size)
        unit.spot = terrain_spot
        self.player.add_unit(unit)
        return True


@attr.s
class RemoveUnitCommand(Command):
    unit_id = attr.ib(validator=attr.validators.instance_of(str))

    def _execute(self, game):
        try:
            unit = self.player.get_unit(self.unit_id)
        except Exception:
            logging.error("no unit with id")
            return False

        game.terrain.remove_spot(unit.spot)
        self.player.remove_unit(self.unit_id)
        return True


def command_from_json(json):
    if json["action_type"] == "buy_unit":
        return BuyUnitCommand(
            json["player_id"],
            json["unit_class_id"],
            Position(json["position_x"], json["position_y"]),
        )
