import pytest

from libs.base_unit.base_unit import DummyUnit
from libs.player.player import Player
from libs.player.resource_wallet import ResourceWallet
from libs.terrain.terrain import Position
from libs.game.command import BuyUnitCommand, RemoveUnitCommand
from libs.game.game import Game


def test_game(default_game):
    first_player = Player(wallet=ResourceWallet(100, 100, 100),
                          player_name="default",
                          player_id=0)

    command = BuyUnitCommand(player_id=0, unit_class_id=DummyUnit.class_id, unit_position=Position(4, 4))

    default_game.players[first_player.player_id] = first_player
    default_game.add_action(command)

    default_game.iteration()
    assert first_player.units_by_id
