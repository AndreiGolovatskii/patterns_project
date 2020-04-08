from typing import Set
import attr
from abc import ABCMeta, abstractproperty, abstractmethod


@attr.s(frozen=True)
class Dot:
    x = attr.ib(converter=int)
    y = attr.ib(converter=int)

    def __add__(self, other):
        return Dot(self.x + other.x, self.y + other.y)


@attr.s
class BaseObject:
    __metaclass__ = ABCMeta
    position = attr.ib(validator=attr.validators.instance_of(Dot))
    """relative position from Dot(0, 0)"""

    @abstractproperty
    def size_x(self) -> int:
        """size by height"""

    @abstractproperty
    def size_y(self) -> int:
        """size by width"""

    def is_inside(self, dot: Dot) -> bool:
        return (
            self.position.x <= dot.x < self.position.x + self.size_x
            and self.position.y <= dot.y < self.position.y + self.size_y
        )

    def collision(self, other) -> bool:
        """check collision"""
        for dot in {
            self.position,
            self.position + Dot(0, self.size_y - 1),
            self.position + Dot(self.size_x - 1, 0),
            self.position + Dot(self.size_x - 1, self.size_y - 1),
        }:
            if other.is_inside(dot):
                return True

        for dot in {
            other.position,
            other.position + Dot(0, self.size_y - 1),
            other.position + Dot(self.size_x - 1, 0),
            other.position + Dot(self.size_x - 1, self.size_y - 1),
        }:
            if self.is_inside(dot):
                return True
        return False

    @abstractmethod
    def accept_visitor(visitor) -> None:
        """should сall visitor.process_[class_name]"""


@attr.s
class SampleObject(BaseObject):
    size_x = 3 
    size_y = 3 
    
    def accept_visitor(visitor) -> None:
        pass
    
