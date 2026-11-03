#!/usr/bin/env python3
"""This module measures how long wait_n takes to run and reports the
average time spent per coroutine."""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the total execution time of wait_n(n, max_delay) and
    return that total divided by n as a float."""
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start
    return total_time / n
