#!/usr/bin/env python3
"""
code for asyncio

"""
import asyncio
import random


async def wait_random(max_delay=10):
    """
    function for random
    """
    random_num = random.uniform(0, max_delay)
    await asyncio.sleep(random_num)
    return random_num
