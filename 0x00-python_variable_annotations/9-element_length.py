#!/usr/bin/env python3
"""
element_length module
"""
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples, containing the element and its length."""
    return [(i, len(i)) for i in lst]
