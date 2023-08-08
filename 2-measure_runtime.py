#!/usr/bin/env python3
"""
Module that contains a function to measure execution time
"""

import asyncio
from typing import List
import time

wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: float) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (float): The maximum delay for each wait_random.

    Returns:
        float: The average execution time per coroutine.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n

