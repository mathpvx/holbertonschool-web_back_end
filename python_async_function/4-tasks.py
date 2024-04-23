#!/usr/bin/env python3
""" asynchronous routine that spawns
task_wait_random n times."""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """asynchronous routine that spawns task_wait_random n times"""
    tasks = [task_wait_random(max_delay) for i in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
