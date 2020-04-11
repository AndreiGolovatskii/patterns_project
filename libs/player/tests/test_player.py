import logging

from libs.base_unit.base_unit import DummyUnit
from libs.player.player import Player


def test_player_simple():
    test = Player(wallet=None, player_name='test', player_id=1)

    unit1 = DummyUnit(123)

    test.add_unit(unit1)
    assert test.get_unit(123) == unit1
    test.remove_unit(123)

