#!/usr/bin/env python3
"""Asynchronous coroutine that takes in an integer
argument (max_delay, with a default value of 10)
named wait_random that waits for a random delay between
0 and max_delay (included and float value) seconds and
eventually returns it."""

import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Returns a list of all the delays"""
    delays = []
    for i in range(n):
        delays.append(await wait_random(max_delay))
    return sorted(delays)
