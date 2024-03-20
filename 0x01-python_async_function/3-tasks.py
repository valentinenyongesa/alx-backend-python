#!/usr/bin/env python3

"""Takes an integer max_delay and returns a asyncio.Task"""
import asyncio
from typing import Callable

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Regular function that creates an asyncio.Task for wait_random coroutine.

    Args:
        max_delay (int): The maximum delay in seconds for wait_random.

    Returns:
        asyncio.Task: The asyncio.Task object for wait_random.
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
