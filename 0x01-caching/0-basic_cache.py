#!/usr/bin/env python3
""" BasicCache module
"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache inherit from BaseCaching and
    implements a basic caching system
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None:
            return None
        return self.cache_data.get(key, None)
