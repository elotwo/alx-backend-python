#!/usr/bin/env python3
wait_random = __import__('0-basic_async_syntax').wait_random
def task_wait_random(max_delay: int):
    wait_random(max_delay)

