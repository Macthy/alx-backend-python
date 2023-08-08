#!/usr/bin/env python3
"""
Async Generator
"""

import asyncio
import random

async def async_generator() -> float:
    """
    Coroutine that yields a random number between 0 and 10
    after asynchronously waiting for 1 second for 10 times.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

# Run the async generator coroutine
if __name__ == "__main__":
    asyncio.run(async_generator())

