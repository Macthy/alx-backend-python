#!/usr/bin/env python3
"""
Async Comprehension
"""

from typing import List

async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehension
    over async_generator and returns the list of random numbers.
    """
    return [i async for i in async_generator()]

# Run the async comprehension coroutine
if __name__ == "__main__":
    import asyncio
    asyncio.run(async_comprehension())

