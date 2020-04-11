import logging

import attrs

@attr.s(frozen=True)
class Cell:
    x = attr.ib()
    y = attr.ib()

def spot_cells(position: Cell, size: int):
    for dx in range(size):
        for dy in range(size):
            yield Cell(position.x + dx, position.y + dy)


@attr.s
class Terrain:
    cells = attr.ib(factory=set)

    def can_get_spot(self, position: Cell, size: int):
        for cell in spot_cells(position, size):
            if cell not in cells:
                return False
        return True

    def get_spot(self, position: Cell, size: int):
        result = TerrainSpot(position, size, set(spot_cells(position, size)))

    def remove_spot(self, spot):
        self.cells.union(spot.cells)
        spot.cells = None

@attr.s
class TerrainSpot:
    position = attr.ib()
    size = attr.ib()
    cells = attr.ib()
