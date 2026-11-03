#!/usr/bin/env python3
"""The module provides an asynchronous generator that yields ten random
numbers, waiting one second before each one."""
import asyncio
import random
from typing import Generator


async def async_generator() -> AsyncGenerator[float, None]:
    """Loop ten times, asynchronously wait one second each time, then
    yield a random float between 0 and 10."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
