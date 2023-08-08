#!/usr/bin/env python3
"""
Module that contains an asynchronous routine for concurrent coroutines
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: float) -> List[float]:
    """
    Asynchronous routine that spawns multiple wait_random coroutines

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (float): The maximum delay for each wait_random.

    Returns:
        List[float]: A list of delay times.
    """
    delay_tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*delay_tasks)
    return sorted(delays)

