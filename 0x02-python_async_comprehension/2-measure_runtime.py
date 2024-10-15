#!/usr/bin/env python3
"""
Coroutine to measure runtime
"""
import asyncio
import random
import time
from typing import List
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
    end_time = time.time()
    total_runtime = end_time - start_time
    return total_runtime
