#!/usr/bin/env python3


import asyncio
from typing import List
from asyncio import Task

task_wait_random = __import__('4-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns
    task_wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times to spawn task_wait_random.
        max_delay (int): The maximum delay in
        seconds for each task_wait_random.

    Returns:
        List[float]: List of all the delays in ascending order.
    """
    delays: List[float] = []
    tasks: List[Task] = []

    for _ in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    for task in tasks:
        delay = await task
        delays.append(delay)

    return delays
