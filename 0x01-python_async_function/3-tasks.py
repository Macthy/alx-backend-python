#!/usr/bin/env python3
"""
Module that contains a function returning an asyncio.Task
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task for wait_random(max_delay)

    Args:
        max_delay (int): The maximum delay for wait_random.

    Returns:
        asyncio.Task: An asyncio.Task for wait_random(max_delay).
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task

