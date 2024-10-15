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
    start_time = time.perf_counter()  # Record the start time

    # Execute async_comprehension four times in parallel
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time.perf_counter()  # Record the end time
    total_runtime = end_time - start_time  # Calculate total runtime
    return total_runtime
