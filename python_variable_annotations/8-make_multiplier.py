#!/usr/bin/env python3
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multi_func(x: float) -> float:
        return (x * multiplier)
    return (multi_func)
