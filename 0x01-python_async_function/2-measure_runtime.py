#!/usr/bin/env python3

"""Mesuring the runtime"""

import time
from typing import List
from asyncio import run
from asyncio.tasks import Task

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average execution time for wait_n(n, max_delay).

    Args:
        n (int): Number of times to execute wait_n.
        max_delay (int): The maximum delay in seconds for each wait_n.

    Returns:
        float: The average execution time for wait_n(n, max_delay).
    """
    start_time = time.time()
    run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
