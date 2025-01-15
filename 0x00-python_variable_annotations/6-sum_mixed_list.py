#!/usr/bin/env python3
"""Sum of a mixed list."""


from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Return the sum of a list of integers and floats."""

    return sum(mxd_lst)
