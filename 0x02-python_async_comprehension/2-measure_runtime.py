#!/usr/bin/env python3
"""
Run time for four parallel comprehensions
"""

import asyncio
from time import perf_counter
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """
    Measures the total runtime of executing async_comprehension
    four times in parallel using asyncio.gather.
    Returns the total runtime.
    """
    start_time = perf_counter()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = perf_counter()
    total_runtime = end_time - start_time

    return total_runtime

# Run the measure_runtime coroutine
if __name__ == "__main__":
    asyncio.run(measure_runtime())

