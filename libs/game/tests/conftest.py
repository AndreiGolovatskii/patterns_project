import pytest

from libs.game.game import Game
from libs.market.market import Market
from libs.player.player import Player
from libs.terrain.terrain import Terrain
from libs.base_unit.base_unit import DummyUnit


@pytest.fixture()
def default_market():
    market = Market()
    market.set_product_price(DummyUnit, 10)
    return market


@pytest.fixture()
def default_terrain():
    return Terrain.empty_terrain(100)


@pytest.fixture()
def default_game(default_market, default_terrain):
    return Game(terrain=default_terrain, market=default_market)
