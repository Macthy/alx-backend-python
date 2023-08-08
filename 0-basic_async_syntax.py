#!/usr/bin/env python3
"""
Module that contains an asynchronous coroutine
"""

import asyncio
import random

async def wait_random(max_delay: float = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay and returns it

    Args:
        max_delay (float, optional): The maximum delay. Defaults to 10.

    Returns:
        float: The random delay.
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay

