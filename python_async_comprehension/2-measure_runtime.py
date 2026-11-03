#!/usr/bin/env python3
"""This module measures how long it takes to run async_comprehension four
times in parallel with asyncio.gather."""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Run async_comprehension four times in parallel using asyncio.gather
    and return the total elapsed time in seconds."""
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.perf_counter() - start
