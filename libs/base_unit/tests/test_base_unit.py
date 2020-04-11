import pytest

from libs.base_unit.base_unit import DummyUnit, BaseUnit


def test_base_unit():
    dummy = DummyUnit(unit_id = 1234)
    assert isinstance(dummy, BaseUnit)
    assert dummy.name == 'Dummy Unit'
    assert dummy.size == 3
    assert dummy.unit_id == 1234
