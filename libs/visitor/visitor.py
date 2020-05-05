import attr


@attr.s
class Visitor:
    j = attr.ib(factory=dict)

    def unit_serialize(self, unit):
        return {
            "unit_id": unit.unit_id,
            "position_x": unit.spot.position.x,
            "position_y": unit.spot.position.y,
            "class_id": unit.class_id,
            "size": unit.size,
            "name": unit.name,
            "texture": "assets/{}.png".format(unit.name),
        }

    def market_product_serialize(self, product, price):
        return {
            "class_id": product.class_id,
            "name": product.name,
            "texture": "assets/{}.png".format(product.name),
            "price": price,
            "size": product.size,
        }

    def visit_player(self, player):
        units = [self.unit_serialize(unit) for unit in player.units_by_id.values()]
        self.j.setdefault("players", list())
        self.j["players"].append(
            {
                "player_id": player.player_id,
                "player_name": player.player_name,
                "wallet": dict(player.wallet),
                "units": units,
            }
        )

    def visit_terrain(self, terrain):
        self.j["terrain"] = {"width": terrain.width,
                             "height": terrain.height,
                             "texture": "assets/default_terrain.png"}

    def visit_game(self, game):
        for player in game.players.values():
            self.visit_player(player)

        self.visit_terrain(game.terrain)
        self.visit_market(game.market)

    def visit_market(self, market):
        self.j["market"] = [
            self.market_product_serialize(p, dict(market.price[p])) for p in market.price
        ]
