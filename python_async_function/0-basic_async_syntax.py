#!/usr/bin/env python3
"""
Basic Async Syntax
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Async routine that takes in an integer argument
    """
    random_float = __import__('random').uniform(0, max_delay)
    await asyncio.sleep(random_float)
    return random_float
