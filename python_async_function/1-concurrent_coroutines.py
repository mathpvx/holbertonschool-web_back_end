#!/usr/bin/env python3
""" async routine called wait_n that takes in
2 int arguments: n and max_delay"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ returns a list of coroutines delays"""
    tasks = [wait_random(max_delay) for i in range(n)]
    delays_list = await asyncio.gather(*tasks)
    return sorted(delays_list)
