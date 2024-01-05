#!/usr/bin/env python3
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """ Compute the start index and an end index
    for those particular pagination parameter
    """
    sIndex = page_size * (page - 1)
    eIndex = page_size * page
    return (sIndex, eIndex)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert (isinstance(page, int) and isinstance(page_size, int))
        assert (page > 0 and page_size > 0)
        size = len(self.dataset())
        start, end = index_range(page, page_size)
        end = min(end, size)
        if start > size:
            return []
        return self.dataset()[start:end]
