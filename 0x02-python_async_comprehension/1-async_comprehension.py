#!/usr/bin/env python3
"""
this script is about asynchrous comprehension
"""
import asyncio
import random
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[int]:
    """
    this function collect list from a async generator
    """
    collect: List[int] = [num async for num in async_generator()]
    return collect
