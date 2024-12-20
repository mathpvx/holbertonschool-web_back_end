#!/usr/bin/env python3
""" LIFO Caching """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO Caching """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if (len(self.cache_data) >= BaseCaching.MAX_ITEMS
                    and key not in self.cache_data):
                # Remove the last added item
                if self.last_key is not None:
                    print(f"DISCARD: {self.last_key}")
                    del self.cache_data[self.last_key]

            # Add/Update the item in the cache
            self.cache_data[key] = item
            self.last_key = key

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key)
