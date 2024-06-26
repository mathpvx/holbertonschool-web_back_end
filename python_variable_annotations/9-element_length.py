#!/usr/bin/env python3
"""function that returns an iterable"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns an iterable"""
    return [(i, len(i)) for i in lst]
