import pytest

from libs.terrain.terrain import Cell, Position, Terrain, TerrainSpot
from libs.terrain.terrain import spot_positions


def test_spot_positions():
    start_position = Position(0, 0)
    assert set(spot_positions(start_position, 2)) == {
        Position(0, 0),
        Position(0, 1),
        Position(1, 0),
        Position(1, 1),
    }
    assert Position(0, 0) == Position(0, 0)


@pytest.fixture()
def terrain_sample():
    terrain = Terrain()
    positions = set()
    for i in range(10):
        for j in range(10):
            positions.add(Position(i, j))

    for position in positions:
        terrain.free_positions.add(position)
        terrain.cells[position] = Cell(resources=None)
    return terrain


def test_terrain(terrain_sample):
    assert terrain_sample.can_get_spot(Position(0, 0), 4)

    spot: TerrainSpot = terrain_sample.get_spot(Position(0, 0), 4)

    assert spot.size * spot.size == len(spot.cells)
    assert not terrain_sample.can_get_spot(Position(1, 1), 2)
    assert terrain_sample.can_get_spot(Position(5, 5), 4)

    terrain_sample.remove_spot(spot)
    assert terrain_sample.can_get_spot(Position(0, 0), 4)

    spot_2: TerrainSpot = terrain_sample.get_spot(Position(5, 5), 4)
    assert not terrain_sample.can_get_spot(Position(4, 4), 2)

    terrain_sample.remove_spot(spot)
    assert terrain_sample.can_get_spot(Position(0, 0), 4)
    terrain_sample.remove_spot(spot_2)

    assert terrain_sample.can_get_spot(Position(0, 0), 10)
