#!/usr/bin/env python3
""" safely get value"""
from typing import TypeVar, Mapping, Any, Optional


T = TypeVar('T')

def safely_get_value(dct: Mapping[Any, T], key: Any, default: Optional[T] = None) -> Optional[T]:
    """Return the value for key."""
    if key in dct:
        return dct[key]
    else:
        return default
