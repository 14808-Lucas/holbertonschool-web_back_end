#!/usr/bin/env python3
"""This module wraps the wait_random coroutine in an asyncio Task so it
can be scheduled on the event loop and awaited later."""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create and return an asyncio Task that runs wait_random with the
    given max_delay on the currently running event loop."""
    return asyncio.create_task(wait_random(max_delay))
