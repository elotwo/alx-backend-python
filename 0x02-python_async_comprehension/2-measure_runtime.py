#!/usr/bin/env python3
"""
Coroutine to measure runtime
"""
import asyncio
import time
from typing import List
from importlib import import_module as using
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel and measures runtime.
    Returns the total runtime.
    """
    start_time = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    return time.time() - start_time
