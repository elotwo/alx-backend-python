#!/usr/bin/env python3
"""Zoom array."""


from typing import List, Tuple

def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """Return a zoomed-in version of a tuple by repeating elements factor times."""

    zoomed_in: List[int] = [
            item for item in lst
            for _ in range(factor)
            ]
    return zoomed_in

    array = (12, 72, 91)  # Tuple instead of list

    zoom_2x = zoom_array(array)  # Works with default factor of 2
    zoom_3x = zoom_array(array, 3)  # Corrected to use an integer factor
