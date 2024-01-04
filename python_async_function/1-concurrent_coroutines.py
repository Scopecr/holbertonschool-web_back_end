#!/usr/bin/env python3
"""
Basic Async Syntax
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> list[float]:
    """
        n: number of times wait_random will be called
        max_delay: max wait time for each call of wait_random
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delay_list = []
    for future in asyncio.as_completed(tasks):
        result = await future
        delay_list.append(result)
    return delay_list
