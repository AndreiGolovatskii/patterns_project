from typing import Set
import attr
from abc import ABCMeta, abstractproperty, abstractmethod


@attr.s
class BaseUnit:
    __metaclass__ = ABCMeta
    unit_id = attr.ib()
    spot = attr.ib(default=None)

    @abstractproperty
    def size():
        """size of unit is size x size"""

    @abstractproperty
    def name():
        """unit human-readable name"""


@attr.s
class DummyUnit(BaseUnit):
    name = "Dummy Unit"
    size = 3   
    
