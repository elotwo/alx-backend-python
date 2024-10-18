#!/usr/bin/env python3
"""
asyncio code
"""
import asyncio
import random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int):
    """
    multiple coroutines at the same time with async
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return delays
