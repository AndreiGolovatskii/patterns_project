import logging
from collections import deque
from time import clock
from typing import Dict

import attr

from libs.terrain.terrain import Terrain
from libs.player.player import Player
from libs.market.market import Market
from .command import command_from_json


@attr.s
class Game:
    terrain: Terrain = attr.ib()
    market: Market = attr.ib()
    players: Dict[int, Player] = attr.ib(factory=dict)
    action_queue = attr.ib(factory=deque)
    iteration_time = attr.ib(default=1)
    last_update = attr.ib(factory=clock)

    def __attrs_post_init__(self):
        pass

    def iteration(self):
        while self.action_queue:
            action = self.action_queue.pop()
            logging.info("execute action %s", action)
            status = action.execute(self)
            if not status:
                logging.info("execute action failed")

        new_time = clock()
        for player in self.players.values():
            player.iteration(new_time - self.last_update)

        self.last_update = new_time

    def add_action_from_json(self, action):
        print(action)
        self.add_action(command_from_json(action))

    def add_action(self, action):
        self.action_queue.append(action)

    def visit(self, visitor):
        visitor.visit_game(self)
