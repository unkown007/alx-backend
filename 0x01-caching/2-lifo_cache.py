#!/usr/bin/env python3
""" LIFOCache module
"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache inherits BaseCaching and
    implements LIFO caching algorithm
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if BaseCaching.MAX_ITEMS == len(self.cache_data):
                if key not in self.cache_data:
                    aux = list(self.cache_data.keys())[-1]
                    del self.cache_data[aux]
                    print(f"DISCARD: {aux}")
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None:
            return None
        return self.cache_data.get(key, None)
