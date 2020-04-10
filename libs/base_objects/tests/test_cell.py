import pytest

from libs.base_objects.cell import Cell

def test_cell():
    first = Cell(1.0, "1")
    assert first.x == 1 and first.y == 1

    second = Cell(1, 1)

    assert first == second

    third = Cell(2, 2)
    assert first != third

    assert first + second == third

