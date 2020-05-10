from typing import Set
import attr
from abc import ABCMeta, abstractproperty, abstractmethod
from libs.player.resource_wallet import ResourceWallet


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

    @abstractproperty
    def class_id():
        """class id"""

    @classmethod
    def visit(cls, visitor):
        visitor.visit_unit_class(cls)

    def work(self):
        pass


@attr.s
class DummyUnit(BaseUnit):
    size = 3
    name = "Dummy Unit"
    class_id = 0

    def visit(self, visitor):
        visitor.visit_unit(self)

    def work(self):
        return ResourceWallet(0, 0, 0)
