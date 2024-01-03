#!/usr/bin/env python3
"""
Type anotation that takes a string k and an int OR float v as arguments
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple."""
    return (k, v ** 2)
