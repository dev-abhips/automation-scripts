from typing import List
from enum import Enum


def get_enum_values(enum_class: Enum) -> List:
    assert issubclass(enum_class, Enum)
    return [enum_type.value for enum_type in enum_class]


def get_enum_names(enum_class: Enum) -> List:
    assert issubclass(enum_class, Enum)
    return [enum_type.name for enum_type in enum_class]