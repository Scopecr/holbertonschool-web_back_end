#!/usr/bin/env python3
"""
Make a type-annotated function make_multiplier that takes a float multiplier as
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float by multiplier."""
    def multiply(n: float):
        return n * multiplier
    return multiply
