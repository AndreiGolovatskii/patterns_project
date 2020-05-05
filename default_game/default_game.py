from libs.game.game import Game
from libs.market.market import Market
from libs.player.player import Player
from libs.player.resource_wallet import ResourceWallet
from libs.terrain.terrain import Terrain
import libs.units.units as units


def get_default_game():
    market = Market()
    market.set_product_price(units.DummyUnit, ResourceWallet(1, 1, 1))
    market.set_product_price(units.TownHall, ResourceWallet(50, 30, 20))

    player = Player(ResourceWallet(100, 100, 100), 'default', 0)

    terrain = Terrain.empty_terrain(50)
    game = Game(terrain, market)
    game.players.setdefault(0, player)

    return game
