#!/usr/bin/env python3
"""
Async comprehension
"""

from typing import Lists

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Lists[float]:
    """ Async Comprehension """
    return [i async for i in async_generator()]
