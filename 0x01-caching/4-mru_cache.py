#!/usr/bin/env python3
""" MRUCache module
"""
from collections import OrderedDict


BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache inherits BaseCaching and
    implements MRU caching algorithm
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if BaseCaching.MAX_ITEMS == len(self.cache_data):
                if key not in self.cache_data:
                    mru_key, _ = self.cache_data.popitem(False)
                    print(f"DISCARD: {mru_key}")
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
