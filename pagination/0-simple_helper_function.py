#!/usr/bin/env python3
"""Simple helper function index range"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Simple helper function index range
    """
    start_index = page_size * (page - 1)
    page_range = start_index + page_size
    return (start_index, page_range)
