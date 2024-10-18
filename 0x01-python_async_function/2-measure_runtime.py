#!/usr/bin/env python3
"""This script measures the total time for execuition """
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n, max_delay) -> float:
    """
    This return the total time
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    return (start_time - end) / n
