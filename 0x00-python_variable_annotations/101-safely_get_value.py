#!/usr/bin/env python3


from typing import Mapping, TypeVar, Any, Union

T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """Adding type annotatipons to functions"""
    if key in dct:
        return dct[key]
    else:
        return default
