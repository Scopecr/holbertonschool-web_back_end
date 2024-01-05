#!/usr/bin/env python3
"""Import sarync_generator and  write a coroutine called async_comprehension that takes no arguments
The coroutine will collect 10 random numbers using an async comprehensing over async_generator, 
then return the 10 random numbers.
"""

from typing import Lists

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Lists[float]:
    """ Async Comprehension """
    return [i async for i in async_generator()]