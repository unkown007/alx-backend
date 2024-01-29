#!/usr/bin/env python3
import csv
import math
from typing import List, Dict, Any


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
        """ Simple Pagination
        """
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0
        size = len(self.dataset())
        start, end = index_range(page, page_size)
        end = min(end, size)
        if start > size:
            return []
        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """ Hyper Pagination
        """
        data = self.get_page(page, page_size)
        size = len(self.dataset())
        next_page = page + 1\
            if len(self.get_page(page + 1, page_size)) else None
        total_pages = int(size / page_size) if (size % page_size) == 0\
            else int(size / page_size) + 1
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
