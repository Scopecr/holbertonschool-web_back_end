#!/usr/bin/env python3
"""
Basic Async Syntax
"""

import asyncio
from python_async_function import wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """
        n: number of times wait_random will be called
        max_delay: max wait time for each call of wait_random
    """
    delays = []
    for i in range(n):
        delays.append(await wait_random(max_delay))
    return sorted(delays)
