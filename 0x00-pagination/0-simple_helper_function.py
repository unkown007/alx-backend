#!/usr/bin/env python3
""" Simple helper module
"""


def index_range(page: int, page_size: int) -> tuple:
    """ Compute the start index and an end index
    for those particular pagination parameter
    """
    sIndex = page_size * page - page_size
    eIndex = page_size * page
    return (sIndex, eIndex)
