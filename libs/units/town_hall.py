import attr


from libs.base_unit.base_unit import BaseUnit
from libs.player.resource_wallet import ResourceWallet


@attr.s
class TownHall(BaseUnit):
    size = 4
    name = "Town Hall"
    class_id = 1

    def work(self):
        return ResourceWallet(10, 10, 10)
