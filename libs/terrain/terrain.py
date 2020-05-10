import attr


@attr.s(frozen=True)
class Position:
    x = attr.ib()
    y = attr.ib()


def spot_positions(position: Position, size: int):
    for dx in range(size):
        for dy in range(size):
            yield Position(position.x + dx, position.y + dy)


@attr.s
class Cell:
    resources = attr.ib()


@attr.s
class TerrainSpot:
    position = attr.ib(validator=attr.validators.instance_of(Position))
    size = attr.ib()
    cells = attr.ib(validator=attr.validators.instance_of(list))


@attr.s
class Terrain:
    width = attr.ib(default=10)
    height = attr.ib(default=10)
    cells = attr.ib(factory=dict)
    free_positions = attr.ib(factory=set)

    def can_get_spot(self, position: Position, size: int) -> bool:
        for cell in spot_positions(position, size):
            if cell not in self.free_positions:
                return False
        return True

    def get_spot(self, start_position: Position, size: int) -> TerrainSpot:
        cells = list()
        for position in spot_positions(start_position, size):
            self.free_positions.remove(position)
            cells.append(self.cells[position])
        return TerrainSpot(start_position, size, cells)

    def remove_spot(self, spot: TerrainSpot) -> None:
        for position in spot_positions(spot.position, spot.size):
            self.free_positions.add(position)

    @classmethod
    def empty_terrain(cls, size):
        terrain = cls(size, size)
        terrain.free_positions = set(spot_positions(Position(0, 0), size))
        for position in terrain.free_positions:
            terrain.cells[position] = Cell(resources=None)
        return terrain

    def visit(self, visitor):
        visitor.visit_terrain(self)
