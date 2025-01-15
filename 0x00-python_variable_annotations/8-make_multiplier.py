#!/usr/bin/env python3
"""Make a multiplier."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by multiplier."""
    def fun(num: float):
        """Multiply num by multiplier."""
        return num * multiplier
    return fun
