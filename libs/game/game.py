import logging

import attr

from libs.terrain.terrain import Terrain
from libs.player.player import Player

@attr.s
class Game:
    terrain = attr.ib()
    market = attr.ib()
    players = attr.ib()

    def __attrs_post_init__(self):
        pass
     
    def interation(self):
       pass 



