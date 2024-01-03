#!/usr/bin/env python3
"""
Type anotation that sums a list of integers and returns them into float
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of a list of floats."""
    return sum(mxd_lst)
