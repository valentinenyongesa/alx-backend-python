#!/usr/bin/env python3

"""Take the code from wait_n and
alter it into a new function task_wait_n"""

import asyncio
from typing import Union


async def wait_random(max_delay: int = 10) -> Union[int, float]:
    """
    Asynchronous coroutine that waits for a random delay and returns it.

    Args:
        max_delay (int): The maximum delay in seconds. Defaults to 10.

    Returns:
        Union[int, float]: The random delay in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


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
