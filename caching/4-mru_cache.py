#!/usr/bin/python3
""" MRU Caching """
from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache that inherits from
    BaseCaching and is a caching system: """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item to the cache """
        if key is not None and item is not None:
            if key in self.cache_data:
                # Remove the existing item so it can be added to the end
                self.cache_data.pop(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Pop the last item in MRU order (most recently used)
                discarded_key, _ = self.cache_data.popitem(last=True)
                print(f"DISCARD: {discarded_key}")
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            # Move the accessed item to the end to mark it as recently used
            value = self.cache_data.pop(key)
            self.cache_data[key] = value
            return value
        return None
