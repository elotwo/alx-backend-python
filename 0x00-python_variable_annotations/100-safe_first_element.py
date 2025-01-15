#!/usr/bin/env python3
""""safe first element"""
from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Return the first element"""
    if lst:
        return lst[0]
    else:
        return None
