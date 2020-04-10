import pytest

from libs.base_objects.physical_object import SamplePhysicalObject
from libs.base_objects.cell import Cell


def test_physical_object():
    first = SamplePhysicalObject(position=Cell(0, 0))
    assert first.is_inside(Cell(0, 0))
    assert not first.is_inside(Cell(3, 3))
    assert first.size == SamplePhysicalObject.size
    assert first.size == SamplePhysicalObject.size

    second = SamplePhysicalObject(position=Cell(2, 2))
    assert first.collision(second)
    assert second.collision(first)
    second.position = Cell(10, 10)
    assert not second.collision(first)
