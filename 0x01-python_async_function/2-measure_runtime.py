#!/usr/bin/env python3
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n
async def measure_time(n, max_delay):
    start_time = time.perf_counter()
    await wait_n(n, max_delay)
    total_time = time.perf_counter() - start_time
    result = total_time /n
    yield result
