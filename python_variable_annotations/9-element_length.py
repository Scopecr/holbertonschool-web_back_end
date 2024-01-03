#!/usr/bin/env python3
"""
Annotations for all parameters and the return value
"""


from typing import Callable
from typing import Iterable
from typing import List
from typing import Sequence
from typing import Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns list of tuples, one for each element"""
    return [(i, len(i)) for i in lst]
