#!/usr/bin/env python3
"""Write an asynchronous coroutine
that takes in an integer argument
(max_delay, with a default value of 10)"""

import asyncio
import random
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
