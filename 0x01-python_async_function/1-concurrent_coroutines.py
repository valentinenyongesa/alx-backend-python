#!/usr/bin/env python3

"""executing multiple coroutines at the same time with async"""

import asyncio
from typing import List
from random import uniform
from asyncio import Task


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns wait_random n times with
    the specified max_delay.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): The maximum delay in seconds for each wait_random.

    Returns:
        List[float]: List of all the delays in ascending order.
    """
    delays: List[float] = []
    tasks: List[Task] = []

    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    for task in tasks:
        delay = await task
        delays.append(delay)

    return delays
