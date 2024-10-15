#!/usr/bin/env python3
"""
this script is about asynchrous comprehension
"""
import asyncio
import random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    this function collect list from a async generator
    """
    collect = [num async for num in async_generator()]
    return collect
