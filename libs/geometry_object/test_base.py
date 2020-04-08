import pytest
from base import Dot, SampleObject


def test_base_dot():
    first = Dot(1.0, "1")
    assert first.x == 1 and first.y == 1

    second = Dot(1, 1)

    assert first == second

    third = Dot(2, 2)
    assert first != third

    assert first + second == third


def test_object():
    first = SampleObject(position=Dot(0, 0))
    assert first.is_inside(Dot(0, 0))
    assert not first.is_inside(Dot(3, 3))
    assert first.size_x == SampleObject.size_x
    assert first.size_y == SampleObject.size_y

    second = SampleObject(position=Dot(2, 2))
    assert first.collision(second)
    assert second.collision(first)
    second.position = Dot(10, 10)
    assert not second.collision(first)
