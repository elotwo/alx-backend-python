#!/usr/bin/env python3
"""
this code is about adynchorous comprehesion
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    this function is a coroutine that return loop
    10 times
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
