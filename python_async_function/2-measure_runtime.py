#!/usr/bin/env python3
"""measures the total execution time for wait_n
and returns total_time / n"""

from typing import List
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """returns total_time / n"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    average_time = total_time / n
    return (average_time)
