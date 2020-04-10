import attrs
from abc import abstractproperty

from libs.base_objects.physical_object import PhysicalObject
from libs.base_objects.logical_object import LogicalObject

@attr.s
class BaseObject(PhysicalObject, LogicalObject)
    @abstractproperty
    def name():
        """object human-readable name"""

    @abstractproperty
    def id():
        """object type id"""
     
