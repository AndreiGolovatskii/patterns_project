from typing import Set
import attr
from abc import ABCMeta, abstractproperty, abstractmethod

from libs.base_objects.cell import Cell

@attr.s
class PhysicalObject:
    __metaclass__ = ABCMeta
    position = attr.ib(validator=attr.validators.instance_of(Cell))
    """relative position from Cell(0, 0)"""

    @abstractproperty
    def size():
        """size of object is size x size"""

    def is_inside(self, cell: Cell) -> bool:
        return (
            self.position.x <= cell.x < self.position.x + self.size
            and self.position.y <= cell.y < self.position.y + self.size
        )

    def collision(self, other) -> bool:
        """check collision"""
        for cell in {
            self.position,
            self.position + Cell(0, self.size - 1),
            self.position + Cell(self.size - 1, 0),
            self.position + Cell(self.size - 1, self.size - 1),
        }:
            if other.is_inside(cell):
                return True

        for cell in {
            other.position,
            other.position + Cell(0, self.size - 1),
            other.position + Cell(self.size - 1, 0),
            other.position + Cell(self.size - 1, self.size - 1),
        }:
            if self.is_inside(cell):
                return True
        return False

@attr.s
class SamplePhysicalObject(PhysicalObject):
    size = 3 
    
    
