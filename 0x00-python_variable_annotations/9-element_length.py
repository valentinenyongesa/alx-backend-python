#!/usr/bin/env python3

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return variables with appropriate values"""
    return [(i, len(i)) for i in lst]
