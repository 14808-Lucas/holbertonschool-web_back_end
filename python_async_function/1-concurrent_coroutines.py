#!/usr/bin/env python3
"""This module runs the wait_random coroutine several times concurrently
and collects the delays in the order the coroutines finish."""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Wait for n random delays concurrently and return the
      list of delays in the order they finish."""
    coroutines = [wait_random(max_delay) for _ in range(n)]
    delays = []
    for finished in asyncio.as_completed(coroutines):
        delay = await finished
        delays.append(delay)
    return delays
