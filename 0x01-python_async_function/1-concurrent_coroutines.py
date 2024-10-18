#!/usr/bin/env python3
"""
asyncio code
"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    multiple coroutines at the same time with async
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    tasks = asyncio.as_completed(tasks)
    delays = [await tasks for tasks in tasks]
    return delays
