#!/usr/bin/env python3

"""Run time for four parallel comprehensions"""

import asyncio
from typing import List
from time import time
from random import uniform

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that measures the total runtime
    of executing async_comprehension four times in parallel.

    This coroutine executes async_comprehension
    four times in parallel using asyncio.gather()
    and measures the total runtime. It returns the total runtime.
    """
    start_time = time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time()
    return end_time - start_time
