#!/usr/bin/env python3
"""
this code is about adynchorous comprehesion
"""
import asyncio
import random


async def async_generator():
    """
    this function is a coroutine that return loop
    10 times
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
