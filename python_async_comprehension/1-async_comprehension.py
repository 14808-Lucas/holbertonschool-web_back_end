#!/usr/bin/env python3
"""This module collects the values produced by async_generator into a
list using an asynchronous comprehension."""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect the 10 random numbers yielded by async_generator using an
    async comprehension and return them as a list."""
    return [number async for number in async_generator()]
