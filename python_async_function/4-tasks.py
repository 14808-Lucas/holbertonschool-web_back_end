#!/usr/bin/env python3
"""This module runs task_wait_random several times concurrently as
asyncio Tasks and collects the delays in the order they finish."""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Task_wait_random n times with max_delay and return the list
    of delays in ascending order, built from the order they complete."""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []
    for finished in asyncio.as_completed(tasks):
        delay = await finished
        delays.append(delay)
    return delays
